import os
import copy
import random


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
    sequence = random.sample(range(1, n + 1), n)
    return sequence


def calculate_sequence_cost(sequence, distance):
    seq_cost = 0
    for j in range(0, len(sequence) - 1):
        cost = distance[sequence[j]][sequence[j + 1]]
        seq_cost += cost
    cost2 = distance[sequence[0]][sequence[-1]]
    seq_cost += cost2
    return seq_cost


def generate_adjacent_sequence(sequence):
    exchange_number_list = random.sample(range(0, len(sequence)), 2)
    exchange_number_list.sort()
    exchange_seq = sequence[exchange_number_list[0]: exchange_number_list[1]]
    exchange_seq.reverse()
    new_seq = copy.deepcopy(sequence)
    new_seq[exchange_number_list[0]: exchange_number_list[1]] = exchange_seq
    return new_seq


if __name__ == '__main__':
    file = r"/resources/berlin52.txt"
    cur_path = os.path.abspath(os.path.dirname(__file__))
    root_path = os.path.dirname(os.path.dirname(__file__))
    input_file_path = root_path + file
    print(root_path)
    print(input_file_path)
    print(build_data(input_file_path))
    print(generate_sequence(4))
