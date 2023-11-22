class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

def min_operations_to_connect_cities(N, routes):
    uf = UnionFind(N)

    for route in routes:
        city1, city2 = route
        uf.union(city1, city2)

    # Count the number of disjoint sets
    disjoint_sets = len(set(uf.find(city) for city in range(N)))

    # The minimum number of operations is equal to the number of disjoint sets minus 1
    return disjoint_sets - 1 if disjoint_sets > 1 else 0

# Example usage:
N = int(input())
route_len = int(input())
routes = []
for i in range(route_len):
    inp = input()
    inp = map(int , inp.split())
    routes.append(inp)

result = min_operations_to_connect_cities(N, routes)
print(result)
