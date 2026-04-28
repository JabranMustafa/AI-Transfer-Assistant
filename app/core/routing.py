import json
import heapq


def load_station_data(file_path="app/station_data.json"):
    with open(file_path, "r") as file:
        return json.load(file)


def build_graph(edges):
    graph = {}

    for edge in edges:
        start = edge["from"]
        end = edge["to"]
        time = edge["time"]
        edge_type = edge["type"]

        if start not in graph:
            graph[start] = []
        if end not in graph:
            graph[end] = []

        graph[start].append((end, time, edge_type))
        graph[end].append((start, time, edge_type))

    return graph


def shortest_path(graph, start, end, mode="fastest"):
    priority_queue = [(0, start, [start])]
    visited = set()

    while priority_queue:
        total_time, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            return {
                "path": path,
                "total_time": total_time
            }

        for neighbor, travel_time, edge_type in graph.get(current_node, []):

            #  Skip stairs if needed
            if mode in ["no_stairs", "wheelchair"] and edge_type == "stairs":
                continue

            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (total_time + travel_time, neighbor, path + [neighbor])
                )

    return None

def generate_instructions(graph, path):
    instructions = []

    if not path or len(path) == 0:
        return instructions

    def readable(name):
        return name.replace("_", " ")

    instructions.append(f"Start at {readable(path[0])}")

    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]

        edge_type = None

        for neighbor, travel_time, current_edge_type in graph.get(current_node, []):
            if neighbor == next_node:
                edge_type = current_edge_type
                break

        current_readable = readable(current_node)
        next_readable = readable(next_node)

        if edge_type == "stairs":
            if "Stairs" in next_node:
                instructions.append(f"Go to {next_readable}")
                instructions.append("Use the stairs")
            else:
                instructions.append(f"Take the stairs to {next_readable}")

        elif edge_type == "lift":
            if "Elevator" in current_node:
                instructions.append("Use the elevator")
            else:
                instructions.append(f"Go to {next_readable}")

        elif edge_type == "walk":
            instructions.append(f"Walk to {next_readable}")

        else:
            instructions.append(f"Go to {next_readable}")

    instructions.append(f"Arrive at {readable(path[-1])}")

    return instructions