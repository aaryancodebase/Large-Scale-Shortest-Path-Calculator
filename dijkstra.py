graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 3, "E": 6},
    "C": {"A": 2, "D": 1},
    "D": {"B": 3, "C": 1, "E": 2},
    "E": {"B": 6, "D": 2}
}

for node in graph:
    for neighbor, weight in graph[node].items():
        if weight < 0:
            raise ValueError(
                "Dijkstra's algorithm cannot be used with negative edge weights."
            )

def dijkstra(graph, start):
    distances = {}
    previous = {}

    for node in graph:
        distances[node] = float("inf")
        previous[node] = None

    distances[start] = 0

    unvisited = set(graph.keys())

    while unvisited:
        current = min(
            unvisited,
            key=lambda node: distances[node]
        )

        unvisited.remove(current)

        if distances[current] == float("inf"):
            break

        for neighbor, weight in graph[current].items():
            new_distance = distances[current] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

    return distances, previous

def reconstruct_path(previous, start, destination):
    path = []
    current = destination

    while current is not None:
        path.append(current)

        if current == start:
            break

        current = previous[current]

    if path[-1] != start:
        return []

    path.reverse()
    return path