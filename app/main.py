from app.solution import Solution
from datarepresentation.movie import Movie
from datarepresentation.server import Server
from datarepresentation.endpoint import Endpoint
from datarepresentation.datacenter import DataCenter
from datarepresentation.connection import Connection
from datarepresentation.requestinfo import RequestInfo


def data_init():
    endpoints = [Endpoint(0, 100, 1), Endpoint(1, 100, 1)]
    movies = [Movie(0, 55), Movie(1, 99)]
    servers = [Server(0), Server(1)]
    connections = [Connection(endpoints[0], servers[0], 11), Connection(endpoints[1], servers[1], 66)]
    requests = [RequestInfo(1, 0, 3), RequestInfo(0, 1, 1)]

    return DataCenter(endpoints, movies, servers, connections, requests)


def random_solution(data):
    return Solution(data, {data.servers[0]: [data.movies[0]], data.servers[1]: [data.movies[1]]})


def print_solution_pool(pool):
    print("\nPOOL:\n", "\n".join(map(str, pool)))


def best_in_neighbourhood(solution, radius, number_of_bees):
    neighbours = []
    for _ in range(number_of_bees):
        neighbours.append(solution.random_neighbour(radius))
    best_neighbour = min(neighbours, key=lambda s: s.evaluate())
    return best_neighbour if best_neighbour.evaluate() < solution.evaluate() else solution


def main():

    n = 5
    m = 3
    e = 1
    nep = 4
    nsp = 2
    ngh = 1
    max_iter = 11
    server_capacity = 99

    data = data_init()

    # bee = Solution(data, {data.servers[0]: [data.movies[0]], data.servers[1]: [data.movies[1]]})
    # print(bee)
    # print(bee.random_neighbour(1))

    pool = [random_solution(data) for _ in range(n)]

    for i in range(max_iter):
        print("Iter ", i)

        solutions_ranking = sorted(pool, key=lambda s: s.evaluate())
        elite_solutions = solutions_ranking[0:e]
        good_solutions = solutions_ranking[e:m]

        print_solution_pool(solutions_ranking)
        # print_solution_pool(elite_solutions)
        # print_solution_pool(good_solutions)

        pool = []
        for es in elite_solutions:
            pool.append(best_in_neighbourhood(es, ngh, nep))
        for gs in good_solutions:
            pool.append(best_in_neighbourhood(gs, ngh, nsp))
        for _ in range(n-m):
            pool.append(random_solution(data))


if __name__ == '__main__':
    main()
