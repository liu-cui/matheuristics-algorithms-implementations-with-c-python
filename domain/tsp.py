import tsplib95

PATH = r"archives/problems/tsp/"


class Problem:
    def __init__(self, name):
        self.name = name
        self.path = PATH + name
        self.problem = self.get_problem()
        self.node = self.get_node()
        self.node_coords = self.get_node_coords()
        self.dimension = self.get_dimension()
        self.type = self.get_type()

    def get_problem(self):
        return tsplib95.load(self.path)

    def get_node(self):
        return self.problem.as_name_dict()["node_coords"].keys()

    def get_node_coords(self):
        return self.problem.as_name_dict()["node_coords"].values()

    def get_dimension(self):
        return self.problem.as_name_dict()["dimension"]

    def get_type(self):
        return self.problem.as_name_dict()["type"]


class Solution:
    def __init__(self):
        pass

