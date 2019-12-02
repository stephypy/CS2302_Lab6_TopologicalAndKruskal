class DisjointSetForest:
    def __init__(self, n):
        self.forest = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index < len(self.forest)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.forest[a] < 0:
            return a

        self.forest[a] = self.find(self.forest[a])  # Path compression

        return self.forest[a]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra != rb:
            self.forest[rb] = ra

    def __str__(self):
        return str(self.forest)
