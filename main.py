from parsers.input_parser import parse_input
from parsers.solution_parser import parse_solution


def main():
    solution = parse_solution("/home/andrzej/Documents/solution.out")
    input_ = parse_input("/home/andrzej/Documents/input.in")
    print(solution)
    print(input_[:-2])
    print("Endpoints:")
    for e in input_[-2]:
        print(e)
    print("Requests:")
    for r in input_[-1]:
        print(r)

if __name__ == '__main__':
    main()
