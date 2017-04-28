import time
from argparse import ArgumentParser

from algorithm.algorithm import Algorithm
from parsers.input_parser import parse_input
from parsers.output_builder import save_solution
from utils.argument_parser_util import add_parser_arguments
from utils.solution_checker import check_solution


def main():
    input_file, output_file = args.i, args.o
    n, m, e = args.n, args.m, args.e
    nep, nsp, ngh = args.nep, args.nsp, args.ngh
    iterations = args.max

    before = time.time()
    best_solution = Algorithm.execute(parse_input(input_file), n, m, e, nep, nsp, ngh, iterations)
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
    add_parser_arguments(parser)
    args = parser.parse_args()
    main()
