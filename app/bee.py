import random


class Bee:

    def __init__(self, servers, films, solution):
        self.servers = servers
        self.films = films
        self.solution = solution

    def random_neighbour(self, radius):

        acceptable_ops = [(s, f)
                          for s in self.servers
                          for f in self.films
                          if f in self.solution[s] or f.size <= self.free_space(s)]

        op = random.choice(acceptable_ops)
        s = op[0]
        f = op[1]
        return self.solution[s].remove(f) if f in self.solution[s] else self.solution[s].append(f)

    def free_space(self, server):
        return 899 - sum([f.size for f in self.solution[server]])
