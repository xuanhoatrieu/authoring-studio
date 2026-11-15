# Front matter, covers and page furniture

Use the current book's decisions. The confirmed sequence and footer below belong to the
named `rural-tourism-vi` profile; do not impose its author identity or structure
on unrelated books. Updating the plugin does not rewrite an existing manuscript.

## Shared opening-page and contents rules

Apply these to every book using separate chapter covers. Once the opening page
shows the chapter number and full title, begin the next page with the first section;
do not print the full chapter heading a second time. Preserve semantic chapter
structure, IDs and cross-references in the source; suppress duplicate display in
the renderer rather than deleting the chapter identity. A book without separate
chapter covers retains its ordinary chapter heading. An explicit book-specific
design can override this default.

Keep one contents entry per chapter with the correct destination. Let a long
contents list span as many pages as needed at readable, agreed type and spacing;
do not compress it to one page by shrinking text or crowding lines. Keep wrapped
titles, leader dots and page numbers readable and aligned. Recalculate destinations
and page numbers after pagination changes and inspect the rendered contents.

## Confirmed tourism sequence

1. **Trang bìa:** a separate page with the exact book title in large, prominent
   type and one representative image.
2. **Lời nói đầu:** why the book was prepared, the practical need and its direction.
   Avoid repeating the objectives and chapter summaries of the general introduction.
3. **Mục lục:** generated from the actual headings and reading order. Update page
   numbers after layout, with clickable destinations in a screen edition.
4. **Giới thiệu chung:** the book's objectives, followed by its structure: the actual
   name of each chapter and a concise summary of that chapter's main ideas. Reuse
   the book's current outline; never infer a chapter count from an older profile.
   Keep audience, scope and usage guidance here when needed, without duplicating
   the preface or automatically expanding the front matter.
5. **Bìa chương, then chapter content:** each chapter starts with a separate cover
   page containing its number, exact title and one representative image. Begin
   the content on the following page. Repeat for each chapter.

Chapter covers are opening pages, not chapter-level learning objectives or prose
introductions. Preserve the existing decision to go straight into the knowledge
and methods after the cover. Do not duplicate a chapter's entry in the contents
because its opening page is stored separately. Bibliography and image credits
remain at the end of the whole book.

## Cover design and source representation

Keep a consistent cover family while changing the artwork to match each topic.
Generate or source the artwork separately, then typeset titles as editable text;
check Vietnamese diacritics, line breaks and contrast. Leave enough room for long
titles. Ordinary section headings retain the profile's left alignment; the title
composition on a cover may be designed for that page, not propagated to the body.

Book and chapter cover images have **no caption and no figure number**. They do
not consume numbers in the content-figure sequence or appear in the list of figures.
Keep alt text and asset provenance. At the end of the book, identify any required
credit as “Ảnh bìa sách” or “Ảnh bìa chương …”, with the chapter title as needed.

Keep all front matter and chapter cover Markdown under `chapters/` so it is included
in source validation. A book cover may use `sec-bia-sach` and `fig-bia-sach`; chapter
covers use stable semantic section/image IDs based on the chapter topic. Declare
`role: book-cover` or `role: chapter-cover`, `caption_id: null`, and `numbered: false`
in `image-index.yaml`. Omitted role means an ordinary content figure. Do not insert
a caption marker for a cover. See [source format](source-format.md) for details.
These IDs are internal links, not instructions to print a figure label. Translate
cover images to unnumbered artwork in the renderer; cross-reference the cover's
section rather than using a numbered figure reference.

## Footer and pagination

The profile footer contains the exact literal text **@ TS.Triệu Xuân Hoà** on the
left and an automatically generated page number on the right, within the page's
text width. The `@` is literal text, not a citation or a copyright symbol. Use the
renderer footer/page-number feature rather than typing repeated footers into the
manuscript or hard-coding page numbers into images.

The implementation default is continuous Arabic page numbers starting at 1, with
the footer on all paginated pages, including cover pages. The user specified the
footer text and right-hand page number, not a separate numbering scheme or cover
exception; preserve a later book-specific decision if one is provided. Keep the
footer clear of body text and captions. In a continuous scrolling screen edition,
do not fabricate page numbers; use a paginated reading/print view to check them.

## Render and verify

Quarto is an optional publishing route, not a required dependency or a replacement
for the user's source files. When selected, adapt the existing Markdown/YAML into
its structure without an automatic manuscript migration. Configure the target
formats explicitly: book title and cover, the agreed preface/contents/introduction
order, chapter opening page breaks, numbering and footer. An HTML home-page cover
does not by itself create the requested print cover pages.

In Quarto, image alignment and caption alignment are separate: explicitly centre
captions in each output format. In any renderer, verify the actual contents links
and page numbers, the cover-to-content page breaks, captionless unnumbered cover
artwork, centred body captions, and footer alignment on first, middle and last pages.
Check each output independently; a correct HTML preview does not prove a PDF or
Word file is formatted correctly. Do not claim that a renderer is bundled or that
the final book has been visually checked merely because this guidance exists.
