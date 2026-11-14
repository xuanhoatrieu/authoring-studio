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
