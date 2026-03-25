def generate_rotation(team):
    """
    Simple fairness:
    Rotate meeting inconvenience across members
    """

    schedule = []

    for i, member in enumerate(team):
        schedule.append({
            "day": f"Day {i+1}",
            "assigned_bad_time_to": member["name"]
        })

    return schedule


def fairness_score(schedule):
    score = {}

    for entry in schedule:
        name = entry["assigned_bad_time_to"]
        score[name] = score.get(name, 0) + 1

    return score