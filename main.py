from algorithm.algorithm import Algorithm
from parsers.input_parser import parse_input
from utils.solution_checker import check_solution
import time

def main():
    # input_file = "files/videos_worth_spreading.in"
    # input_file = "files/kittens.in"
    # input_file = "files/example1.in"
    # input_file = "files/me_at_the_zoo.in"
    input_file = "files/trending_today.in"

    # solution_file = "files/example1.out"
    # solution = check_solution(input_file, solution_file)
    # print(solution)

    before = time.time()
    score = Algorithm.execute(parse_input(input_file))
    after = time.time()

    print("-----------------------------")
    print("Algorithm took time: " + str(round(after-before, 2)) + " s")
    print("-----------------------------")
    print("Saved time: " + str(round(score / 1000, 2)) + " s")

if __name__ == '__main__':
    main()
