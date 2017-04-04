from solutionchecker.solution_reader import read_solution
from solutionchecker.input_reader import read_input


def main():
    # todo argparse
    solution = read_solution("/home/andrzej/Documents/solution.sol")
    input_ = read_input("/home/andrzej/Documents/input.in")
    print(solution)
    print(input_)

if __name__ == '__main__':
    main()
