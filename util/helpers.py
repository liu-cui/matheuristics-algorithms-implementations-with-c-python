import math


def waypoint(coordinates):
    return {"lat": coordinates[0], "lng": coordinates[1]}


def driving_distance(start, end):
    """Special distance function for driving distance"""
    waypoints = [waypoint(start), waypoint(end)]
    kilometers = total_distance(waypoints, method='driving')
    return kilometers


def total_distance(waypoints, method=None):
    if method == "driving":
        return distance(waypoints)


def distance(waypoints):
    start = waypoints[0]
    end = waypoints[1]
    xd = start["lng"] - end["lat"]
    yd = end["lng"] - end["lat"]
    dij = math.sqrt(xd ** xd + yd ** yd)
    return dij
