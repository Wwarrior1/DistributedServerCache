import random
from utils.solution_checker import calculate_score


class AlgorithmUtils:

    @staticmethod
    def random_solution(data):
        """
        TODO to jest oczywiscie bez sensu i do zmiany
        Wbrew pozorom problem generowania losowego rozwiazania nie jest trywialny - pamietajmy, ze bierzemy pod uwage
        tylko poprawne rozwiazania i najlepiej by bylo losowac je z rownym prawdopodobienstwem

        Sprowadza sie to do wylosowania takiego zbioru

        Oczywiscie mozna generowac wszystkie mozliwe zbiory... ale przy duzych danych lepiej tego uniknac

        :param data:
        :return:
        """

        res = dict()
        for ids in range(data.amount_of_cache_servers):
            random_video = random.randint(0, len(data.videos_sizes)-1)
            res[ids] = [random_video] if data.videos_sizes[random_video] <= data.cache_size else []
        return res

    @staticmethod
    def random_neighbour(data, solution, radius):

        """
        Na razie to dziala tak, ze 'radius' razy losujemy sasiada w odleglosci 1
        Potencjalnie mozemy wyladowac w odleglosci radius lub mniejszej (w szczegolnosci wrocic do solution) - to chyba
            nie szkodzi?
        Nie ma tez gwarancji, ze sie nie powtorza - to chyba nie szkodzi?
        Prawdopodobienstwo wylosowania kazdego rozwiazania niekoniecznie jest rowne. Ale nie wiem jak inaczej to zrobic.

        TODO or not TODO? Zostawiamy to, czy ktos ma lepszy pomysl? Ja nie. :)
        """

        res = AlgorithmUtils.solution_copy(solution)
        if radius == 0:
            return res

        acceptable_ops = [(s, v)
                          for s in range(data.amount_of_cache_servers)
                          for v in range(len(data.videos_sizes))
                          if v in res[s] or data.videos_sizes[v] <= AlgorithmUtils.free_space(data, solution, s)]

        op = random.choice(acceptable_ops)
        s = op[0]
        v = op[1]

        if v in res[s]:
            res[s].remove(v)
        else:
            res[s].append(v)

        return AlgorithmUtils.random_neighbour(data, res, radius - 1)

    @staticmethod
    def best_in_neighbourhood(data, solution, radius, number_of_bees):

        """
        Wysylamy losowo 'number_of_bees' pszczol do zbadania obszaru o promieniu radius.
        Zwracamy najlepsze z tych rozwiazan.

        TODO Staralem sie wyliczac score od razu, zeby potem nie robic tego ponownie przy max(...) i w ostatnim ifie
        Stad taka dziwna lista krotek: neighbours = [(solution, score(solution)), ...]
        Da sie to bardziej zoptymalizowac?
        """

        neighbours = []
        for _ in range(number_of_bees):
            neighbour = AlgorithmUtils.random_neighbour(data, solution, radius)
            neighbours.append((neighbour, calculate_score(data, neighbour)))
        best_neighbour = max(neighbours, key=lambda s: s[1])
        return best_neighbour[0] if best_neighbour[1] > calculate_score(data, solution) else solution

    @staticmethod
    def free_space(data, solution, server):

        """
        Ile wolnych MB na danym serwerze (do sprawdzania, czy mozna dodac film)
        """

        return data.cache_size - sum([data.videos_sizes[v] for v in solution[server]])

    @staticmethod
    def solution_copy(solution):

        """
        Bo python.
        """

        res = dict()
        for s in solution:
            res[s] = solution[s][:]
        return res
