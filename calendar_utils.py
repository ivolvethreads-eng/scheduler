from datetime import datetime, timedelta

def generate_google_calendar_link(title, start_dt, end_dt):
    """
    start_dt, end_dt should be UTC datetime objects
    """

    def format_time(dt):
        return dt.strftime("%Y%m%dT%H%M%SZ")

    base_url = "https://calendar.google.com/calendar/render?action=TEMPLATE"

    link = (
        f"{base_url}"
        f"&text={title}"
        f"&dates={format_time(start_dt)}/{format_time(end_dt)}"
    )

    return link


def generate_dummy_schedule_links(schedule):
    """
    For now: fake times just to demonstrate flow
    Later you can plug real times
    """

    links = []

    now = datetime.utcnow()

    for i, entry in enumerate(schedule):
        start = now + timedelta(days=i)
        end = start + timedelta(hours=1)

        link = generate_google_calendar_link(
            title=f"Team Meeting ({entry['assigned_bad_time_to']})",
            start_dt=start,
            end_dt=end
        )

        links.append({
            "day": entry["day"],
            "assigned_to": entry["assigned_bad_time_to"],
            "calendar_link": link
        })

    return links