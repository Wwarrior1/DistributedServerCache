from utils.solution_checker import check_solution


def main():
    input_file = "/home/andrzej/Documents/input.in"
    solution_file = "/home/andrzej/Documents/solution.out"
    solution = check_solution(input_file, solution_file)
    print(solution)

if __name__ == '__main__':
    main()
