from solutionchecker.endpoint import Endpoint


def read_input(file):
    amount_of_videos, amount_of_endpoints, amount_of_request_descriptions = -1, -1, -1
    amount_of_cache_servers, cache_size = -1, -1
    video_sizes = dict()
    endpoints = list()
    endpoint_id = 0
    next_endpoint_definition_at_line = 3
    current_endpoint = None
    with open(file) as f:
        line_number = 0
        for line in f:
            line_number += 1
            if line_number == 1:
                amount_of_videos, amount_of_endpoints, amount_of_request_descriptions,\
                    amount_of_cache_servers, cache_size = parse_general_data(line)
            elif line_number == 2:
                video_sizes = parse_video_sizes(line)
            else:
                line_size = len(line.strip().split(" "))
                if line_size == 2:
                    if line_number == next_endpoint_definition_at_line:
                        current_endpoint = parse_endpoint_definition(endpoint_id, line)
                        endpoints.append(current_endpoint)
                        next_endpoint_definition_at_line = line_number\
                            + current_endpoint.amount_of_caches + 1
                        endpoint_id += 1
                    else:
                        cache_id, latency = parse_latency_to_cache_server(line)
                        current_endpoint.cache_server_latencies[cache_id] = latency
                elif line_size == 3:
                    pass
                else:
                    print("incorrect input at line {0}".format(line_number))
                    break
    return [amount_of_videos, amount_of_endpoints, amount_of_request_descriptions,
            amount_of_cache_servers, cache_size, video_sizes, endpoints]


def parse_general_data(line):
    return list(int(x) for x in line.strip().split(" "))


def parse_video_sizes(line):
    video_sizes = dict()
    list_ = list(line.strip().split(" "))
    for i in range(0, len(list_)):
        video_sizes[i] = int(list_[i])
    return video_sizes


def parse_endpoint_definition(id_, line):
    line = list(int(x) for x in line.strip().split(" "))
    return Endpoint(id_, line[0], line[1])


def parse_latency_to_cache_server(line):
    return list(int(x) for x in line.strip().split(" "))
