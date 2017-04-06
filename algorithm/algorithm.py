from algorithm.utils import AlgorithmUtils
from utils.solution_checker import calculate_score


class Algorithm:

    def __init__(self, n, m, e, nep, nsp, ngh, max_iter):
        self.n = n
        self.m = m
        self.e = e
        self.nep = nep
        self.nsp = nsp
        self.ngh = ngh
        self.max_iter = max_iter

    @staticmethod
    def execute(data):

        """
        :param data:
        :return: score of the best solution found
        """

        n = 55
        m = 7
        e = 2
        nep = 44
        nsp = 27
        ngh = 5
        max_iter = 122

        pool = [AlgorithmUtils.random_solution(data) for _ in range(n)]

        for i in range(max_iter):
            print("Iter ", i)

            solutions_ranking = sorted(pool, key=lambda s: calculate_score(data, s), reverse=True)
            elite_solutions = solutions_ranking[0:e]
            good_solutions = solutions_ranking[e:m]

            # AlgorithmUtils.print_solution_pool(solutions_ranking)

            pool = []
            for es in elite_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, es, ngh, nep))
            for gs in good_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, gs, ngh, nsp))
            for _ in range(n-m):
                pool.append(AlgorithmUtils.random_solution(data))

        print(pool[0])
        return calculate_score(data, pool[0])
