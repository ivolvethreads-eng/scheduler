import networkx as nx


def build_fairness_graph(fairness_score):
    """
    fairness_score = {
        "Zain": 2,
        "John": 1
    }
    """

    G = nx.Graph()

    # Add nodes with weight
    for person, score in fairness_score.items():
        G.add_node(person, weight=score)

    # Connect everyone (team relationship)
    people = list(fairness_score.keys())

    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            G.add_edge(people[i], people[j])

    return G


def graph_to_json(G):
    nodes = []
    edges = []

    for node, data in G.nodes(data=True):
        nodes.append({
            "id": node,
            "weight": data.get("weight", 0)
        })

    for u, v in G.edges():
        edges.append({
            "source": u,
            "target": v
        })

    return {
        "nodes": nodes,
        "edges": edges
    }