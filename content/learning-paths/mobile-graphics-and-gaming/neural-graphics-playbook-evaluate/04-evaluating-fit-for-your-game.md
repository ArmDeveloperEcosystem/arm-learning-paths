---
title: Evaluating fit for your game
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

At this point, you know a little bit about the building blocks. Now the question is whether this is worth applying to your project. That depends more on your game than on the technology itself. Things like content type, camera behavior, and performance targets all play a role. This section focuses on helping you make that call.

Let’s start with an unexpected confession: We didn’t create neural techniques to be equally useful everywhere. Anyone who develops a game knows how complicated it is to build a one-size-fits-all that both looks good but is also practical to integrate.

In some scenarios, our techniques deliver immediate and meaningful value—freeing up performance or letting you push visual quality further without a big rewrite. In others, the gains are smaller, or come with tradeoffs that make them harder to justify.

Neural graphics is a set of tools that work best when applied to the right problems. In this section, you will learn more about what we’ve learned in that area so far.

## Is NFRU right for me?

For most teams, NFRU is the easiest place to start. It’s available as an Unreal Engine plugin with more developer tools coming soon.

It behaves in a way that feels familiar. You enable the plugin, and evaluate what it looks like in your own project. There’s no need to train or customize anything, and no major changes to your content pipeline. In that sense, it feels much closer to a traditional engine feature than something experimental.

What it gives you is straightforward: more frames for less work. Because it works across a wide range of content, it’s also a good way to get a feel for how neural techniques behave in your game.

## Is NSSD right for me?

NSSD is a different kind of investment.

Where NFRU helps you get more out of what you already have, NSSD opens the door to things that weren’t really possible before—especially on mobile.

When paired with modern lighting approaches like MegaLights, it allows you to start working with:

- stronger contrast
- softer shadows from larger light sources
- more dynamic lighting, instead of relying heavily on baked solutions

For a long time, mobile rendering has been shaped by constraint. Lighting in particular has been simplified—not because teams didn’t want more, but because the cost was too high. Fully dynamic, high-quality lighting just wasn’t something you could rely on mobile platforms.

NSSD starts to change that.

In developing Neural Dawn with Sumo Digital, this led to a shift in how scenes were approached. Instead of working around limitations, we started exploring what would happen if those limitations were relaxed.

We deliberately pushed into cases that are usually avoided—scenes with heavy noise, strong contrast, and more complex light interactions than we’d normally attempt on mobile.

That’s where NSSD creates its real value: making new kinds of content feel viable.

That flexibility comes with a cost. NSSD depends heavily on the model matching your content.

This introduces a different kind of workflow. To get the best results, you may need to:

- capture representative data from your game
- train or fine-tune models
- iterate on outputs and debug model issues

For many teams, this is unfamiliar territory. It takes time to get comfortable with, and it’s not something you can treat as a simple drop-in feature.

That’s why NSSD should be seen as an investment.

It makes the most sense for teams that are willing to explore new workflows and push beyond what current pipelines allow. In return, it gives you more control over how the final image is reconstructed—and a new kind of freedom in how you build your scenes.

## Additional considerations

Like with most new technologies, there are cases where tradeoffs become more visible.

### Evaluating quality

Reading this, you might be asking yourself How do I know that my game looks just as good running neural technologies?

Before having access to target hardware, the work with Neural Dawn work focused on image quality. We captured frames, ran reconstruction offline, and compared the results against a high-quality reference.

Metrics like PSNR and FLIP were useful for getting a baseline, but they don’t tell the full story. What matters in practice is how the image behaves over time—whether it stays stable, how artifacts show up in motion, and whether players will actually notice.

In the end, the question is really if it looks as good as it can, and whether it enables something you couldn’t do before.

### Setting expectations

Neural graphics is still evolving, and different techniques are at very different stages.

NFRU is something you can pick up today and evaluate quickly. It’s low risk and easy to reason about.

NSSD is earlier and more involved. It requires time, iteration, and a willingness to work with a different kind of pipeline. But it also points to where things are heading—especially for teams interested in pushing visual quality on mobile.

If there’s one takeaway, it’s this:

Neural graphics creates the most value when it’s used intentionally—either to save performance where it matters, or to unlock things that weren’t previously feasible.

### Fallbacks and scalability

Unlike many traditional rendering features, the runtime cost of neural graphics techniques is generally more stable across content. The cost of running NFRU or NSSD itself does not scale heavily with scene complexity, number of lights, or material count in the way traditional rendering passes often do.

With that said, one important thing to think about early is what happens on devices that don’t support neural technology.

NFRU does not currently have a direct shader-based fallback equivalent. If a device can’t support NFRU, the recommendation is generally to scale the game in more traditional ways, for example by lowering the resolution. NFRU then becomes a way to enhance that baseline, rather than a hard dependency

NSSD is different. At the moment, there isn’t really a direct fallback path for what it enables. In practice, this means that if you build content around NSSD, you should expect to support a separate rendering path for devices that can’t run it. That’s one of the reasons we position NSSD differently throughout this playbook. It’s a deeper rendering investment intended for teams want to get ahead by experimenting with new features.

This is also one of the reasons we recommend evaluating these techniques early in development. Understanding the fallback story helps avoid building content that becomes difficult to scale across different device tiers later on.

## Is my game a good candidate?

One of the biggest takeaways from working on Neural Dawn and light-focused environments is that it comes down to the kind of game you’re building.

A good fit for neural graphics, especially when paired with MegaLights, tends to be about how your scenes are structured and how much you rely on lighting to carry the visual experience. The guidance is also generally aligned with what works for ray-tracing.

The setups that worked best for us were fairly contained, interior environments. Small to mid-sized spaces where you can control what’s on screen and how light behaves. That’s a big reason why much of Neural Dawn takes place in enclosed environments. It gives you more control, and it makes it easier to lean into dynamic lighting without things breaking down.

Those kinds of scenes are also where MegaLights really shines. You can place a lot of smaller dynamic lights, play with contrast, and build atmosphere in a way that would normally be too expensive. Moving from darkness into light, scene by scene, became a core part of how we structured the experience. Instead of relying on baked lighting, which can take a long time to generate and doesn’t adapt at runtime, we could keep things dynamic and iterate much faster.

### Where things get harder

Where things got harder was when we moved outside of those controlled environments. Large outdoor scenes were more challenging. You lose that tight control over lighting, and things like sunlight become harder to handle. Directional lights in particular require a lot of tuning to look right, and that quickly becomes a time sink. It’s not that these scenes are impossible, but they’re not where you get the most value today.

We also ran into issues with certain types of content that are already tricky for ray tracing. Foliage is a good example. Lots of small, thin, semi-transparent elements—like grass or leaves—are difficult to handle cleanly. In our case, we ended up being quite intentional about what we included. Similarly, heavy use of world position offset, especially with lots of instances, needs to be kept in check.

There are also some visual edge cases that are worth calling out. We saw ghosting in certain situations, like decals (for example, moss), although that’s not unique to this approach—it’s something you see with most temporal denoisers and upscalers. With NSSD specifically, we’ve seen issues like flickering (sometimes showing up as black dots), instability when the character is moving quickly over detailed surfaces, and subtle changes in fine detail that can make surfaces or silhouettes look like they’re shifting across frames.

VFX can also be tricky. Bright, fast-moving effects—especially sprite-based ones—can end up looking blurrier than expected. This is an area we’ve been actively working on improving, but it’s something to be aware of when evaluating your own content.

On the NFRU side, the main thing to keep in mind is that you’re still rendering at your base frame rate. If your game is running at 30 FPS and you’re generating intermediate frames, there’s still an inherent delay in the system. For most content that’s fine, but for something like a fast-paced racing game, that tradeoff might be more noticeable.

What stood out most from an art direction point of view was how much freedom this approach gives you when it works. Being able to rely on dynamic lighting—really dynamic lighting—and see it respond in real time was a big shift. It changes how you think about building scenes.

### Conclusion

If you had to boil it down, a good candidate today looks something like this: 

_A game with controlled environments, where lighting plays a big role in the look and feel, and where you’re willing to trade some predictability for flexibility. If your game depends heavily on large open worlds, dense foliage, or very fast, high-precision visuals, you’ll likely run into more friction. That doesn’t mean those cases won’t be supported—it just means they’re not where this approach is the strongest today._

It’s also worth saying that none of this is static. These are the first real attempts at bringing ray-traced lighting and fully dynamic scenes to mobile in a practical way. There isn’t a long history of best practices yet, and part of the work right now is figuring out what those should be. That’s also what makes it interesting.

We’re learning as we go, alongside the teams building with this tech. What works well today will keep improving, and some of the rough edges we see now are already being addressed. It really does feel like the start of something new for mobile graphics—and we’re excited to keep pushing it forward.
