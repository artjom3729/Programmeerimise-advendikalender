import itertools

input_str = """Pärnu: Tallinn - 151min| ; |Tartu - 118min| ; |Lennarti Kodu - 181min
Tallinn: Pärnu - 123min| ; |Tartu - 130min| ; |Lennarti Kodu - 108min
Tartu: Pärnu - 71min| ; |Tallinn - 79min| ; |Lennarti Kodu - 147min
Lennarti Kodu: Pärnu - 123min| ; |Tallinn - 82min| ; |Tartu - 240min"""

graph = {}
for line in input_str.strip().splitlines():
    city, connections = line.split(": ")
    connections = connections.split("| ; |")
    graph[city] = {}
    for connection in connections:
        dest, time = connection.split(" - ")
        graph[city][dest] = int(time.replace("min", ""))


def calculate_route_time(route, graph):
    total_time = 0
    for i in range(len(route) - 1):
        total_time += graph[route[i]][route[i + 1]]
    return total_time


cities = list(graph.keys())
cities.remove("Lennarti Kodu")

permutations = itertools.permutations(cities)

shortest_route = None
shortest_time = float("inf")
for perm in permutations:
    route = ["Lennarti Kodu"] + list(perm) + ["Lennarti Kodu"]
    route_time = calculate_route_time(route, graph)
    if route_time < shortest_time:
        shortest_time = route_time
        shortest_route = route


print(" -> ".join(shortest_route)) # Expected output: Lennarti Kodu -> Pärnu -> Tartu -> Tallinn -> Lennarti Kodu
