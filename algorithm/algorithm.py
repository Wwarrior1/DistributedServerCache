from algorithm.utils import AlgorithmUtils
from utils.solution_checker import calculate_score


class Algorithm:

    @staticmethod
    def execute(data):

        """
        :return: score of the best solution found
        """

        n = 5
        m = 3
        e = 1
        nep = 4
        nsp = 2
        ngh = 5
        max_iter = 2

        pool = [AlgorithmUtils.random_solution(data) for _ in range(n)]

        for i in range(max_iter):
            print("Iter ", i)

            solutions_ranking = sorted(pool, key=lambda s: calculate_score(data, s), reverse=True)
            elite_solutions = solutions_ranking[0:e]
            good_solutions = solutions_ranking[e:m]

            pool = []
            for es in elite_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, es, ngh, nep))
            for gs in good_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, gs, ngh, nsp))
            for _ in range(n-m):
                pool.append(AlgorithmUtils.random_solution(data))

        print(max(pool, key=lambda s: calculate_score(data, s)))
        return calculate_score(data, pool[0])
