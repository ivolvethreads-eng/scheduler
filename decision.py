from analyzer import find_overlap
from predictor import generate_rotation, fairness_score
from calendar_utils import generate_dummy_schedule_links
from graph import build_fairness_graph, graph_to_json

def make_decision(team):
    result = find_overlap(team)

    if result["type"] == "overlap":
        return {
            "status": "success",
            "mode": "overlap",
            "start": str(result["start"]),
            "end": str(result["end"])
        }

    schedule = generate_rotation(team)
    score = fairness_score(schedule)
    calendar_links = generate_dummy_schedule_links(schedule)

    return {
        "status": "success",
        "mode": "fairness",
        "schedule": schedule,
        "fairness_score": score,
        "calendar_links": calendar_links
    }