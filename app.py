import tsplib95


problem = tsplib95.load(r'archives/problems/tsp/berlin52.tsp')

if __name__ == '__main__':
    problem = tsplib95.load(r'archives/problems/tsp/berlin52.tsp')
    opt = tsplib95.load('archives/problems/tour/berlin52.opt.tour')
    print(problem.name)
    print(list(problem.get_nodes()))
    tour = problem.trace_tours(opt.tours)
    print(opt.tours[0])
    print(tour)
    print()
    print(problem.as_name_dict())
    print(problem.as_keyword_dict())
    print(problem.node_coords)
    edge = 3, 8
    weight = problem.get_weight(*edge)
    print(f'The driving distance from node {edge[0]} to node {edge[1]} is {weight}.')
    print()
    G = problem.get_graph()
    print(G.nodes)
    print(G.graph)


