# Visual briefs and image prompts

Use this guidance before generating illustrations or covers and before drawing
diagrams or charts. A discussion or prompt-only request stops at the requested
proposal; an authorized illustration task includes producing and checking the
image with available tools. Do not add a compulsory approval for every prompt.

## Design from the actual content

Read the relevant passage, audience, book style and neighbouring images. Establish
what the reader should notice and what the visual adds beyond the prose. Choose
the visual type before the tool or prompt: a scene for an activity, a flow for a
process, connected/nested elements for relationships, or a plot for numeric data.
Cover artwork should represent the scope of its book or chapter, not merely a
generic technology or landscape theme. Use a consistent visual style across the
book without repeating one composition for every topic.

Create a brief with:

- Purpose and source section: the idea or distinction to make visible.
- Observable evidence: what a reader must actually see to recognize that idea;
  for shared information or handoffs, specify the record, roles and connections.
- Subjects and actions: who does what, with which objects; required relationships.
- Setting: relevant place characteristics, time, clothing, tools and materials.
- Composition: focal point, viewpoint, foreground/background and visual hierarchy.
- Style: photography, technical illustration or another chosen treatment; colour,
  lighting and mood appropriate to the subject and adult readership.
- Use: content figure, book cover or chapter cover; intended size and aspect ratio,
  crop-safe area, and any space reserved for the separately typeset title.
- Constraints: exact details to preserve and specific errors or irrelevant details
  to avoid. Keep exclusions relevant rather than adding a generic long blacklist.

For the tourism profile, generated scenes use a photorealistic photographic style
by default: plausible actions, natural light, believable materials and everyday
settings. This default does not turn diagrams into photos or authorize presenting
an invented scene as a photographed event at a named establishment. Retain generated
origin in the asset record and distinguish illustration from documentary material
where the reader could otherwise be misled.

## Write an executable prompt

Translate abstract ideas into visible actions and relationships. “Professional,
high quality, digital transformation” alone is not a sufficient prompt. Specify
what is important in the frame, not a camera specification unrelated to the goal.
Keep explanatory paragraphs out of the generated image. Short labels, exact
interface text and book/chapter titles are better placed as editable text during
drawing or layout, with Vietnamese accents checked separately.

For example, a section about promoting visitor activities can use this scene:

> Photorealistic illustration for an adult rural-tourism handbook: at a Vietnamese
> tea garden, the operator photographs a guide showing visitors how to pick tea
> buds. Show the connection between the visitor activity and creating promotional
> material. Landscape 3:2, eye-level view, the phone in the foreground and the
> demonstration in the middle ground. Natural daylight, believable working clothes
> and gestures, uncluttered composition legible at 16 cm width. No embedded title,
> logos, information boxes or floating technology symbols.

This is an example of translating purpose into a scene, not a scene to reuse for
every book or every tourism chapter. Derive each actual prompt from its passage.

For a cover, specify a composition suited to the intended page, with quiet space
for the title. Generate the artwork separately and typeset the exact book/chapter
title afterwards. Do not use a social-media landscape size as a print-cover default
or require a collage of many concepts. For a long title, adjust line breaks and
artwork placement instead of shrinking it until unreadable.

## Draw diagrams and charts precisely

A diagram brief specifies nodes, groups, connectors, direction and exact short
labels. Use an editable vector or code-based drawing when precision matters. A
chart brief specifies its data source, variables, units, values, chart type, axes
and legend. Plot from that data; do not ask a generative scene model to invent a
chart, quantitative scale or screenshot. If values are missing, identify the gap
or choose a non-quantitative diagram instead of manufacturing a trend.

Place labels near the parts they explain, use colour to distinguish meaningful
groups and remove details that compete with the teaching point. Evaluate complexity
for the actual reader; do not apply a fixed element count or claim a learning
benefit merely because an image is present.

## Keep the design record and review the result

Save the final brief/prompt or drawing specification under
`image/prompts/<semantic-id>.md`, outside the plugin, and link it from the image
record using `prompt_file`. Include source section, intended size, chosen style,
reference assets and important revisions; record the actual generation tool when
known. Do not include account secrets. Preserve approved artwork when iterating.

Inspect the saved image and then its placement on the page. Check that required
actions and relationships are visible, the activity is plausible, hands/objects
and text are not malformed, labels remain legible at final size, and cropping
does not remove essential detail or the title area. Check diagrams against their
specified links and charts against their source data. A plausible, attractive
scene is insufficient if it does not reveal the intended distinction. Change the
representation or combine scene and diagram when the concept requires it; do not
force a photographic treatment onto abstract relationships.
Read the actual embedded words alongside the passage and caption using
[caption and layout rules](images-layout.md). Remove repeated titles, long
instructional banners and redundant “minh họa”/“ví dụ” labels, while keeping
necessary local identification of hypothetical data. If the result misses the
brief, correct the prompt or drawing specification before retrying. Save only a
reviewed result as reviewed; keep missing tools or unresolved defects explicit.
