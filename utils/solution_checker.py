from parsers.solution_parser import parse_solution
from parsers.input_parser import parse_input


def check_solution(path_to_input_file: str, path_to_solution_file: str):
    """
    Check whether solution is valid or not and if it is valid calculate solution score.

    :param path_to_input_file: path to input file as string
    :param path_to_solution_file: path to solution file as string
    :return: solution score (int)
    """
    input_data = parse_input(path_to_input_file)
    solution = parse_solution(path_to_solution_file)
    validation_result = __validate_solution(input_data, solution)
    if validation_result is True:
        return __calculate_score()
    raise Exception("Solution is not valid! (total size of "
                    "videos stored at server #{0} exceeds "
                    "server capacity)".format(validation_result))


def __validate_solution(input_data: tuple, solution: dict):
    """
    Checks whether solution is valid or not.

    :param input_data: tuple of input data
    :param solution: dictionary of solution data
    :return: returns True if solution is valid. if solution
             is not valid returns index of invalid server.
    """
    server_capacity = input_data[4]
    videos_sizes = input_data[5]
    for server_id in sorted(solution.keys()):
        server_content_size = 0
        for video_id in solution[server_id]:
            server_content_size += videos_sizes[video_id]
        if server_content_size > server_capacity:
            return server_id
    return True


def __calculate_score():
    pass
