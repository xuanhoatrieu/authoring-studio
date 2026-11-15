# Source format version 1

Use UTF-8. `book.yaml`, `state.yaml`, `terms.yaml`, `image-index.yaml`,
`table-index.yaml`, `evidence.yaml` and `references.yaml` live at the book root.
`chapters/` contains prose; `image/` contains acquired or generated assets.
`decisions.md` and `outline.md` contain decisions and structure, not duplicate prose.

Metadata file paths are relative to the book root. Markdown image paths are relative
to the containing Markdown file, so `chapters/a.md` uses `../image/example.jpg`.
Neither uses a machine-specific absolute path. Do not escape the book root.

## Stable IDs and citations

Headings: `## Tên mục {#sec-ten-muc}`. Image: `![Mô tả](../image/name.jpg){#fig-name}`.
Tables: `<!-- table: tbl-name -->` followed by `<!-- caption: tbl-name -->`,
the table title, then the Markdown table. Images have the analogous
`<!-- caption: fig-name -->` followed by the caption paragraph immediately below.
IDs are semantic, not mutable chapter numbers. Cite sources as `[@source-id]`.
Cross-refer with `@sec-name`, `@fig-name` and `@tbl-name`.

`image-index.yaml` maps each figure to `section`, `chapter_file`, `file`,
`caption_id`, `layout`, `status`, `origin`, `source_url`, `rights`, and `alt`.
A planned image may have a null file; validation reports the gap, not a completion.
Optional `role` is `content` (also the default when omitted), `book-cover`, or
`chapter-cover`. Covers require `caption_id: null` and `numbered: false`; retain
the normal image/section anchors and alt text but omit the caption marker. A
content figure still requires its caption; it cannot opt out using `numbered: false`.
Render covers as unnumbered artwork, outside the figure counter/list. Credit covers
by book/chapter title and cross-reference their section, not their figure ID.

For newly generated images or drawn diagrams/charts, save the final brief/prompt
or specification as `image/prompts/<semantic-id>.md` and set `prompt_file` to that
book-relative path. The validator checks provided prompt paths and files. These
fields extend schema 1 without requiring changes to existing content-figure records;
older plugin builds may not understand cover records. Do not automatically migrate
existing books or change their approval state.
`table-index.yaml` maps each table to its section, chapter file, caption marker,
header row count and body-column types (`text` or `number`). Layout policy is in
`book.yaml`. No renderer is bundled; requested previews and exports must apply
these values through an available renderer and undergo visual inspection.

Keep source URLs, rights and processing history in image records. Where needed,
author an end-of-book image credits section in Markdown linked to stable figure
IDs; render the corresponding figure numbers for content figures and cover titles
for covers. Apply the caption and
credit rules in [images and layout](images-layout.md). Original work for the user
does not require a self-credit source line.

In `references.yaml`, use `references: []` or CSL-compatible entries with `id`,
`type`, `title`, `author`, `issued`, `URL` and other needed CSL fields. Use one
whole-book bibliography. Store locators and checks in `evidence.yaml` rather than
inventing citation processor fields.

## Initialization and validation

From the plugin root, using a Python environment with the declared dependencies:

```sh
python scripts/init_book.py /path/outside/plugin/new-book --title "Tên sách" --dry-run
python scripts/init_book.py /path/outside/plugin/new-book --title "Tên sách"
python scripts/validate_book.py /path/outside/plugin/new-book
```

Use `--profile rural-tourism-vi` only for this agreed tourism book. Initializing
creates empty chapter/image directories and records, not a chapter draft. It refuses
existing destinations and any destination within this plugin or its source repository.
Validation is read-only; `--strict` treats unresolved warnings as failures.

## Updating

Edit the existing Markdown, never a compiled copy. Preserve IDs and the user's edits.
If content moves, update index paths, section relationships and evidence references.
Record completed work and remaining gaps in `state.yaml`. Do not duplicate complete
captions, source entries or chapter text into progress records.
Keep the book's reading order in `outline.md`, including front matter and chapter
opening pages under `chapters/`. A cover stored separately is not an extra chapter.
On a requested export, derive the table of contents from the actual headings/order
and let the renderer compute page numbers. Footer text and numbering policy live
in `book.yaml`, not in repeated source paragraphs.
