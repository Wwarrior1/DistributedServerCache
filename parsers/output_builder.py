def save_solution(solution, name):
    with open(name, 'w') as f:
        f.write(str(len(solution)) + "\n")
        for s in solution:
            f.write(str(s) + " " + " ".join([str(v) for v in solution[s]]) + "\n")
