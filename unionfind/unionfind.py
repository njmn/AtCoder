n,m = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            self.size[root_x] = 0

    def group_size(self,x):
        return self.size[self.find(x)]
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(n)

for i in range(m):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)

