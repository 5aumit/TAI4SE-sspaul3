"""Restore a wizard's in-progress state between page loads."""
import base64
import pickle

from flask import Flask, jsonify, request

app = Flask(__name__)

STEPS = ("account", "billing", "review")


def blank_state():
    return {"step": STEPS[0], "answers": {}, "version": 2}


def summarise(state):
    answered = len(state.get("answers", {}))
    return {"step": state.get("step"), "answered": answered}


@app.route("/wizard/resume", methods=["POST"])
def resume():
    blob = request.form.get("state")
    if not blob:
        return jsonify(summarise(blank_state()))

    raw = base64.b64decode(blob)
    state = pickle.loads(raw)

    if state.get("version") != 2:
        return jsonify(error="stale session"), 409
    return jsonify(summarise(state))


@app.route("/wizard/save", methods=["POST"])
def save():
    state = blank_state()
    state["answers"] = request.get_json(silent=True) or {}
    state["step"] = request.form.get("step", STEPS[0])
    blob = base64.b64encode(pickle.dumps(state)).decode("ascii")
    return jsonify(state=blob)


if __name__ == "__main__":
    app.run(port=8083)
