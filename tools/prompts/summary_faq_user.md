Generate an AI-assisted summary paragraph and FAQ section for this Arm Learning Path.

Use the Learning Path title, description, audience, objectives, prerequisites, tags, platform metadata, step excerpts, and supplied authoring guidance to understand the learner journey and produce useful draft content for a developer following the path.

Important: the generated block appears on the same page as the existing Learning Path metadata and introduction. Do not repeat information that the learner can already see in existing fields or sections, especially prerequisites, objectives, audience, tags, descriptions, "What will you learn?", installation/setup lists, or other front-matter-driven content.

Assume these rules while writing:
- Use only the Learning Path context below. Do not add facts, tools, commands, prerequisites, performance claims, compatibility claims, or outcomes that are not present.
- Write as an Arm Learning Path author by following the supplied guidance from `.github/copilot-instructions.md` and `content/learning-paths/cross-platform/_example-learning-path/`.
- Keep the content useful for human review. The draft should be specific enough to evaluate, but not so detailed that it replaces the Learning Path steps.
- If the context is thin, be honest and stay high-level rather than filling gaps.
- Match the complexity of the Learning Path. Introductory paths should stay approachable; advanced paths can use more precise technical language from the context.
- Treat prerequisites and objectives as background context, not content to rewrite. Only mention them if doing so helps answer a specific step-level concern that is not already obvious from the page.

Summary guidance:
- Write the summary as an Arm Learning Path overview, not from the learner's first-person point of view.
- Never use first-person wording in the summary, including "I", "we", "my", "our", or "let's".
- Use "you" sparingly in the summary. Prefer neutral phrasing such as "This Learning Path shows...", "The path guides learners through...", or "Learners configure..." unless second person is clearly more direct.
- Say what learners build, configure, measure, deploy, debug, validate, or compare as they work through the steps.
- Mention Arm technologies, tools, operating systems, and cloud platforms only when they appear in the context.
- Avoid restating prerequisites, audience, objectives, or title text. The summary should add orientation around the workflow, not duplicate the surrounding page content.
- If prerequisites are absent, do not comment on that absence unless the steps make a setup dependency unclear.
- Do not make the summary sound promotional; make it sound like a useful technical overview.

FAQ guidance:
- Write questions that a real reader would ask while moving through the Learning Path steps or checking their work after a step.
- Prioritize questions that help a learner complete the work: tool or platform choices, command outcomes, what gets created, how to validate success, which file or service to inspect, what decision to make during the procedure, and what to check before continuing.
- Do not use the FAQ to repeat prerequisites. Avoid questions like "What prerequisites do I need?", "Do I need prior experience?", or "What should I install first?" unless the answer gives specific step-level guidance that is not already covered by the prerequisites or install sections.
- Include before-you-start questions only when they are genuinely useful for preventing a blocker that is not already clearly covered elsewhere on the page.
- Avoid generic questions like "What will I learn?", "Who is this for?", or "What is this Learning Path about?" when the context supports more practical workflow questions.
- Good FAQ questions should feel like something a learner might ask with the Learning Path open in another tab.
- Good FAQ answers should point the learner toward the next useful check or decision without repeating entire paragraphs from the Learning Path.
- Avoid far-fetched edge cases. Stay close to common developer concerns raised by the actual steps and metadata.
- Answer each question directly using only information from the context.

Learning Path context:

{{ learning_path_context }}
