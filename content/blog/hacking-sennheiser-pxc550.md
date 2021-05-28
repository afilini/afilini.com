+++
title = "Hacking my Sennheiser PXC 550"
date = "2021-05-25"
description = "Fixing the annoying issue that makes them turn off and on constantly"
tags = [
    "hardware",
    "hacking",
    "pxc550"
]
+++

### aka "Why the fuck are they constantly turning off by themselves??"

Once upon a time, when lockdowns and closed borders weren't really a thing, I used to spend a decent amount of time travelling, most of the time on an airplane. Since they tend to be rather noisy environments, I started to
look around for a pair of noise-cancelling headphones that would allow me to enjoy music while I wait to get from point *A* to point *B* at 35000 ft.

In the end I settled for a pair of [Sennheiser PXC 550][msAFRq_link][^msAFRq] because of... <abbr title="tbh I don't remember why I picked those instead of the Sony MX-whatever. They were probably just cheaper.">reasons</abbr>.

As an absolutely average music listener who listens to (high bitrate) MP3s over Bluetooth, they sounded great to me and the noise-cancelling effect was also pretty decent.

Fast forward almost a year and one day they just randomly reboot while I'm using them. I didn't think too much of it, "maybe it's just the low battery". But the more time went on, the more they started doing it,
up to the point where they would reboot at least once every time I would use them. Eventually I also noticed that this issue seemed somewhat related to the movements I made with my head: it would happen more
frequently if I was walking rather than sitting still at my desk.

At this point I should probably explain how's that even possible: is there a loose connection somewhere inside? Why the hell would they turn off if I just move my head without touching them?

Well, Sennheiser apparently thought it was a good idea to make the headphones turn on automatically when they are unfolded out of their case and worn.

And how do they do that? With a little magnet in the frame and an [Hall effect sensor][AnOuAO_link][^AnOuAO] in the right earcup. The sensor should pick up the magnetic field when the earcup is aligned with the frame, and make the headphones turn on. The
magnetic field should then disappear when the headphones are folded away, so they would turn off automatically.

Clearly this doesn't work so well considering the amount of Reddit posts[^uIbDkh]<sup>,</sup>[^JkXGPd]<sup>,</sup>[^PCRsLl] I managed to find describing headphones that turn off and on by themselves.

I tried replacing the magnet with a [different one][PNpqCE_link][^PNpqCE], hoping that it would be stronger and lead to a more stable signal for the sensor, but that didn't help.

In the end I just accepted that I would have to live with this issue: it was too late to get an RMA, and the issue seemed like a design flaw of that specific model rathern than just a defective unit, so even getting
a new pair wouldn't have fixed the problem permanently.

The people I work with must have heard me say "sorry my headphones disconnected, can you repeat that?" at least a dozen times, but as bad as it sounds, it wasn't a complete dealbreaker for me. Sure, it was annoying,
but in the end I could still get to the end of hour-long calls with one or maybe two disconnections. It was still *good enough* that I would just live with it instead of trying to fix the problem.

That is, until one day I started randomly looking for more workarounds and I found [this other][OXOImz_link][^OXOImz] Reddit post that described how the physical Bluetooth on/off switch could be re-routed and used as a power switch. A brilliant idea!

The post didn't have any pictures though, so I would have to figure things out by myself. I was kinda worried I would find a super crammed PCB, but I decided to give it a shot and opened the right earcup (the ones that
houses all the interesting circuitry) to get to work.

In the end it turned out to be pretty easy, even for somebody with crappy soldering skills like myself. I unfortunately didn't document the whole process, but I took this picture before closing them up:

{{< my-figure url="/images/blog/hacking-my-sennheiser-pxc-550/pxc550-annotated.jpg" caption="Annotated shot of the right earcup after the mod" >}}

Highlighted you can see:
* In purple the disconnected Hall effect sensor. To unplug it you can push forward (away from the white piece) the little black part of the connector, and then lift it up slightly to pull the flat cable out.
* In blue the first wire soldered to a test point right above the sensor connector. From a quick experiment it looks like the two inner pins of the connector are both GND while the two outer pins (and the test pad) are the "signal" pins.
When pulled to GND they will make the headphones turn on.
* In yellow the second wire soldered to a relatively large ground pad.
* In red the two wires that were originally soldered to the switch, joined toghether to force Bluetooth to be always on and then moved out of the way.

And that was it! I've been using them with this mod for almost a month now and they've been working great. The new power switch is not super easy to access, but I'll take that over having them randomly turning off.

[OXOImz_link]: https://www.reddit.com/r/sennheiser/comments/gmcmzs/pxc_550_power_switch_fix/
[msAFRq_link]: https://en-us.sennheiser.com/wireless-headphone-headset-bluetooth-noise-cancelling-pxc-550-travel
[AnOuAO_link]: https://en.wikipedia.org/wiki/Hall_effect_sensor
[PNpqCE_link]: https://www.amazon.it/dp/B00TACKU36/ref=cm_sw_r_u_apa_glt_i_2TW0DERF91YB3P80X749

[^uIbDkh]: *PXC 550&#x27;s turning on and off randomly, any ideas hot to fix? : sennheiser* [[original]](https://www.reddit.com/r/sennheiser/comments/bxx0dx/pxc_550s_turning_on_and_off_randomly_any_ideas/) [[archived]](https://archive.md/31yE3)
[^JkXGPd]: *Problems with PXC 550. Turning off randomly at very small angles and slight head movement. : sennheiser* [[original]](https://www.reddit.com/r/sennheiser/comments/ggoott/problems_with_pxc_550_turning_off_randomly_at/) [[archived]](https://archive.md/8J7Ul)
[^PCRsLl]: *PXC 550 will auto shut off : headphones* [[original]](https://www.reddit.com/r/headphones/comments/aqtbf8/pxc_550_will_auto_shut_off/) [[archived]](https://archive.md/7YquU)
[^OXOImz]: *PXC 550 Power Switch Fix : sennheiser* [[original]](https://www.reddit.com/r/sennheiser/comments/gmcmzs/pxc_550_power_switch_fix/) [[archived]](https://archive.md/D8GzG)
[^msAFRq]: *Sennheiser PXC 550 TRAVEL - Wireless Headphone Headset Bluetooth® - Active Noise cancelling* [[original]](https://en-us.sennheiser.com/wireless-headphone-headset-bluetooth-noise-cancelling-pxc-550-travel) [[archived]](https://archive.md/KYljs)
[^AnOuAO]: *Hall effect sensor - Wikipedia* [[original]](https://en.wikipedia.org/wiki/Hall_effect_sensor) [[archived]](https://archive.md/gyUIC)
[^PNpqCE]: *first1magnets F331-N35-50 - Magnete al neodimio N35, diametro 3 mm x spessore 1 mm, forza magnetica 0,13 Kg (50 pezzi): Amazon.it: Fai da te* [[original]](https://www.amazon.it/dp/B00TACKU36/ref=cm_sw_r_u_apa_glt_i_2TW0DERF91YB3P80X749) [[archived]](https://archive.md/PyqK7)
