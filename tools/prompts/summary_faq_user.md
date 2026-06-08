Generate an AI-assisted summary paragraph and FAQ section for this Arm Learning Path.

Use the Learning Path title, description, audience, objectives, prerequisites, tags, platform metadata, step excerpts, and supplied authoring guidance to produce useful draft content for a developer following the path.

Assume these rules while writing:
- Use only the Learning Path context below. Do not add facts, tools, commands, prerequisites, performance claims, compatibility claims, or outcomes that are not present.
- Write as an Arm Learning Path author by following the supplied guidance from `.github/copilot-instructions.md` and `content/learning-paths/cross-platform/_example-learning-path/`.
- Keep the content useful for human review. The draft should be specific enough to evaluate, but not so detailed that it replaces the Learning Path steps.
- If the context is thin, be honest and stay high-level rather than filling gaps.
- Match the complexity of the Learning Path. Introductory paths should stay approachable; advanced paths can use more precise technical language from the context.

Summary guidance:
- Say what the learner will build, configure, measure, deploy, or understand.
- Mention Arm technologies, tools, operating systems, and cloud platforms only when they appear in the context.
- If prerequisites are absent, say that no explicit prerequisites are listed.
- Do not make the summary sound promotional; make it sound like a useful technical overview.

FAQ guidance:
- Write questions that a real reader would ask while moving through the Learning Path steps, not only questions they would ask before starting.
- Prioritize questions that help a learner complete the work: required setup, tool or platform choices, command outcomes, what gets created, how to validate success, what skills or access are assumed, and what decisions the learner must make during the procedure.
- Include before-you-start questions only when they are genuinely useful for preventing a blocker, such as missing prerequisites, permissions, hardware, cloud account access, or required prior knowledge.
- Avoid generic questions like "What will I learn?", "Who is this for?", or "What is this Learning Path about?" when the context supports more practical workflow questions.
- Good FAQ questions should feel like something a learner might ask with the Learning Path open in another tab.
- Avoid far-fetched edge cases. Stay close to common developer concerns raised by the actual steps and metadata.
- Answer each question directly using only information from the context.

Learning Path context:

{{ learning_path_context }}
