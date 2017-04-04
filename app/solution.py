import random
from functools import reduce


class Solution:

    def __init__(self, data, solution):
        self.data = data
        self.solution = solution

    def __str__(self):
        res = "Solution: "
        for s in self.solution:
            res += str(s.ids) + "->["
            for m in self.solution[s]:
                res += str(m)
            res += "], "
        return res

    def random_neighbour(self, radius):

        acceptable_ops = [(s, f)
                          for s in self.data.servers
                          for f in self.data.movies
                          if f in self.solution[s] or f.size <= self.free_space(s)]

        op = random.choice(acceptable_ops)
        s = op[0]
        f = op[1]
        return self.solution[s].remove(f) if f in self.solution[s] else self.solution[s].append(f)

    def free_space(self, server):
        return 899 - sum([f.size for f in self.solution[server]])

    def evaluate(self):

        res = 0

        for request in self.data.requests:
            res += 1
            # print(request)

        return res
