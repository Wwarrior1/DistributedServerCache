from app.solution import Solution
from datarepresentation.movie import Movie
from datarepresentation.server import Server
from datarepresentation.endpoint import Endpoint
from datarepresentation.datacenter import DataCenter
from datarepresentation.connection import Connection
from datarepresentation.requestinfo import RequestInfo


def data_init():
    endpoints = [Endpoint(0, 44, 1), Endpoint(1, 11, 1)]
    movies = [Movie(0, 55), Movie(1, 99)]
    servers = [Server(0), Server(1)]
    connections = [Connection(endpoints[0], servers[0], 11), Connection(endpoints[1], servers[1], 66)]
    requests = [RequestInfo(0, 0, 3), RequestInfo(1, 1, 1)]

    return DataCenter(endpoints, movies, servers, connections, requests)


def main():

    max_iter = 3
    server_capacity = 99

    data = data_init()

    bee = Solution(data, {data.servers[0]: [data.movies[0]], data.servers[1]: [data.movies[1]]})
    print(bee)
    print(bee.evaluate())
    print(bee.random_neighbour(2))
    print(bee.random_neighbour(1).evaluate())

if __name__ == '__main__':
    main()
