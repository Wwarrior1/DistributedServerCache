from app.solution import Solution
from datarepresentation.movie import Movie
from datarepresentation.server import Server


def main():

    max_iter = 3
    server_capacity = 99
    s0 = Server(0)
    s1 = Server(1)
    f0 = Movie(0, 55)
    f1 = Movie(1, 99)

    bee = Solution([s0, s1], [f0, f1], {s0: [f0], s1: [f1]})
    print(bee.random_neighbour(1))

if __name__ == '__main__':
    main()
