import random
import copy

from util.helpers import distance_matrix
from config.log import logger


class Predatory:
    def __init__(self, problem):
        self.evaluation_number = 64
        self.n_limit = 51
        self.min_threshold = 3
        self.max_threshold = 153
        self.normal_threshold = 48
        self.problem = problem
        self.distance_matrix = self.get_distance_matrix()

    def get_distance_matrix(self):
        return distance_matrix(list(self.problem.node_coords))

    def generate_sequence(self):
        sequence = random.sample(range(0, self.problem.dimension), self.problem.dimension)
        return sequence

    def generate_adjacent_sequence(self, sequence):
        exchange_number_list = random.sample(range(0, len(sequence)), 2)
        exchange_number_list.sort()
        exchange_seq = sequence[exchange_number_list[0]: exchange_number_list[1]]
        exchange_seq.reverse()
        new_seq = copy.deepcopy(sequence)
        new_seq[exchange_number_list[0]: exchange_number_list[1]] = exchange_seq
        return new_seq

    def calculate_sequence_cost(self, sequence):
        seq_cost = 0
        for j in range(1, len(sequence)):
            cost = self.distance_matrix[sequence[j - 1]][sequence[j]]
            seq_cost += cost
        cost_start_end = self.distance_matrix[sequence[0]][sequence[-1]]
        seq_cost += cost_start_end
        return seq_cost

    def evaluation_domain(self, sequence, s_number):
        # evaluation_domain函数：生成n_limit个顺序seq的领域解
        evaluation_seq = [[0 for _ in range(len(sequence) - 1)] for _ in range(s_number)]
        for i in range(0, s_number):
            eval_seq = self.generate_adjacent_sequence(sequence)
            evaluation_seq[i] = eval_seq
        return evaluation_seq

    def restriction_level(self, sequence, number_level):
        restrict_domain = self.evaluation_domain(sequence, number_level)
        restrict_cost = [self.calculate_sequence_cost(restrict_domain[i]) for i in range(number_level)]
        restrict_level = copy.deepcopy(restrict_cost)
        restrict_level.sort()
        restrict_level.insert(0, self.calculate_sequence_cost(sequence))
        return restrict_level

    def solve(self):
        n = self.problem.dimension
        best_seq = self.generate_sequence()
        best_cost = self.calculate_sequence_cost(best_seq)
        cur_restriction_level = self.restriction_level(best_seq, self.n_limit)
        solution = best_seq
        cost_trend_list = [best_cost]
        logger.info("before opt random initial sequence")
        logger.info(best_seq)
        logger.info("before opt random initial sequence cost")
        logger.info(best_cost)
        l = 0
        count = 0
        while l < n:
            if l == self.min_threshold:
                l = self.normal_threshold
            while True:
                ns_domain = self.evaluation_domain(solution, self.evaluation_number)
                ns_cost = [self.calculate_sequence_cost(ns_domain[i]) for i in range(self.evaluation_number)]
                proposal_cost = min(ns_cost)
                proposal_index = ns_cost.index(proposal_cost)
                proposal_solution = ns_domain[proposal_index]
                if proposal_cost < cur_restriction_level[l]:
                    solution = proposal_solution
                    if proposal_cost < best_cost:
                        best_seq = solution
                        best_cost = proposal_cost
                        cur_restriction_level = self.restriction_level(best_seq, self.n_limit)
                        l = 0
                        count = 0
                        cost_trend_list.append(best_cost)
                    else:
                        count += 1
                else:
                    count += 1
                if count > self.max_threshold:
                    count = 0
                    l += 1
                    break
        logger.info("after opt best sequence")
        logger.info(best_seq)
        logger.info("after opt best sequence cost is")
        logger.info(best_cost)

