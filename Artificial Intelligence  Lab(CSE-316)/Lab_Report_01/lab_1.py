import numpy as np
import random

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class DFS:
    def __init__(self):
        self.directions = [(1, 0, "down"), (-1, 0, "up"), (0, 1, "right"), (0, -1, "left")]
        self.found = False
        self.N = 0
        self.source = None
        self.goal = None
        self.visited = set()
        self.path = []
        self.topological_order = []
        self.parent = {}

    def run(self):
        self.N = np.random.randint(4, 8)
        graph = np.random.randint(0, 2, size=(self.N, self.N))
        print("Grid:")
        print(graph)

        valid_cells = []
        for x in range(self.N):
            for y in range(self.N):
                if graph[x][y] == 1:
                    valid_cells.append((x, y))

        source_x, source_y = random.choice(valid_cells)
        dest_x, dest_y = random.choice(valid_cells)
        while source_x == dest_x and source_y == dest_y:
            dest_x, dest_y = random.choice(valid_cells)

        self.source = Node(source_x, source_y)
        self.goal = Node(dest_x, dest_y)

        print("Source:", self.source.x, self.source.y)
        print("Goal:", self.goal.x, self.goal.y)

        self.st_dfs(graph)

        if self.found:
            print("Goal found & DFS Path:")
            self.print_path()
        else:
            print("Goal cannot be reached")

        print("Topological Order:", self.topological_order)

    def st_dfs(self, graph):
        stack = []
        stack.append(self.source)
        self.visited.add((self.source.x, self.source.y))
        self.parent[(self.source.x, self.source.y)] = None

        while stack:
            u = stack.pop()
            self.topological_order.append((u.x, u.y))

            if u.x == self.goal.x and u.y == self.goal.y:
                self.found = True
                self.explore_path(u)
                return

            for dx, dy, move in self.directions:
                v_x, v_y = u.x + dx, u.y + dy

                if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1 and (v_x, v_y) not in self.visited:
                    self.visited.add((v_x, v_y))
                    stack.append(Node(v_x, v_y))
                    self.parent[(v_x, v_y)] = (u.x, u.y, move)

    def explore_path(self, node):
        current = (node.x, node.y)
        while current is not None:
            parent_info = self.parent[current]
            if parent_info is not None:
                parent_x, parent_y, move = parent_info
                self.path.append((current[0], current[1], move))
                current = (parent_x, parent_y)
            else:
                self.path.append((current[0], current[1], None))
                current = None
        self.path.reverse()

    def print_path(self):
        for x, y, move in self.path:
            if move is not None:
                print(f"({x}, {y}), {move}")
            else:
                print(f"({x}, {y})")

if __name__ == "__main__":
    dfs = DFS()
    dfs.run()