import tsplib95

from predatory_search.predatory_test import Predatory
from domain.tsp import Problem

problem = tsplib95.load('archives/problems/tsp/berlin52.tsp')
opt = tsplib95.load('archives/problems/tour/berlin52.opt.tour')
print(problem.name)
print(list(problem.get_nodes()))
tour = problem.trace_tours(opt.tours)
print(opt.tours[0])
print(tour)


if __name__ == "__main__":
    problem = Problem(r"berlin52.tsp")
    print(problem.node)
    print(problem.node_coords)
    sol = Predatory(problem)
    print(len(sol.distance_matrix[0]))
    sol.solve()






