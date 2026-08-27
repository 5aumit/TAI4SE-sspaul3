"""Search endpoint for the docs site."""
import re

from flask import Flask, request

from index import DocumentIndex

app = Flask(__name__)
index = DocumentIndex.load("index/docs.idx")

PAGE_SIZE = 20
SNIPPET_CHARS = 180


def snippet(body, term):
    """Return the text around the first occurrence of the term."""
    position = body.lower().find(term.lower())
    if position < 0:
        return body[:SNIPPET_CHARS]
    start = max(0, position - SNIPPET_CHARS // 2)
    return body[start:start + SNIPPET_CHARS]


def normalise(term):
    return re.sub(r"\s+", " ", term).strip()


@app.route("/search")
def search():
    term = normalise(request.args.get("q", ""))
    page = int(request.args.get("page", 1))

    if not term:
        return "<p>Enter a search term.</p>"

    hits = index.query(term, offset=(page - 1) * PAGE_SIZE, limit=PAGE_SIZE)

    rows = []
    for hit in hits:
        rows.append(
            "<li><a href='/doc/%s'>%s</a><p>%s</p></li>"
            % (hit.doc_id, hit.title, snippet(hit.body, term))
        )

    return (
        "<h2>%d results for %s</h2><ul>%s</ul>"
        % (len(hits), term, "".join(rows))
    )


@app.route("/healthz")
def healthz():
    return {"status": "ok", "documents": index.size()}


if __name__ == "__main__":
    app.run(port=8080)
