def read_solution(file):
    solution = dict()
    with open(file) as f:
        line_number = -1
        for line in f:
            line_number += 1
            if line_number == 0:
                amount_of_servers = int(line)
            elif line_number > amount_of_servers:
                print("too many lines")
                break
            else:
                line = line.strip()
                server_id = line.split(" ")[0]
                videos_ids = line.split(" ")[1:]
                solution[server_id] = videos_ids
    return solution
