import tsplib95

from predatory_search.predatory import Predatory
from domain.tsp import Problem

problem = tsplib95.load('archives/problems/tsp/berlin52.tsp')
opt = tsplib95.load('archives/problems/tour/berlin52.opt.tour')
tour = problem.trace_tours(opt.tours)
print("opt tour: ", opt.tours[0])
print("opt tour cost: ", tour)


if __name__ == "__main__":
    problem = Problem(r"berlin52.tsp")
    sol = Predatory(problem)
    print(len(sol.distance_matrix[0]))
    sol.solve()






