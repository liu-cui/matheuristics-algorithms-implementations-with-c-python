import os
import copy
import random
from parameter import Parameter


def build_data(file_path):
    location = []
    with open(file_path) as f:
        for line in f:
            if line == "\n":
                line.strip("\n")
            else:
                line = ((line.strip("\n")).strip(" ")).split(" ")
                line = [float(line[i]) if i > 0 else int(line[i]) - 1 for i in range(len(line))]
                location.append(line)
    return location


def build_distance_matrix(location):
    n = len(location)
    distance = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x = pow(location[i][1] - location[j][1], 2)
            y = pow(location[i][2] - location[j][2], 2)
            distance[i][j] = pow(x + y, 0.5)
    return distance


def generate_sequence(n):
    sequence = random.sample(range(0, n), n)
    return sequence


def generate_adjacent_sequence(sequence):
    exchange_number_list = random.sample(range(0, len(sequence)), 2)
    exchange_number_list.sort()
    exchange_seq = sequence[exchange_number_list[0]: exchange_number_list[1]]
    exchange_seq.reverse()
    new_seq = copy.deepcopy(sequence)
    new_seq[exchange_number_list[0]: exchange_number_list[1]] = exchange_seq
    return new_seq


def calculate_sequence_cost(sequence, distance):
    seq_cost = 0
    for j in range(1, len(sequence)):
        cost = distance[sequence[j-1]][sequence[j]]
        seq_cost += cost
    cost_start_end = distance[sequence[0]][sequence[-1]]
    seq_cost += cost_start_end
    return seq_cost


def evaluation_domain(sequence, s_number):
    # evaluation_domain函数：生成n_limit个顺序seq的领域解
    evaluation_seq = [[0 for _ in range(len(sequence) - 1)] for _ in range(s_number)]
    for i in range(0, s_number):
        eval_seq = generate_adjacent_sequence(sequence)
        evaluation_seq[i] = eval_seq
    return evaluation_seq


def restriction_level(sequence, distance, number_level):
    restrict_domain = evaluation_domain(sequence, number_level)
    restrict_cost = [calculate_sequence_cost(restrict_domain[i], distance) for i in range(number_level)]
    restrict_level = copy.deepcopy(restrict_cost)
    restrict_level.sort()
    restrict_level.insert(0, calculate_sequence_cost(sequence, distance))
    return restrict_level


def solve(file_path, param):
    location_list = build_data(file_path)
    n = len(location_list)
    distance = build_distance_matrix(location_list)
    best_seq = generate_sequence(n)
    best_cost = calculate_sequence_cost(best_seq, distance)
    cur_restriction_level = restriction_level(best_seq, distance, param.n_limit)
    solution = best_seq
    cost_trend_list = [best_cost]
    print("before opt random initial sequence: \n", best_seq)
    print("before opt random initial sequence cost: ", best_cost)

    l = 0
    count = 0
    while l < n:
        if l == param.min_threshold:
            l = param.normal_threshold
        while True:
            ns_domain = evaluation_domain(solution, param.evaluation_number)
            ns_cost = [calculate_sequence_cost(ns_domain[i], distance) for i in range(param.evaluation_number)]
            proposal_cost = min(ns_cost)
            proposal_index = ns_cost.index(proposal_cost)
            proposal_solution = ns_domain[proposal_index]
            if proposal_cost < cur_restriction_level[l]:
                solution = proposal_solution
                if proposal_cost < best_cost:
                    best_seq = solution
                    best_cost = proposal_cost
                    cur_restriction_level = restriction_level(best_seq, distance, param.n_limit)
                    l = 0
                    count = 0
                    cost_trend_list.append(best_cost)
                else:
                    count += 1
            else:
                count += 1
            if count > param.max_threshold:
                count = 0
                l += 1
                break
    print("after opt best sequence: \n", best_seq)
    print("after opt best sequence cost is: ", best_cost)


if __name__ == '__main__':
    file = r"/resources/berlin52.txt"
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = os.path.dirname(os.path.dirname(__file__))
    input_file_path = root_path + file
    parameter = Parameter()
    location = build_data(input_file_path)
    dist = build_distance_matrix(location)
    seq = generate_sequence(len(location))
    cost = calculate_sequence_cost(seq, dist)
    solve(input_file_path, parameter)

