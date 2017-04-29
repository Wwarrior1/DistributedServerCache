from os.path import join, split
from subprocess import call
from time import time

from concurrent.futures import ProcessPoolExecutor
from os import getcwd

from parsers.output_builder import clear_results_file


def main():
    main_path = __get_path()
    input_dir = join(split(getcwd())[0], "files")
    input_file = join(input_dir, "me_at_the_zoo.in")
    output_dir = join(split(getcwd())[0], "files")
    output_file = join(output_dir, "results.csv")
    clear_results_file(';', output_file)
    before = time()
    with ProcessPoolExecutor(None) as executor:
        # todo make ranges and steps as parameters? maybe add more parameters to manipulate
        for bees in range(10, 11, 10):
            for iterations in range(100, 150, 50):
                for tries_with_same_parameters in range(0, 10):
                    command = "python {0} -i {1} -o {2} -n {3} -max {4} -s False" \
                        .format(main_path, input_file, output_file, bees, iterations)
                    executor.submit(call, command)
    after = time()
    print("Execution took: " + str(round(after - before, 2)) + " s")


def __get_path():
    directory = split(getcwd())[0]
    filename = "main.py"
    return join(directory, filename)


if __name__ == '__main__':
    main()
