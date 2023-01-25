+++
title = "Taking a Break From BDK"
date = "2023-01-25"
description = "Taking a break from my maintainer role of BDK, what it means and what's next"
tags = [
    "bdk",
    "personal",
]
+++

My yearly grant from Brink is about to expire, and I decided not to renew it so that I could take a break from BDK.

## Why?

The short answer is that lately I've been finding it hard to work on BDK: what I mean is that, for a reason that I can't really explain
myself, I lost some of the motivation that was driving me to work on this project. Essentially I went from being compltely captured and
fascinated by working on it, to having to force myself to work because I would naturally tend to procrastinate.

This is very unusual for me, over the years I've always been very passionate about what I do and I would normally find it hard to *stop*
working on something. I would have to remind myself to eat and sleep, because my interest was completely captured by whatever project I
was working on at the time.

Maybe I'm burnt out, or maybe it's something else. Either way, this had a pretty big negative impact on my productivity, and as a
consequence on my happiness in general because I felt like my work was not up to my standards.

## What's gonna change?

First of all let me talk a bit about the roadmap I have in mind: over the past few months we have been working on what we call "[bdk\_core][rvYlbh_link][^rvYlbh]",
essentially a set of core libraries that can be used as building blocks for a wallet. The difference between `bdk` and `bdk_core` is that
the core libraries are at a very low level: they are very powerful but also harder to use compared to the full `bdk` library.

The plan is to eventually update the `bdk` library to internally use the "core" components: this would give advanced users more flexibilty,
because they would be able to work at the "core" level if they need to, while keeping the general API easy enough for everybody to use.

We were hoping to be done by the end of 2022, and while we are actually pretty close we still aren't finished yet. For this reason, I think it's
best for me to stay around at least until that's done, and we will release [BDK `v1.0`][krRYLO_link][^krRYLO].

After that's finished the main difference will be that I won't be reviewing PRs or hanging around so much in the BDK discord. Or maybe I will,
sometimes. I don't know. Either way, there are a bunch of other people working on BDK full time with grants from entities like Spiral, so
I'm not concerned at all with the development side of things while I'm away.

## What I'm gonna do next?

I'm planning to do consultancy/contracting work for a few months: I think it will be good for me to spend time on a bunch of different projects to
find the motivation and the love for coding that I seem to have lost a bit lately.

I'm also working on opening [hack.bs][UAlowC_link][^UAlowC], which is a physical hackerspace for bitcoiners and cypherpunks in northern Italy. I'm sure that will
take some of my time over the next few months, although being strictly non-profit I will still have to find myself proper gigs to earn some
money.

If you are an individual or a company and you feel like you could use my help somehow, feel free to shoot me an [email](/contact). I have experience
in many fields of computer science, ranging from web development, to embedded development, to devops/sysadmin.

## Conclusion

It's very hard for me to step down (even if temporarily) from my role with BDK, but I feel like this is the right thing to do given the
circumnstances. I hope taking a break will allow me to come back in the future with even more motivation and more ideas.

I'd like to thank Brink for the support they've given me in the past couple of years, and I'd like to apologize to everybody for my work
which I know has not been great lately.


[UAlowC_link]: https://hack.bs.it/
[rvYlbh_link]: https://bitcoindevkit.org/blog/bdk-core-pt1/
[krRYLO_link]: https://bitcoindevkit.org/blog/road-to-bdk-1/

[^UAlowC]: *hack.bs* [[original]](https://hack.bs.it/) [[archived]](https://archive.md/iQSPI)
[^rvYlbh]: *`bdk_core`: a new architecture for the Bitcoin Dev Kit | Bitcoin Dev Kit Documentation* [[original]](https://bitcoindevkit.org/blog/bdk-core-pt1/) [[archived]](https://archive.md/LjtcN)
[^krRYLO]: *The Road to BDK 1.0 | Bitcoin Dev Kit Documentation* [[original]](https://bitcoindevkit.org/blog/road-to-bdk-1/) [[archived]](https://archive.md/1Z3nT)
