from datarepresentation.endpoint import Endpoint
from datarepresentation.requestinfo import RequestInfo


def parse_input(file):
    """
    Description here...

    :param file:
    :return:
    """
    amount_of_videos, amount_of_endpoints, amount_of_request_descriptions = -1, -1, -1
    amount_of_cache_servers, cache_size = -1, -1
    video_sizes = dict()
    endpoints = list()
    endpoint_id = 0
    next_endpoint_definition_at_line = 3
    current_endpoint = None
    requests = list()
    with open(file) as f:
        line_number = 0
        for line in f:
            line_number += 1
            if line_number == 1:
                amount_of_videos, amount_of_endpoints, amount_of_request_descriptions,\
                    amount_of_cache_servers, cache_size = __parse_general_data(line)
            elif line_number == 2:
                video_sizes = __parse_video_sizes(line)
            else:
                line_size = len(line.strip().split(" "))
                if line_size == 2:
                    if line_number == next_endpoint_definition_at_line:
                        current_endpoint = __parse_endpoint_definition(endpoint_id, line)
                        endpoints.append(current_endpoint)
                        next_endpoint_definition_at_line = line_number\
                            + current_endpoint.amount_of_caches + 1
                        endpoint_id += 1
                    else:
                        cache_id, latency = __parse_latency_to_cache_server(line)
                        current_endpoint.cache_server_latencies[cache_id] = latency
                elif line_size == 3:
                    requests.append(__parse_request_info(line))
                else:
                    print("incorrect input at line {0}".format(line_number))
                    break
    return [amount_of_videos, amount_of_endpoints, amount_of_request_descriptions,
            amount_of_cache_servers, cache_size, video_sizes, endpoints, requests]


def __parse_general_data(line: str):
    return list(int(x) for x in line.strip().split(" "))


def __parse_video_sizes(line: str):
    video_sizes = dict()
    video_sizes_list = list(line.strip().split(" "))
    for i in range(0, len(video_sizes_list)):
        video_sizes[i] = int(video_sizes_list[i])
    return video_sizes


def __parse_endpoint_definition(id_: int, line: str):
    endpoint_parameters = list(int(x) for x in line.strip().split(" "))
    return Endpoint(id_, endpoint_parameters[0], endpoint_parameters[1])


def __parse_latency_to_cache_server(line: str):
    return list(int(x) for x in line.strip().split(" "))


def __parse_request_info(line: str):
    line = line.strip().split(" ")
    request_information = list(int(x) for x in line)
    return RequestInfo(request_information[0], request_information[1], request_information[2])
