"""Assemble the weekly usage report."""

SECTIONS = ("summary", "growth", "retention", "billing", "support")


def build_report(
    account_id,
    start_date,
    end_date,
    include_growth,
    include_retention,
    include_billing,
    include_support,
    compare_previous,
    currency,
    locale,
    timezone,
    recipient_email,
    attach_csv,
    send_immediately,
):
    """Render one account's weekly report."""
    header = {
        "account": account_id,
        "period": (start_date, end_date),
        "currency": currency,
        "locale": locale,
        "timezone": timezone,
        "compare_previous": compare_previous,
    }

    sections = ["summary"]
    if include_growth:
        sections.append("growth")
    if include_retention:
        sections.append("retention")
    if include_billing:
        sections.append("billing")
    if include_support:
        sections.append("support")

    return {
        "header": header,
        "sections": sections,
        "delivery": {
            "to": recipient_email,
            "csv": attach_csv,
            "immediate": send_immediately,
        },
    }


def schedule_all(accounts, defaults):
    reports = []
    for account in accounts:
        reports.append(
            build_report(
                account.id,
                defaults.start_date,
                defaults.end_date,
                account.tier != "free",
                account.tier == "enterprise",
                account.billable,
                account.has_support_plan,
                defaults.compare_previous,
                account.currency,
                account.locale,
                account.timezone,
                account.owner_email,
                account.wants_csv,
                defaults.send_immediately,
            )
        )
    return reports
