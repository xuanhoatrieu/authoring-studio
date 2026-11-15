# Images and layout

Plan illustrations alongside topics. Every substantive topic or method in the
tourism profile has a suitable visual; a multi-step method may need several.
Do not use an arbitrary image quota or decorative fillers to satisfy coverage.

## Asset workflow

1. Read the relevant passage, identify what the image must show, and select the
   visual type before writing a prompt. Use [visual briefs and prompts](image-prompts.md).
2. For documentary examples, prefer verified photographs of the actual subject
   or actual screenshots. Check subject, place, relevant date, rights and resolution.
3. Save permitted assets in the book's `image/` directory with a semantic ID.
   Never bypass a provider's download/display restriction. If unavailable, record
   the gap instead of silently using a thumbnail or hotlink as a local asset.
4. Concept illustrations and cover images may be designed proactively; they do
   not require an unsuccessful stock-photo search first. Use image-generation
   tooling for raster creation/editing. Draw processes and data plots with tools
   that preserve exact structure, labels and values. Photorealistic style is a
   visual treatment, not documentary evidence of a real place, practice or result.
5. Keep the original provenance and mark `origin` internally: existing, screenshot,
   generated, diagram, chart or pending. Name the content directly in captions,
   following the shared rules below. Identify generated origin in an appropriate
   credits note or nearby explanation when needed to avoid documentary confusion;
   never call an invented scene a photograph of a real event. Do not automatically
   label each caption “Minh họa” or “hình ảnh thật”.
6. Inspect the saved image and its relation to the text. Missing rights, unclear
   resolution or an unverified subject remains unresolved in the working record.

## Choose a visual that explains the content

Show the objects, actions, relationships or differences the reader needs to
understand. Do not default to a repeated grid of rounded boxes containing prose.
Shortening the text in those boxes alone does not make a useful illustration.

- People, activities and experiences: use suitable photos or generated scenes
  in the book's chosen style; the tourism profile favours photorealistic scenes.
- Operations: show the relevant action in a sequence; software instructions use
  actual screenshots with concise annotations, not invented interface controls.
- Processes: show the flow and connections; use arrows only for an actual direction
  or sequence, not to imply unsupported stages or a maturity scale.
- Relationships: use a linked or nested diagram suited to the relationship.
- Places and landscapes: use an appropriate photograph.
- Comparisons: use aligned visual examples or a table; priorities may use a matrix.
- Data: use a chart only when traceable values support it.
- Covers: represent the book/chapter topic and reserve space for separately typeset
  titles. Follow [book structure](book-structure.md) for captionless cover treatment.

For a topic distinguishing digitizing information, using digital tools and changing
work organization, show a leaflet being saved on a phone, a booking entered in a
spreadsheet, and staff sharing one schedule. Use short labels instead of three
paragraphs in boxes. A concise caption could be “Hình 1.7. Số hóa thông tin, sử dụng
công cụ số và đổi mới cách tổ chức công việc.” Do not add a banner such as “không
phải thang chứng nhận” when the visual does not present a certification scale.

Before accepting an image, ask what the reader can see more clearly than in the
paragraph alone. Revise a visual that merely repeats prose or fills an image quota.
Inspect the whole set for repetitive layouts and each image at its intended size.
Check the teaching point itself, not just aesthetic quality: a scene of people
talking does not by itself show shared data, a handoff or assigned responsibility.
For invisible processes, combine a scene with a concise diagram or use a diagram
alone. Make the relevant common record, actors, connections or change visible;
do not rely on the caption to assert relationships the image fails to show.

## Caption, source and accessibility

Every content figure has a caption directly below it. Book and chapter cover images
have no caption or figure number in the tourism profile; retain alt text, semantic
IDs and provenance, and identify their credits by cover/chapter title at the end.
Author content captions once in Markdown,
with `<!-- caption: fig-id -->` immediately before the caption paragraph.
For all books, use the figure number and a short, specific content name. In
Vietnamese the pattern is “Hình x.x. Nội dung của hình.” Use the book's numbering
scheme and equivalent figure label in other languages. Remove introductory
“Minh họa”, “Hình minh họa” and redundant “Ví dụ” from captions; name the activity,
relationship, object or result directly. Add the external creator's name when
applicable. For example: “Hình 1.5. Vùng chè tại
Thái Nguyên, Bacthai20”. Include dates only when they matter to understanding the
image. Do not append a paragraph explaining the topic or repeating the body text.

Review the passage, all visible words inside the image, and its caption as one
editorial unit. Check the actual image, not just alt text, a prompt or caption
metadata. Remove decorative qualifiers inside images too: “Thông điệp minh họa”
can become “Thông điệp”; “Một bộ hồ sơ minh họa” can become “Hồ sơ và công việc
ưu tiên”. Keep short labels that explain parts and relationships; move long
instructions and applicability conditions into the nearby prose when they need
not be visible in the diagram. Preserve meaningful technical uses of these words.
If words are baked into pixels, revise the editable source or regenerate/edit the
asset when authorized; a caption-only edit does not resolve the image-text issue.

Identify hypothetical situations and invented quantities once in the local
introduction rather than repeating the warning in the image title, caption and
body. Keep the identification with the asset when it is intended to circulate
independently or would otherwise mislead. Do not present invented prices or
outcomes as observed data merely to shorten a caption.

Original figures, tables, diagrams and forms created for the user need no source
line saying “tác giả biên soạn”, “tác giả đề xuất” or equivalent self-credit. This
also applies to work produced with the skill. If the content adapts external
research, a model or data, retain that source citation without the self-credit.
Being newly drawn does not make externally sourced content original research.

Preserve asset provenance, source links, license and processing history in the
image records. Keep necessary reader-facing third-party credits and license
information in a concise end-of-book image credits section mapped to stable figure
IDs and rendered figure numbers, where the applicable license permits this placement.
Do not delete required attribution when shortening captions or leave it only in
internal metadata. Retain a local credit if the asset's terms require it.

Routine notes such as “giữ nguyên tệp tải về”, “không chỉnh thêm”, download dates
and crop history belong in the asset record, except for any change notice required
in the published credit. Avoid unsupported claims directly instead of adding
“ảnh không xác nhận…” to ordinary landscape captions. Preserve meaningful limits
in the relevant body text, and identify an illustration when needed to avoid
mistaking generated material for documentary evidence.

Include concise alt text describing meaningful visual information rather than
copying the caption or the credit. The image index references the caption marker
and exact section ID; do not duplicate authored captions there.

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

For every paginated book, keep a short lead-in with its figure/table when feasible.
Keep a short table that fits on a page intact rather than splitting it simply to
fill the preceding page. Long tables may continue with repeated headers and a
clear continuation label. Rebalance nearby content without changing reading order
or shrinking agreed type to solve pagination. Check both sides of each affected
page break; grouping a whole long section can create excessive blank space.

Check print legibility, adequate contrast, visible Vietnamese accents and screenshot
text. Charts require traceable data. Do not fabricate values to fill a graph.

## Confirmed typography for the tourism profile

Use A4 portrait, left margin 3 cm and top/right/bottom margins 2 cm; the text area
is 16 cm wide. Body text is Times New Roman 13 pt, justified, with line spacing
1.3, paragraph spacing 0 pt before and 4 pt after. Chapter and section headings
are left-aligned. Figure captions are 12 pt and centred; table titles remain
centred. These are confirmed settings for `rural-tourism-vi`, not requirements to
impose on unrelated books. Read the current book's decisions before applying them.

Apply these settings to requested previews as well as exports, using the book's
profile as the source of layout values. A responsive screen view may reflow for
readability, but its print view must use the agreed paper, margins and typography.
For HTML, provide print-specific page settings, hide navigation in print, and
check pagination rather than treating a 210 mm-wide scrolling container as an A4
layout. Keep captions with images and headings with following content; avoid
clipping, overflow and unreadably small labels. Inspect the actual rendered result
before claiming that its format is correct. See [quality](quality.md) for handoff.
The profile footer has the exact text “@ TS.Triệu Xuân Hoà” on the left and an
automatic page number on the right. See [book structure](book-structure.md) for
pagination, cover pages and format-specific rendering requirements.

## Table conventions for the agreed profile

Table title is centred, and every cell of the first/header row is centred horizontally
and vertically. This does NOT apply to chapter or section headings.
Body numeric columns are centred; body text columns are left-aligned horizontally
and vertically centred. Tables use single line spacing and 0 pt before/after each
paragraph. Repeat the header on continued tables when a renderer supports it; allow
rows to grow and do not clip content. Rendering and visual inspection remain required
before claiming the formatting is achieved.
