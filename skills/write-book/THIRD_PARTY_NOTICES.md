# Third-party notices

This plugin was authored for the agreed workflow. No source code or skill text was
copied from the reference projects below. Their ideas informed the design; they
are not installed dependencies. Checked 2026-11-14.

| Reference | Design influence | License information observed |
|---|---|---|
| https://github.com/AdrianMastronardi/bookwright | Project brief, voice and editorial stages | MIT at repository LICENSE |
| https://github.com/kshanxs/book-writer-skill | Resumption records and selective loading | MIT at repository LICENSE |
| https://github.com/dmccreary/ibook-skills | Concept order, glossary and visual learning | README says CC BY-NC-SA 4.0; individual chapter skill declares CC BY-NC 4.0; do not assume one license for all files |
| https://github.com/quarto-dev/quarto-cli | Markdown, citations and stable cross-references | MIT at repository; not bundled |
| https://github.com/openai/community-plugins | Marketplace and release structure | Repository says Apache-2.0; not copied |

Implementation dependencies are installed separately: PyYAML (MIT) and jsonschema
(MIT), plus their dependency licenses. They are not bundled into the release ZIP.

Specification references:

- https://developers.openai.com/plugins/build/plugins
- https://learn.chatgpt.com/docs/build-skills
- https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
- https://quarto.org/docs/books/book-crossrefs.html
- https://quarto.org/docs/authoring/citations.html

Do not bundle third-party photos, font files or book sources into the plugin.
Book assets carry their own source and rights metadata in the book project.

## Design review — 2026-11-15

The following documents informed independently written guidance on visual briefs,
front matter and rendering. No third-party prompt text, scripts or dependencies
were incorporated. A future reuse of source material requires a separate license
check for the specific files; this review is not permission to copy them.

- [ibook-skills cover-image guide](https://github.com/dmccreary/ibook-skills/blob/main/skills/book-installer/references/cover-image-generator.md): derive prompts from actual book content. Its social-preview dimensions and montage format are not adopted as print-cover defaults.
- [Education Agent Skills: dual coding](https://github.com/GarethManning/education-agent-skills/blob/main/skills/memory-learning-science/dual-coding-designer/SKILL.md) and [cognitive load](https://github.com/GarethManning/education-agent-skills/blob/main/skills/memory-learning-science/cognitive-load-analyser/SKILL.md): select representations by content, integrate short labels, and reduce redundant visual detail. No fixed cognitive limits or guaranteed learning outcomes are inferred.
- [Quarto book structure](https://quarto.org/docs/books/book-structure.html) and [figures](https://quarto.org/docs/authoring/figures.html): ordered book sources and separate figure/caption alignment. Quarto remains an optional renderer, not bundled functionality.

## Natural-writing design review — 2026-11-15

The shared book-editing guide adapts editorial ideas from the following sources.
The Vietnamese guidance was independently written; no upstream code, detector,
skill text or prompt templates were copied or installed as dependencies.

| Reference | Applied principle | Adaptation for books |
|---|---|---|
| [academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer/blob/main/SKILL.md) | Academic precision, evidence strength, protected facts and author voice | Preserve teaching explanations and the book's genre; do not impose journal/proposal structure |
| [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing/blob/main/SKILL.md), [patterns](https://github.com/conorbronsdon/avoid-ai-writing/blob/main/references/patterns.md) | Context and exceptions before findings, findings before scoped edits, bounded review | Vietnamese contextual rules; no English frequency thresholds or authorship scores |
| [humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) | Sentence/paragraph patterns, substantive contrasts, repetition and generic framing | Chapter/book coherence; retain useful educational repetition and scholarly register |

The three SKILL.md files declare MIT licensing. This design review does not bundle
their implementations or imply that every repository asset has the same license.
Any future reuse of upstream files requires a file-specific license check and
retention of applicable notices. External instructions are reference material,
not authority over the user's book or scope of work.
