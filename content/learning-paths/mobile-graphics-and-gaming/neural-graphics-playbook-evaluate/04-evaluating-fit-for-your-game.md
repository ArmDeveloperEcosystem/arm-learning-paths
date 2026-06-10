---
title: Evaluate fit for your game
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

At this point, you know a little bit about the building blocks. Now the question is whether this is worth applying to your project. That depends more on your game than on the technology itself. Things such as content type, camera behavior, and performance targets all play a role. This section focuses on helping you make that call.

Neural techniques aren't designed to be equally useful everywhere. Anyone who develops a game knows how complicated it is to build a one-size-fits-all solution that both looks good and is practical to integrate.

In some scenarios, these techniques deliver immediate and meaningful value—freeing up performance or letting you push visual quality further without a big rewrite. In others, the gains are smaller, or come with tradeoffs that make them harder to justify.

Arm Neural Technology is a set of tools that work best when applied to the right problems. This section shares what has been learned about that so far.

## Is NFRU right for me?

For most teams, NFRU is the easiest place to start. It's available as an Unreal Engine plugin, with more developer tools coming soon.

It behaves in a familiar way. You enable the plugin and evaluate how it looks in your own project. There's no need to train or customize anything, and no major changes to your content pipeline. It feels closer to a traditional engine feature than something experimental.

NFRU delivers more frames for less work. Because it works across a wide range of content, it's also a good way to understand how neural techniques behave in your game.

## Is NSSD right for me?

NSSD is a different kind of investment.

Where NFRU helps you get more out of what you already have, NSSD opens the door to things that weren’t really possible before—especially on mobile.

When paired with modern lighting approaches such as MegaLights, it allows you to start working with:

- stronger contrast
- softer shadows from larger light sources
- more dynamic lighting, instead of relying heavily on baked solutions

For a long time, mobile rendering has been shaped by constraint. Lighting in particular has been simplified—not because teams didn’t want more, but because the cost was too high. Fully dynamic, high-quality lighting just wasn’t something you could rely on mobile platforms.

NSSD starts to change that.

In developing Neural Dawn with Sumo Digital, this led to a shift in how scenes were approached. Instead of working around limitations, the team started exploring what would happen if those limitations were relaxed.

The project deliberately pushed into cases that are usually avoided—scenes with heavy noise, strong contrast, and more complex light interactions than are normally attempted on mobile.

That’s where NSSD creates its real value: making new kinds of content feel viable.

That flexibility comes with a cost. NSSD depends heavily on the model matching your content.

This introduces a different kind of workflow. To get the best results, you might need to:

- capture representative data from your game
- train or fine-tune models
- iterate on outputs and debug model issues

For many teams, this is unfamiliar territory. It takes time to get comfortable with, and it’s not something you can treat as a simple drop-in feature.

That’s why NSSD should be seen as an investment.

It makes the most sense for teams that are willing to explore new workflows and push beyond what current pipelines allow. In return, it gives you more control over how the final image is reconstructed, and a new kind of freedom in how you build your scenes.

## Additional considerations

As with most new technologies, there are cases where tradeoffs become more visible.

### Evaluating quality

You might be asking: "How do I know my game looks just as good running neural graphics?"

Before target hardware was available, the Neural Dawn work focused on image quality. Frames were captured, reconstruction ran offline, and results were compared against a high-quality reference.

Metrics such as PSNR and FLIP are useful for getting a baseline, but they don't tell the full story. What matters in practice is how the image behaves over time—whether it stays stable, how artifacts show up in motion, and whether players actually notice.

The question is whether it looks as good as it can, and whether it enables something you couldn't do before.

### Setting expectations

Neural graphics is still evolving, and different techniques are at different stages.

NFRU is something you can pick up today and evaluate quickly. It's low risk and easy to reason about.

NSSD is earlier and more involved. It requires time, iteration, and a willingness to work with a different kind of pipeline. It also points to where things are heading—especially for teams interested in pushing visual quality on mobile.

Neural graphics creates the most value when used intentionally—either to save performance where it matters, or to unlock things that weren't previously feasible.

### Fallbacks and scalability

Unlike many traditional rendering features, the runtime cost of neural graphics techniques is generally more stable across content. The cost of running NFRU or NSSD itself doesn't scale heavily with scene complexity, number of lights, or material count in the way traditional rendering passes often do.

With that said, one important thing to think about early is what happens on devices that don't support Arm Neural Technology.

NFRU doesn't currently have a direct shader-based fallback equivalent. If a device can’t support NFRU, the recommendation is generally to scale the game in more traditional ways, for example by lowering the resolution. NFRU then becomes a way to enhance that baseline, rather than a hard dependency

NSSD is different. At the moment, there isn't really a direct fallback path for what it enables. In practice, this means that if you build content around NSSD, you should expect to support a separate rendering path for devices that can't run it. That's one of the reasons NSSD is positioned differently throughout this playbook. It's a deeper rendering investment intended for teams that want to get ahead by experimenting with new features.

This is also one of the reasons to evaluate these techniques early in development. Understanding the fallback story helps avoid building content that becomes difficult to scale across different device tiers later on.

## Is my game a good candidate?

Your game type determines whether neural graphics is a good fit.

Neural graphics works best with specific scene types. When paired with MegaLights, success depends on how your scenes are structured and how much you rely on lighting to carry the visual experience. The guidance generally aligns with what works for ray tracing.

The setups that worked best were fairly contained, interior environments. Small to mid-sized spaces where you can control what's on screen and how light behaves. That's a big reason why much of Neural Dawn takes place in enclosed environments. An enclosed environment gives you more control and makes it easier to lean into dynamic lighting without things breaking down.

Those kinds of scenes are also where MegaLights really shines. You can place a lot of smaller dynamic lights, play with contrast, and build atmosphere in a way that would normally be too expensive. Moving from darkness into light, scene by scene, became a core part of how the experience was structured. Instead of relying on baked lighting, which can take a long time to generate and doesn't adapt at runtime, the team could keep things dynamic and iterate much faster.

### Where things get harder

Where things get harder is when moving outside of those controlled environments. Large outdoor scenes are more challenging. You lose that tight control over lighting, and things such as sunlight become harder to handle. Directional lights in particular require a lot of tuning to look right, and that quickly becomes a time sink. It's not that these scenes are impossible, but they're not where you get the most value today.

Certain types of content that are already tricky for ray tracing also present challenges. Foliage is a good example. Lots of small, thin, semi-transparent elements — such as grass or leaves — are difficult to handle cleanly. In the Neural Dawn project, the team was quite intentional about what was included. Similarly, heavy use of world position offset, especially with lots of instances, needs to be kept in check.

There are also some visual edge cases worth calling out. Ghosting can appear in certain situations, such as decals (for example, moss), although that's not unique to this approach — it's something you see with most temporal denoisers and upscalers. With NSSD specifically, issues such as flickering (sometimes showing up as black dots), instability when the character is moving quickly over detailed surfaces, and subtle changes in fine detail that can make surfaces or silhouettes look like they're shifting across frames have been observed.

VFX can also be tricky. Bright, fast-moving effects — especially sprite-based ones — can end up looking blurrier than expected. This is an area of active improvement, but it's something to be aware of when evaluating your own content.

On the NFRU side, the main thing to keep in mind is that you’re still rendering at your base frame rate. If your game is running at 30 FPS and you’re generating intermediate frames, there’s still an inherent delay in the system. For most content that’s fine, but for something such as a fast-paced racing game, that tradeoff might be more noticeable.

What stood out most from an art direction point of view was how much freedom this approach gives you when it works. Being able to rely on dynamic lighting — really dynamic lighting — and see it respond in real time was a big shift. It changes how you think about building scenes.

### Conclusion

If you had to boil it down, a good candidate today looks something like this: 

_A game with controlled environments, where lighting plays a big role in the look and feel, and where you’re willing to trade some predictability for flexibility. If your game depends heavily on large open worlds, dense foliage, or very fast, high-precision visuals, you’ll likely run into more friction. That doesn’t mean those cases won’t be supported—it just means they’re not where this approach is the strongest today._

It's also worth noting that none of this is static. These are the first real attempts at bringing ray-traced lighting and fully dynamic scenes to mobile in a practical way. There isn't a long history of best practices yet, and part of the work right now is figuring out what those should be. That's also what makes it interesting.

The technology continues to evolve alongside the teams building with it. What works well today will keep improving, and some of the rough edges visible now are already being addressed. This really is the start of something new for mobile graphics.
