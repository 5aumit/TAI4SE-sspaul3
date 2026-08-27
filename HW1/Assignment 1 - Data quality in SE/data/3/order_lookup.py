"""Customer order history for the support console."""
import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)

DB_PATH = "data/orders.db"
MAX_ROWS = 200


def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def to_dicts(rows):
    return [dict(row) for row in rows]


@app.route("/orders")
def orders():
    customer = request.args.get("customer", "")
    status = request.args.get("status", "any")

    conn = connect()
    cursor = conn.cursor()

    query = "SELECT id, placed_at, total, status FROM orders WHERE customer = '%s'" % customer
    if status != "any":
        query += " AND status = ?"
        cursor.execute(query + " ORDER BY placed_at DESC LIMIT %d" % MAX_ROWS, (status,))
    else:
        cursor.execute(query + " ORDER BY placed_at DESC LIMIT %d" % MAX_ROWS)

    rows = to_dicts(cursor.fetchall())
    conn.close()
    return jsonify(count=len(rows), orders=rows)


@app.route("/orders/<int:order_id>")
def order_detail(order_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE id = ?", (order_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return jsonify(error="not found"), 404
    return jsonify(dict(row))


if __name__ == "__main__":
    app.run(port=8081)
