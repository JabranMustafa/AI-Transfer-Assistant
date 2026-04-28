from typing import Literal
from mcp.server.fastmcp import FastMCP
from app.services.route_service import get_route_service, list_nodes_service
mcp = FastMCP("AI Transfer Assistant")


@mcp.tool()
def list_nodes() -> list[str]:
    """Return all available station nodes."""
    return list_nodes_service()


@mcp.tool()
def find_route(
    start: str,
    end: str,
    mode: Literal["fastest", "no_stairs", "wheelchair"] = "fastest"
) -> dict:
    """
    Find a route between two station nodes.
    Returns path, total_time, and human-readable instructions.
    """
    result = get_route_service(start, end, mode)

    if result["status"] != 200:
        return {
            "success": False,
            "error": result["error"],
            "status": result["status"]
        }

    return {
        "success": True,
        **result["data"]
    }


if __name__ == "__main__":
    mcp.run()