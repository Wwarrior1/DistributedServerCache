from algorithm.utils import AlgorithmUtils
from utils.solution_checker import calculate_score


class Algorithm:

    @staticmethod
    def execute(data):

        """
        Pomaga myslenie o rozwiazaniach jako o kwiatkach. Kazda pszczola siedzi w danym momencie na jednym konkretnym
        kwiatku, czyli pszczola jest reprezentacja konkretnego rozwiazania.

        n - liczba pszczol, czyli rozwiazan w puli w kazdej iteracji. Ta liczba nigdy sie nie zmieni!
        m - liczba rozwiazan dobrych (w tym elitarnych)
        e - liczba rozwiazan elitarnych (czyli najlepszych)
        nep - kazda pszczola elitarna wybierze nep zblizonych rozwiazan, zeby wybrac jedno najlepsze
            jesli wszystkie beda gorsze, zostanie na tym samym kwiatku, na ktorym jest teraz.
        nsp - j.w., tylko dla rozwiazan dobrych, a nie elitarnych.
        ngh - promien sasiedztwa, czyli jak dalekie rozwiazania rozpatrujemy po elitarnych/dobrych
        max_iter - liczba iteracji
        """

        n = 4
        m = 3
        e = 1
        nep = 4
        nsp = 2
        ngh = 4
        max_iter = 8

        # inicjalizujemy pule losowymi rozwiazaniami
        pool = [AlgorithmUtils.random_solution(data) for _ in range(n)]

        for i in range(max_iter):
            print("Iter ", i)

            # dla kazdego rozwiazania obliczamy wynik - ukladamy je od najlepszych do najgorszych
            solutions_ranking = sorted(pool, key=lambda s: calculate_score(data, s), reverse=True)
            # najlepsze e rozwiazan to elitarne...
            elite_solutions = solutions_ranking[0:e]
            # ... a kolejne (m-e) to po prostu dobre
            good_solutions = solutions_ranking[e:m]

            # tworzymy nowa pule rozwiazan
            pool = []
            # kazde elitarne rozwiazanie zastepujemy jednym, najlepszym sposrod nep wybranych z sasiedztwa
            # UWAGA: to ze np. nep=4, nie znaczy ze dostajemy 4 nowe pszczoly. Po prostu sprawdzamy 4 rozwiazania, ale
            # tylko do najlepszego z nich poleci pszczola. Jedna pszczola tu przyleciala i jedna tu zostanie!
            # Nie jest powiedziane, ze ta pszczola bedzie znowu elitarna w kolejnej itreracji - to moze sie zmienic
            for es in elite_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, es, ngh, nep))
            # to samo dla dobrych rozwiazan
            for gs in good_solutions:
                pool.append(AlgorithmUtils.best_in_neighbourhood(data, gs, ngh, nsp))
            # dla pszczol ktore byly slabe wybieramy dla nich nowe, calkowicie losowe rozwiazania (leca gdzie indziej)
            for _ in range(n-m):
                pool.append(AlgorithmUtils.random_solution(data))

            # podsumowujac - jesli np. n=5, m=3, e=1, to zawsze na koniec iteracji 1 pszczola pochodzi z obszaru
            # elitarnego, 2 z dobrych, a 2 sa losowane od nowa.

        pool = sorted(pool, key=lambda s: calculate_score(data, s), reverse=True)
        return pool[0]
