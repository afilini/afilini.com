+++
title = "Fuzz Your Mother If You Want Fuzz"
date = "2022-08-02"
description = "Fuzzing BDK's algorithms to find hidden bugs"
tags = [
    "bdk",
    "fuzzing",
]
+++

I've always seen fuzzers as a very useful tool to stress-test parsers or more generally any piece of code that deals with untrusted data. That's clearly where they shine, looking at live coverage data they can tweak
the input to trigger new code paths, potentially unveiling bugs.

But after seeing a [PR][mdNzzr_link][^mdNzzr] fixing a couple of issues that had been hiding in our coin selection code, I realized that in fact any piece of code, any algorithm, could benefit from being run through a fuzzer: after all,
whether you are dealing with trusted or untrusted data, you are just looking at a bunch of instructions and bugs generally hide in spots that are rarely or never taken. And a fuzzer could help hunt those down.

So I decided to give it a shot: I could try fuzzing our coin selection and transaction creation code. Specifically this code deals with picking which UTXOs to add to a transaction, how much we should allocate for fees,
whether we should add a change output or not. And at the end produces an unsigned PSBT and a little recap of the transaction (how much the wallet is "sending" and "receiving", and the absolute fee), which we call
[`TransactionDetails`][gcWRLS_link][^gcWRLS].

The [code itself][pdrBGa_link][^pdrBGa] is pretty simple: we setup a wallet with a few mocked UTXOs, like we do normally in the tests, and then we try to build transactions and perform some assertions on the result.

The fuzzer controls three key things:
- How many UTXOs the wallet has and their value
- At which fee rate the transaction should be created
- How many outputs to create and their value

We apply some limitations to the inputs and outputs, to avoid causing crashes that we don't care about: for example, each input and output is capped at a relatively low value, because otherwise just having two inputs or outputs
very close to the maximum `u64` value would cause an overflow when adding them together in the coin selection code.

We also cap the fee rate at a maximum of `100000` sat/vb and the number of inputs and outputs to make sure we can keep the number of iterations per second a bit on the high end.

Immediately after starting it, we could see a few interesting crashes:

## Bug #1: BDK accepts `Nan`, infinite or negative fee rates

Fee rates are expressed as floating point numbers, for obvious reasons. But floating point numbers can take many different values, including (positive and negative) infinity, "not a number" (`NaN`), and even
negative zero!

Clearly those aren't valid fee rates and we should [ensure we don't accidentally allow them][sXdxZZ_link][^sXdxZZ], or we risk breaking the coin selection in many interesting ways.

## Bug #2: The Branch and Bound CS assumes UTXO effective values are always positive

The Branch and Bound coin selection works with the "effective value" of a UTXO, meaning that instead of just looking at its value (which is always positive), it also subtracts the fee cost for spending it. Generally
UTXO values are much, much larger than the fee cost, and even at moderately high fee rates they will remain positive.

That said, we can't assume so and our code should handle negative effective values correctly.

Here we actually found two different bugs related to negative effective values:

### Assuming the sum of effective values is positive

At some point in the branch and bound code we would sum all the effective values of our UTXOs, which are represented as `i64`s, and convert the sum to a `u64` using `try_into()`. But instead of handling the error
our code had an "expect", which is basically like asserting the result is always good. Hence, if the sum of effective values would end up being negative, BDK would crash with `SIGABRT` when trying to perform this conversion.

This is generally not the case, but as we've just said we should not completely rule out this case and we should handle the error properly.

### The sum of all effective values is the highest amount we can spend

Right after summing up all the effective values, we used to compare the sum to our "target" value and return an early error in case the target was higher. The rationale was that if we couldn't reach
the target even when spending all of our UTXOs, there was no need to bother running the actual coin selection algorithm. We could just error out immediately and tell the user there aren't enough funds in the wallet.

Again, this assumption would hold true assuming all the effective values were positive. But if we have UTXOs with negative effective values, we should remove them first from our set (as it doesn't make economic sense to
spend them) and then perform this check.

This is, in fact, [the solution][PFUdYc_link][^PFUdYc] we decided to adopt: we exclude all the (optional) UTXOs with negative effective value, and then perform this check. If we still can't reach the target, then we can return an early error.

## Review Buddy

On top of the bugs we found in the live code of BDK, the fuzzer also proved to be a very helpful "review buddy" when looking at the original PR that started this journey: the PR itself fixed a constant we had in our code, that would essentially
cause BDK to spend a little bit more than necessary in fees for each input added[^1].

However, fixing this constant started making the fuzzer complain that some transactions had an actual fee rate lower than what we asked for. We were a bit puzzled by this, because we had just checked many times that the constant
was correct, so why was this failing now?

It turns out there was *another* wrong constant, this time at least not in live code, but in our tests (which was copied over to the fuzzer): most of our tests work with `wpkh()` descriptors, meaning that when satisfied
they have an empty `scriptSig` and they contain two items in their witness, the public key (33 bytes long) and the signature (at most 72 bytes long, with the sighash byte included).

To mock signing in the tests we instead used to push a single item to the witness of lengh 108, but this is actually wrong:

- A correctly signed transaction would contain in the witness 1 byte for the first PUSH, 33 bytes for the pubkey, another byte for the second PUSH and then 72 byes for the signature. `1 + 33 + 1 + 72 = 107`.
- Our mocked transaction would contain 1 byte for the PUSH and then 108 bytes of dummy data for a total of `109` (!!) bytes.

Why didn't we notice this previously? Because the other wrong constant would cover the extra fees for the extra two bytes, which weigh two weight units. So in all our tests our transactions would never have a fee
rate lower than expected.

Coincidentally, this mistake made it even harder to notice that we were overpaying, because now instead of adding four extra weight units we were only adding two (at least in the tests where we used this mocked signing).

## Conclusion

I'd like to thank my other, albeit slower and less effective, review buddy, [Daniela Brozzoni][kPsTuR_link][^kPsTuR] for her help debugging and digging through the code to fix all these issues.

I can't help but feel a bit ashamed about all this: I find it hard to accept that after having looked at the same few lines of code so many times there could still be all these issues scattered around.

However, I don't think hiding or sweeping this whole story under the rug is the right way to handle this: I decide to write this blog post hoping others will find it useful and maybe apply the same techniques to
improve their projects.

I personally look forward to using this more in the future and potentially even integrate this as part of our automated continuous integration on some key areas.

I guess the lesson here is that sometimes the solution to your problems isn't an extra hour spent writing tests, it's just running your code through 100M iterations with semi-random values on a powerful AWS machine.

## Footnote

Wondering what's up with the title? It's a reference to [this tweet](https://archive.ph/jOKIP).

[^1]: We would count an extra 4 weight units per-input for the `scriptSig` len, which it turns out is already accounted for by miniscript's `max_satisfaction_weight`.

[gcWRLS_link]: https://docs.rs/bdk/0.20.0/bdk/struct.TransactionDetails.html
[mdNzzr_link]: https://github.com/bitcoindevkit/bdk/pull/666
[pdrBGa_link]: https://github.com/afilini/bdk/commit/edf52c97b664b6ad81e934f865c151bb9119a886#diff-7752c03aaebb94d64d83a051350a05c0c733e3c3833f18a2f9b953b7f8619a39
[sXdxZZ_link]: https://github.com/bitcoindevkit/bdk/pull/694
[PFUdYc_link]: https://github.com/bitcoindevkit/bdk/pull/693
[kPsTuR_link]: https://twitter.com/danielabrozzoni

[^gcWRLS]: *TransactionDetails in bdk - Rust* [[original]](https://docs.rs/bdk/0.20.0/bdk/struct.TransactionDetails.html) [[archived]](https://archive.ph/pgHqg)
[^mdNzzr]: *Various fixes to the `fee_amount` calculation in `create_tx` by danielabrozzoni · Pull Request #666 · bitcoindevkit/bdk · GitHub* [[original]](https://github.com/bitcoindevkit/bdk/pull/666) [[archived]](https://archive.ph/VitHp)
[^pdrBGa]: *Fuzz the Branch and Bound coin selection · afilini/bdk@edf52c9 · GitHub* [[original]](https://github.com/afilini/bdk/commit/edf52c97b664b6ad81e934f865c151bb9119a886#diff-7752c03aaebb94d64d83a051350a05c0c733e3c3833f18a2f9b953b7f8619a39) [[archived]](https://archive.ph/wQh6n)
[^sXdxZZ]: *Add assertions in the FeeRate constructor by afilini · Pull Request #694 · bitcoindevkit/bdk · GitHub* [[original]](https://github.com/bitcoindevkit/bdk/pull/694) [[archived]](https://archive.ph/nh5Jp)
[^PFUdYc]: *Fix the early InsufficientFunds error in the branch and bound by afilini · Pull Request #693 · bitcoindevkit/bdk · GitHub* [[original]](https://github.com/bitcoindevkit/bdk/pull/693) [[archived]](https://archive.ph/fGJAc)
[^kPsTuR]: *Daniela ⚡ - (@danielabrozzoni)* [[original]](https://twitter.com/danielabrozzoni) [[archived]](https://archive.ph/AM9We)

