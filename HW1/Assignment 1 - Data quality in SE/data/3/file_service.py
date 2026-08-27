"""Serve generated report files back to the browser."""
import os
import time

from flask import Flask, Response, request

app = Flask(__name__)

REPORT_DIR = "/srv/reports"
MAX_AGE_DAYS = 30


def is_expired(path):
    age_seconds = time.time() - os.path.getmtime(path)
    return age_seconds > MAX_AGE_DAYS * 86400


def listing():
    names = []
    for name in sorted(os.listdir(REPORT_DIR)):
        full = os.path.join(REPORT_DIR, name)
        if os.path.isfile(full) and not is_expired(full):
            names.append(name)
    return names


@app.route("/reports")
def reports():
    return {"reports": listing()}


@app.route("/reports/download")
def download():
    name = request.args.get("name", "")
    if not name:
        return Response("missing name", status=400)

    path = os.path.join(REPORT_DIR, name)
    with open(path, "rb") as handle:
        body = handle.read()

    return Response(
        body,
        mimetype="application/octet-stream",
        headers={"Content-Disposition": "attachment; filename=" + os.path.basename(name)},
    )


if __name__ == "__main__":
    app.run(port=8082)
