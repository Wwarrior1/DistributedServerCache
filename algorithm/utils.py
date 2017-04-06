import random
from utils.solution_checker import calculate_score


class AlgorithmUtils:

    @staticmethod
    def random_solution(data):
        res = dict()
        for ids in range(data.amount_of_cache_servers):
            res[ids] = [0]
        return res

    @staticmethod
    def print_solution_pool(pool):
        print("\nPOOL:\n", "\n".join(map(str, pool)))

    @staticmethod
    def random_neighbour(data, solution, radius):

        res = solution.copy()
        if radius == 0:
            return res

        acceptable_ops = [(s, f)
                          for s in range(data.amount_of_cache_servers)
                          for f in range(len(data.videos_sizes))
                          if f in res[s] or data.videos_sizes[f] <= AlgorithmUtils.free_space(data, s, solution)]

        op = random.choice(acceptable_ops)
        s = op[0]
        f = op[1]

        if f in res[s]:
            res[s].remove(f)
        else:
            res[s].append(f)

        return AlgorithmUtils.random_neighbour(data, res, radius - 1)

    @staticmethod
    def best_in_neighbourhood(data, solution, radius, number_of_bees):
        neighbours = []
        for _ in range(number_of_bees):
            neighbours.append(AlgorithmUtils.random_neighbour(data, solution, radius))
        best_neighbour = min(neighbours, key=lambda s: calculate_score(data, s))
        return best_neighbour if calculate_score(data, best_neighbour) < calculate_score(data, solution) else solution

    @staticmethod
    def free_space(data, server, solution):
        return 999
