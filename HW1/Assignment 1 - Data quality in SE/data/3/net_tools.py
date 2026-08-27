"""Reachability checks exposed to the on-call dashboard."""
import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)

DEFAULT_COUNT = 3
DEFAULT_TIMEOUT = 5


def parse_rtt(output):
    """Pull the average round-trip time out of ping's summary line."""
    for line in output.splitlines():
        if "avg" in line and "/" in line:
            stats = line.split("=")[-1].strip().split("/")
            if len(stats) >= 2:
                return float(stats[1])
    return None


def ping(host, count=DEFAULT_COUNT):
    command = "ping -c " + str(count) + " -W " + str(DEFAULT_TIMEOUT) + " " + host
    try:
        output = subprocess.check_output(command, shell=True, text=True)
    except subprocess.CalledProcessError as exc:
        return {"host": host, "reachable": False, "detail": exc.output}
    return {"host": host, "reachable": True, "rtt_ms": parse_rtt(output)}


@app.route("/diagnostics/ping")
def diagnostics_ping():
    host = request.args.get("host", "")
    if not host:
        return jsonify(error="missing host"), 400

    count = int(request.args.get("count", DEFAULT_COUNT))
    return jsonify(ping(host, count))


@app.route("/diagnostics/routes")
def diagnostics_routes():
    table = subprocess.run(["netstat", "-rn"], capture_output=True, text=True)
    return jsonify(routes=table.stdout.splitlines()[:40])


if __name__ == "__main__":
    app.run(port=8084)
