from app.core.routing import load_station_data, build_graph, shortest_path, generate_instructions
# Load once at startup
station_data = load_station_data("app/data/station_data.json")
graph = build_graph(station_data["edges"])


def get_route_service(start, end, mode):
    if start not in graph:
        return {"error": f"Start node '{start}' does not exist", "status": 400}

    if end not in graph:
        return {"error": f"End node '{end}' does not exist", "status": 400}

    result = shortest_path(graph, start, end, mode)

    if not result:
        return {"error": "No route found", "status": 404}

    instructions = generate_instructions(graph, result["path"])

    return {
        "data": {
            "start": start,
            "end": end,
            "mode": mode,
            "path": result["path"],
            "total_time": result["total_time"],
            "instructions": instructions
        },
        "status": 200
    }
def list_nodes_service():
    return sorted(list(graph.keys()))

def evaluate_transfer_service(start, end, mode, transfer_time, delay):
    route_result = get_route_service(start, end, mode)

    if route_result["status"] != 200:
        return route_result

    route_data = route_result["data"]

    remaining_time = transfer_time - delay
    required_time = route_data["total_time"]

    if remaining_time >= required_time:
        status = "safe"
        message = "Transfer is still possible."
    elif remaining_time > 0:
        status = "risky"
        message = "Transfer is risky. Move quickly or consider a backup option."
    else:
        status = "missed"
        message = "Transfer is likely missed. Look for the next connection."

    return {
        "data": {
            "start": start,
            "end": end,
            "mode": mode,
            "transfer_time": transfer_time,
            "delay": delay,
            "remaining_time": remaining_time,
            "required_time": required_time,
            "status": status,
            "message": message,
            "route": route_data
        },
        "status": 200
    }