from datetime import datetime, timedelta
import pytz

def get_utc_range(member):
    tz = member["timezone"]

    today = datetime.utcnow().date()

    start_local = tz.localize(datetime.combine(today, member["start"]))
    end_local = tz.localize(datetime.combine(today, member["end"]))

    return (
        start_local.astimezone(pytz.utc),
        end_local.astimezone(pytz.utc)
    )


def find_overlap(team):
    ranges = [get_utc_range(m) for m in team]

    latest_start = max(r[0] for r in ranges)
    earliest_end = min(r[1] for r in ranges)

    if latest_start < earliest_end:
        return {
            "type": "overlap",
            "start": latest_start,
            "end": earliest_end
        }

    return {
        "type": "no_overlap",
        "ranges": ranges
    }