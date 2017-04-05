import random


class Solution:

    def __init__(self, data, solution):
        self.data = data
        self.solution = solution

    def __str__(self):
        res = "Solution: "
        for s in self.solution:
            res += str(s.ids) + "->["
            for m in self.solution[s]:
                res += str(m) + " "
            res += "], "
        res += str(self.evaluate())
        return res

    def __copy__(self):
        res = Solution(self.data, dict(self.solution))
        for l in res.solution:
            res.solution[l] = list(res.solution[l])
        return res

    def random_neighbour(self, radius):

        res = self.__copy__()
        if radius == 0:
            return res

        acceptable_ops = [(s, f)
                          for s in res.data.servers
                          for f in res.data.movies
                          if f in res.solution[s] or f.size <= res.free_space(s)]

        op = random.choice(acceptable_ops)
        s = op[0]
        f = op[1]

        if f in res.solution[s]:
            res.solution[s].remove(f)
        else:
            res.solution[s].append(f)

        return res.random_neighbour(radius-1)

    def free_space(self, server):
        return 899 - sum([f.size for f in self.solution[server]])

    def evaluate(self):

        res = 0

        for request in self.data.requests:
            m = self.data.movies[request.video_id]
            e = self.data.endpoints[request.endpoint_id]
            best_conn = e.datacenter_latency

            for c in e.connections:
                if c.latency < best_conn and m in self.solution[c.server]:
                    best_conn = c.latency

            res += best_conn * request.amount_of_requests

        return res
