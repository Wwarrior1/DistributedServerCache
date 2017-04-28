from os.path import join

from os import listdir, remove


def save_solution(solution, name):
    with open(name, 'w') as f:
        f.write(str(len(solution)) + "\n")
        for s in solution:
            f.write(str(s) + " " + " ".join([str(v) for v in solution[s]]) + "\n")


def save_execution_parameters(separator, file, n, m, e, nep, nsp, ngh, iterations, score, output_file):
    with open(output_file, 'w') as f:
        f.write(separator.join(str(x) for x in (file, n, m, e, nep, nsp, ngh, iterations, score)))


def concatenate_executions_results(separator, directory, extension, output_file):
    with open(output_file, 'w') as out:
        out.write(separator.join(("file", "n", "m", "e", "nep", "nsp", "ngp", "iterations", "score")) + "\n")
        for file in listdir(directory):
            if file.endswith(extension):
                file = join(directory, file)
                with open(file, 'r') as inp:
                    for line in inp:
                        if line.endswith("\n"):
                            out.write(line)
                        else:
                            out.write(line + "\n")
                remove(file)
