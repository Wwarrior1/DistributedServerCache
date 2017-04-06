from algorithm.algorithm import Algorithm
from parsers.input_parser import parse_input


def main():
    # input_file = "files/videos_worth_spreading.in"
    # input_file = "files/kittens.in"
    # input_file = "files/example1.in"
    input_file = "files/trending_today.in"

    # solution_file = "files/example1.out"
    # solution = check_solution(input_file, solution_file)
    # print(solution)

    score = Algorithm.execute(parse_input(input_file))
    print(score)

if __name__ == '__main__':
    main()
