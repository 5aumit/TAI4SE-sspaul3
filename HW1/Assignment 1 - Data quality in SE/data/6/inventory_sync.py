"""Push local stock levels up to the warehouse partner."""


def _record(sku, quantity, status):
    return {"sku": sku, "quantity": quantity, "status": status}


def sync_batch(rows, warehouse):
    results = []

    for row in rows:
        if row.quantity < 0:
            results.append(_record(row.sku, row.quantity, "rejected: negative quantity"))
            continue

        if not warehouse.knows(row.sku):
            created = warehouse.create(row.sku, row.description)
            if not created:
                results.append(_record(row.sku, row.quantity, "rejected: negative quantity"))
                continue

        acknowledged = warehouse.set_level(row.sku, row.quantity)
        if acknowledged:
            results.append(_record(row.sku, row.quantity, "accepted"))
        else:
            results.append(_record(row.sku, row.quantity, "rejected: negative quantity"))

    return results


def summarise(results):
    accepted = sum(1 for item in results if item["status"] == "accepted")
    return {"total": len(results), "accepted": accepted, "failed": len(results) - accepted}
