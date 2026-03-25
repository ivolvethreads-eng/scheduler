from datetime import time
import pytz

COMMON_TIMEZONES = {
    "london": "Europe/London",
    "new york": "America/New_York",
    "california": "America/Los_Angeles",
    "us": "America/New_York",
    "usa": "America/New_York",
    "india": "Asia/Kolkata",
    "japan": "Asia/Tokyo",
    "tokyo": "Asia/Tokyo",
}


def normalize_timezone(tz_input):
    tz_input = tz_input.strip().lower()

    if tz_input in COMMON_TIMEZONES:
        return COMMON_TIMEZONES[tz_input]

    return tz_input


def parse_member(member):
    # 🔥 Safe name
    name = member.get("name", "").strip() or "Unknown"

    # 🔥 Safe timezone handling
    tz_input = member.get("timezone", "").strip()

    if not tz_input:
        tz_name = "UTC"
    else:
        tz_name = normalize_timezone(tz_input)

    try:
        tz = pytz.timezone(tz_name)
    except:
        tz = pytz.timezone("UTC")

    # 🔥 Safe time parsing
    try:
        start_hour, start_min = map(int, member["start"].split(":"))
        end_hour, end_min = map(int, member["end"].split(":"))
    except:
        # fallback if input is broken
        start_hour, start_min = 9, 0
        end_hour, end_min = 17, 0

    return {
        "name": name,
        "timezone": tz,
        "start": time(start_hour, start_min),
        "end": time(end_hour, end_min)
    }


def parse_team(team_data):
    return [parse_member(member) for member in team_data]