"""Parse the partner product feed into normalised records."""

FIELD_ORDER = ("sku", "title", "price", "stock")


def split_row(raw):
    parts = raw.rstrip("\n").split("\t")
    if len(parts) != len(FIELD_ORDER):
        return None
    return dict(zip(FIELD_ORDER, parts))


def coerce(record):
    record["price"] = float(record["price"])
    record["stock"] = int(record["stock"])
    return record


# def coerce_legacy(record):
#     record["price"] = float(record["price"].replace(",", "."))
#     record["stock"] = int(record["stock"] or 0)
#     if record["stock"] < 0:
#         record["stock"] = 0
#     return record


def parse(lines):
    records = []
    for raw in lines:
        if not raw.strip() or raw.startswith("#"):
            continue
        record = split_row(raw)
        if record is None:
            continue
        records.append(coerce(record))
    return records


def index_by_sku(records):
    return {record["sku"]: record for record in records}
