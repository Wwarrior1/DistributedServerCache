from algorithm.utils import AlgorithmUtils
from utils.solution_checker import calculate_score


class Algorithm:

    @staticmethod
    def execute(data):

        """
        :return: score of the best solution found
        """

        n = 4   # nr of bees == solutions
        m = 3
        e = 1
        nep = 4  # 1 elite bee goes to 4 different places
                 # from these 4 places chooses exactly 1
        nsp = 2  # 2 good bees goes to 2 different places
                 # from these 4 places chooses exactly 1
        ngh = 4     # max distance from center (e.g. elite solution)
        max_iter = 8

        # n losowych rozwiazan (pszczol)
        pool = [AlgorithmUtils.random_solution(data) for _ in range(n)]

        for i in range(max_iter):
            print("Iter ", i)

            # calcuate all solutions and sort them all
            solutions_ranking = sorted(pool, key=lambda s: calculate_score(data, s), reverse=True)
            # choose 1 elite
            elite_solutions = solutions_ranking[0:e]
            good_solutions = solutions_ranking[e:m]

            pool = []
            # choose 1 solution from each elite solutions
            for es in elite_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, es, ngh, nep))
            # choose 1 solution from each good solutions
            for gs in good_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, gs, ngh, nsp))
            # dla pszczol ktore byly slabe wybieramy dla nich nowe rozwiazania (leca gdzie indziej)
            for _ in range(n-m):
                pool.append(AlgorithmUtils.random_solution(data))

        print(max(pool, key=lambda s: calculate_score(data, s)))
        return calculate_score(data, pool[0])
