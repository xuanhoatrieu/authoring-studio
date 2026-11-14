# Images and layout

Plan illustrations alongside topics. Every substantive topic or method in the
tourism profile has a suitable visual; a multi-step method may need several.
Do not use an arbitrary image quota or decorative fillers to satisfy coverage.

## Asset workflow

1. Specify what the image must teach and the details it must show.
2. Prefer appropriate existing photographs or screenshots. Check the source page,
   subject, place, date where relevant, rights and actual resolution before use.
3. Save permitted assets in the book's `image/` directory with a semantic ID.
   Never bypass a provider's download/display restriction. If unavailable, record
   the gap instead of silently using a thumbnail or hotlink as a local asset.
4. Create an illustration only when suitable material is missing. Authored process
   diagrams and data plots may be produced directly. Use image-generation tooling
   for raster creation or editing when available. Never manufacture documentary
   evidence of a real place, practice or result.
5. Keep the original provenance and mark `origin` internally: existing, screenshot,
   generated, diagram, chart or pending. Generated images may be captioned as
   illustrations when needed to avoid confusion; never call them photographs of a
   real event. The phrase “hình ảnh thật” is unnecessary in reader-facing prose.
6. Inspect the saved image and its relation to the text. Missing rights, unclear
   resolution or an unverified subject remains unresolved in the working record.

## Caption, source and accessibility

Every image has a caption directly below it. Author captions once in Markdown,
with `<!-- caption: fig-id -->` immediately before the caption paragraph.
Give a short description and the detail that matters. Put attribution in the
following source line. Include concise alt text distinct from the caption.
Image index references the caption marker and exact section ID.

## Layout vocabulary

- `text-left-image-right`: short explanation with an image on the right.
- `image-left-text-right`: image first, analysis on the right.
- `full-width-below` or `full-width-above`: width of the text area, not paper bleed.
- `pair`: two related images with labels and a shared or separate clear caption.
- `steps`: ordered sequence, with step numbers matching the instructions.

For the tourism A4 profile the text width is 16 cm. A provisional side-by-side
split is 9 cm text + 0.5 cm gap + 6.5 cm image. Use full width when detail or text
length would make side columns difficult to read. Preserve image proportions.
Keep image and caption together; place them near the explaining paragraph. Avoid
putting long explanations into tables solely to force a layout.

Check print legibility, adequate contrast, visible Vietnamese accents and screenshot
text. Charts require traceable data. Do not fabricate values to fill a graph.

## Table conventions for the agreed profile

Table title is centred, and every cell of the first/header row is centred horizontally
and vertically. This does NOT apply to chapter or section headings.
Body numeric columns are centred; body text columns are left-aligned horizontally
and vertically centred. Tables use single line spacing and 0 pt before/after each
paragraph. Repeat the header on continued tables when a renderer supports it; allow
rows to grow and do not clip content. Rendering and visual inspection remain required
before claiming the formatting is achieved.
