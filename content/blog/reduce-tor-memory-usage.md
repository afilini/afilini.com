+++
title = "Reducing Tor's memory usage"
date = "2021-09-04"
description = "Dramatically decreasing the memory footprint of a fast Tor relay with jemalloc"
tags = [
    "tor",
    "relay",
    "libc",
    "jemalloc",
]
+++

I recently migrated my Tor relay from a Fedora 32 container to a NixOS container. For some reason, it magically stared using a lot less CPU, but also a bit more memory.

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Today&#39;s weird thing that I&#39;m too afraid to investigate: moved my Tor relay container from Fedora 32 to NixOS. Same configuration, only went from v0.4.5.8 to v0.4.5.9 in the process.<br><br>Now it&#39;s using 1/5 of the CPU, a bit more RAM and it yields ~the same bandwidth 🤔🧐 <a href="https://t.co/kWy4NyOcaI">pic.twitter.com/kWy4NyOcaI</a></p>&mdash; Alekos Filini (@afilini) <a href="https://twitter.com/afilini/status/1431571319917793285?ref_src=twsrc%5Etfw">August 28, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

[[archived]](https://archive.md/TWw4c)

After a few days it was clear that it was struggling with the memory, I could see a few big drops in memory usage where the kernel swapped out a lot of pages.

[In the official docs][PFqdPo_link][^PFqdPo] docs they recommend recompiling with a different malloc implementation (which they also use in the official release tarballs), but being lazy I didn't really want to spend time configuring
NixOS to compile the package locally with non-standard flags. So I decided to try the quick route first: changing the malloc implementation at runtime.

NixOS supports [a few different memory allocators][VauVPy_link][^VauVPy]. Most of them are designed to aid development, by trying to help finding undefined behaviors in the usage of allocated memory. There is one provider that can help
us, though: `jemalloc`.

[`jemalloc`][eJRsGS_link][^eJRsGS] is designed to reduce memory fragmentation, which is very likely the cause of the high memory usage of my relay, since it doesn't seem to be connected to the bandwidth provided but just slowly grows
over time.

So, I tried adding `environment.memoryAllocator.provider = "jemalloc"` to my configuration, restarting Tor, and...

{{< my-figure url="/images/blog/reduce-tor-memory-usage/glibc.png" caption="First 24 hours of Tor running with the default libc (glibc)" >}}

{{< my-figure url="/images/blog/reduce-tor-memory-usage/jemalloc.png" caption="First 24 hours of Tor running with jemalloc" >}}

[PFqdPo_link]: https://support.torproject.org/operators/relay-memory/
[VauVPy_link]: https://github.com/NixOS/nixpkgs/blob/nixos-21.05/nixos/modules/config/malloc.nix#L61-L83
[eJRsGS_link]: http://jemalloc.net

[^PFqdPo]: *Why is my Tor relay using so much memory? | Tor Project | Support* [[original]](https://support.torproject.org/operators/relay-memory/) [[archived]](https://archive.md/KqwVE)
[^VauVPy]: *nixpkgs/malloc.nix at nixos-21.05 · NixOS/nixpkgs · GitHub* [[original]](https://github.com/NixOS/nixpkgs/blob/nixos-21.05/nixos/modules/config/malloc.nix#L61-L83) [[archived]](https://archive.md/jAieS)
[^eJRsGS]: *jemalloc* [[original]](http://jemalloc.net) [[archived]](https://archive.md/TMIyN)
