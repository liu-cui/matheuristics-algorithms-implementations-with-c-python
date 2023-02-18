import tsplib95

from predatory_search.predatory import Predatory
from domain.tsp import Problem
from config.log import logger

problem = tsplib95.load('archives/problems/tsp/berlin52.tsp')
opt = tsplib95.load('archives/problems/tour/berlin52.opt.tour')
tour = problem.trace_tours(opt.tours)
logger.info("best tour distance")
logger.info(tour[0])


if __name__ == "__main__":
    problem = Problem(r"berlin52.tsp")
    sol = Predatory(problem)
    sol.solve()







