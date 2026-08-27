"""Total up an invoice, applying discounts and tax."""

TAX_RATE = 0.2
BULK_DISCOUNT = 0.05
BULK_THRESHOLD = 10


def line_total(line):
    gross = line.unit_price * line.quantity
    if line.quantity >= BULK_THRESHOLD:
        return gross * (1 - BULK_DISCOUNT)
    return gross


def invoice_total(invoice):
    subtotal = 0.0
    discounted_lines = 0
    line_count = len(invoice.lines)

    for line in invoice.lines:
        total = line_total(line)
        if line.quantity >= BULK_THRESHOLD:
            discounted_lines += 1
        subtotal += total

    tax = subtotal * TAX_RATE
    return {
        "subtotal": round(subtotal, 2),
        "tax": round(tax, 2),
        "total": round(subtotal + tax, 2),
        "lines": line_count,
    }


def format_total(invoice, totals):
    return "%s%.2f" % (invoice.currency.symbol, totals["total"])
