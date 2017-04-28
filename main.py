import time
from argparse import ArgumentParser
from os.path import join

from os import getcwd

from algorithm.algorithm import Algorithm
from parsers.input_parser import parse_input
from parsers.output_builder import save_solution
from utils.solution_checker import check_solution


def main():
    input_file = args.i
    output_file = args.o

    before = time.time()
    best_solution = Algorithm.execute(parse_input(input_file))
    save_solution(best_solution, output_file)
    score = check_solution(input_file, output_file)
    after = time.time()

    print(best_solution)
    print("-----------------------------")
    print("Algorithm took: " + str(round(after - before, 2)) + " s")
    print("-----------------------------")
    print("Saved time: " + str(round(score / 1000, 2)) + " s (score: " + str(score) + ")")


if __name__ == "__main__":
    parser = ArgumentParser(description="Distributed cache problem solver.")

    default_input_filename = "me_at_the_zoo.in"
    parser.add_argument("-i", "-input_file", help="Path to input file.", type=str,
                        default=join(getcwd(), "files", default_input_filename))

    default_output_filename = "solution.out"
    parser.add_argument("-o", "-output_file", help="Path to output file.", type=str,
                        default=join(getcwd(), "files", default_output_filename))

    args = parser.parse_args()
    main()
