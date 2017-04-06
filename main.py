from utils.solution_checker import check_solution
from algorithm.algorithm import Algorithm
from parsers.input_parser import parse_input
from utils.solution_checker import calculate_score


def main():
    input_file = "files/example1.in"
    # solution_file = "files/example1.out"
    # solution = check_solution(input_file, solution_file)
    # print(solution)

    algo = Algorithm(5, 3, 1, 4, 2, 1, 11)
    score = algo.execute(parse_input(input_file))
    print(score)

if __name__ == '__main__':
    main()
