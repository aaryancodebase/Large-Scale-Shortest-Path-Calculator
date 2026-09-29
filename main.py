from dijkstra import graph, dijkstra, reconstruct_path

start = "A"
destination = "E"

distances, previous = dijkstra(graph, start)

path = reconstruct_path(previous, start, destination)

print("Shortest Path:", " -> ".join(path))
print("Total Distance:", distances[destination])