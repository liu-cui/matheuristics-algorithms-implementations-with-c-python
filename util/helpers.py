import math


def distance_matrix(nodes_coordinates):
    n = len(nodes_coordinates)
    nodes = [waypoint(coord) for coord in nodes_coordinates]
    dist = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = distance(nodes[i], nodes[j])
    return dist


def waypoint(coordinates):
    return {"lat": coordinates[0], "lng": coordinates[1]}


def driving_distance(start, end):
    """Special distance function for driving distance"""
    waypoints = [waypoint(start), waypoint(end)]
    kilometers = total_distance(waypoints, method='driving')
    return kilometers


def total_distance(waypoints, method=None):
    if method == "driving":
        start = waypoints[0]
        end = waypoints[1]
        return distance(start, end)


def distance(start, end):
    xd = start["lat"] - end["lat"]
    yd = end["lng"] - end["lng"]
    dij = math.sqrt(xd * xd + yd * yd)
    return dij
