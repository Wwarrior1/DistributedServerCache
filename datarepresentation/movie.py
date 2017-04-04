class Movie:
    def __init__(self, idf, size):
        self.idf = idf
        self.size = size

    def __str__(self):
        return "m"+str(self.idf)
