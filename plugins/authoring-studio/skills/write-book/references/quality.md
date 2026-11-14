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
do not mutate the book just because a newer plugin exists. Version 0.1.0 has no schema
migration or automatic updater. It validates schema 1 and reports unsupported versions.

The helpers require Python 3.10+, PyYAML and jsonschema. Use an environment already
provided by the host or an explicitly provisioned virtual environment. Do not install
packages into the user's global Python as a hidden side effect of writing.
Read-only checks and Markdown editing do not require Quarto or a document renderer.

For later export, check Times New Roman on the export machine. Do not silently
substitute or bundle proprietary font files. Inspect actual pages, table headers,
captions and image placement. Version 0.1.0 does not claim export equivalence.

Maintain the behavioural regression scenarios shipped in the repository. Automated
source tests check integrity; model behaviour scenarios require an actual controlled
run and its recorded result. Do not report an unrun scenario as passed.
