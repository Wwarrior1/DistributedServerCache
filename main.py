from utils.solution_checker import check_solution


def main():
    input_file = "files/example1.in"
    solution_file = "files/example1.out"
    solution = check_solution(input_file, solution_file)
    print(solution)

if __name__ == '__main__':
    main()
