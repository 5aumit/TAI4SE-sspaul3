"""Work out which shipping band an order falls into."""

DOMESTIC = "domestic"
EUROPE = "europe"
REST_OF_WORLD = "row"

FREE_THRESHOLD = 75.0
HEAVY_KG = 20.0


def band(order, customer, calendar):
    """Return the shipping band, or None when the order cannot ship."""
    if order.destination is None:
        return None

    if order.destination.country == "GB":
        if order.weight_kg > HEAVY_KG:
            if order.contains_hazardous:
                if not customer.has_hazmat_agreement:
                    return None
                elif calendar.is_holiday(order.placed_at):
                    return "domestic-hazmat-delayed"
                else:
                    return "domestic-hazmat"
            elif order.total >= FREE_THRESHOLD:
                return "domestic-heavy-free"
            else:
                return "domestic-heavy"
        elif order.express:
            if calendar.is_weekend(order.placed_at) and not customer.is_business:
                return "domestic-express-monday"
            else:
                return "domestic-express"
        elif order.total >= FREE_THRESHOLD:
            return "domestic-free"
        else:
            return DOMESTIC
    elif order.destination.in_eu:
        if order.contains_hazardous:
            return None
        elif order.weight_kg > HEAVY_KG:
            if customer.is_business:
                return "europe-freight"
            else:
                return "europe-heavy"
        elif order.express and not calendar.is_holiday(order.placed_at):
            return "europe-express"
        else:
            return EUROPE
    else:
        if order.contains_hazardous or order.weight_kg > HEAVY_KG:
            return None
        elif customer.is_business and order.total >= FREE_THRESHOLD * 2:
            return "row-account"
        else:
            return REST_OF_WORLD


def describe(code):
    return code.replace("-", " ") if code else "not shippable"
