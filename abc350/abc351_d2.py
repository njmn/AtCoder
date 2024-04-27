n,m = input().split()
n = int(n)
m = int(m)

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

uf = UnionFind(n)

for i in range(m):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)

parent_list =[]
for i in range(n):
    if 0 == uf.size[i]:
        continue
    parent_list.append(uf.size[i])

complete_graph_con_count = 0

for i in parent_list:
    complete_graph_con_count += i*(i-1)//2

print(complete_graph_con_count-m)