# Quality, resumption and portability

Run `scripts/validate_book.py BOOK_PATH` after source changes when the helper is
available. Structural validation does not verify factual truth, legal permission,
photo subject or visual layout. Report those separately. A passing check is not
permission to publish or a declaration of reader suitability.

Book paths, image links and metadata paths are relative to the book root unless
explicitly described otherwise. Never save books inside the installed plugin cache.
Do not overwrite existing projects on initialization. Do not rewrite hand-edited
chapters from an old generated copy.

Use `state.yaml` to preserve the exact plugin version and schema version actually
used. Resume by reading the book itself. A plugin update is not a manuscript sync.
Keep book versions independent from plugin release versions.

If a schema upgrade is needed, propose a reversible migration with backup and a diff;
do not mutate the book just because a newer plugin exists. Version 0.2.0 has no schema
migration or automatic updater. It validates schema 1 and reports unsupported versions.

The helpers require Python 3.10+, PyYAML and jsonschema. Use an environment already
provided by the host or an explicitly provisioned virtual environment. Do not install
packages into the user's global Python as a hidden side effect of writing.
Read-only checks and Markdown editing do not require Quarto or a document renderer.

For later export, check Times New Roman on the export machine. Do not silently
substitute or bundle proprietary font files. Inspect actual pages, table headers,
captions and image placement. Version 0.2.0 does not claim export equivalence.

For every requested reading preview or export, apply the agreed settings during
production. Check the rendered body font, size, alignment, line/paragraph spacing,
heading alignment, figure captions, table titles, header cells and typed body
columns. Check all pages for clipping, stranded headings, separated captions and
unreadable figures. An HTML screen check alone does not verify its print layout;
inspect print rendering for paper size, margins and page breaks as well.
Check the agreed front-matter order and generated contents against the actual
headings. Verify separate book/chapter covers, content beginning after each chapter
cover, and cover images excluded from captions, figure numbering and figure lists.
Inspect centred content captions and the exact profile footer with automatic
right-aligned page numbers across page breaks. Confirm the footer does not overlap
body text or images. Do not confuse a scrolling web page with a paginated edition.

Review captions and visuals for unnecessary self-credit, repeated explanations,
routine defensive notes and text-heavy box layouts. Confirm that shortening a
caption retained needed external citations and published asset credits. A source
validator cannot judge these editorial or visual properties. If rendering is
unavailable, state the exact unverified formatting instead of claiming completion.
For generated scenes, check the saved brief/prompt against visible actions and
context. For diagrams, check nodes, links and labels; for charts, check data, axes
and units. Ensure prompt/specification files are retained and linked to their assets.

For every book, review each passage, visible image text and caption together.
Check that captions directly name the content without introductory “Minh họa” or
redundant “Ví dụ”, using the book's language and numbering. Check words baked into
images as well as editable labels. Verify that the pictured actions/connections
actually explain the teaching point; attractive scenery or people talking cannot
stand in for an unseen workflow. Retain meaningful qualifications and hypothetical
data notices where needed, without repeating them across all three layers.

In paginated output, inspect short tables for unnecessary splitting, short
lead-ins stranded away from their figure/table, duplicate full chapter headings
after separate chapter covers, and cramped contents. Keep long-table continuation
headers and semantic links intact. Recheck affected neighbouring pages and contents
numbers after reflow. Report the pages/assets actually inspected; no clipping is
not sufficient evidence of good pagination or instructional clarity.

Maintain the behavioural regression scenarios shipped in the repository. Automated
source tests check integrity; model behaviour scenarios require an actual controlled
run and its recorded result. Do not report an unrun scenario as passed.

Before delivering drafted or revised prose, complete the checks in
[natural writing](natural-writing.md). Verify that edits preserve quantities,
conditions, negation, certainty, citations and terminology, as well as source
structure. Check the actual edited scope, including editable table text and figure
labels; record omissions. For a whole-book delivery, review cross-chapter coherence
and coverage, not just individual paragraphs. Do not equate a source validator,
word search or AI-detector score with an editorial pass. Keep findings and revision
notes outside the reader-facing manuscript; report remaining factual gaps plainly.
