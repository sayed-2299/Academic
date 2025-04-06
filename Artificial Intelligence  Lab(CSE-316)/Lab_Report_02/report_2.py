from typing import List, Tuple

class MazeSolver:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dls(self, maze: List[List[int]], current: Tuple[int, int], target: Tuple[int, int], depth: int, visited: set,
            path: List[Tuple[int, int]]) -> Tuple[bool, List[Tuple[int, int]]]:
        if depth < 0:
            return False, []

        if current == target:
            path.append(current)
            return True, path

        x, y = current
        visited.add(current)
        path.append(current)

        for dx, dy in self.directions:
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < self.rows and 0 <= next_y < self.cols and (
            maze[next_x][next_y] == 0) and (next_x, next_y) not in visited):
                found, final_path = self.dls(maze, (next_x, next_y), target, depth - 1, visited, path.copy())
                if found:
                    return True, final_path

        return False, []

    def iddfs(self, maze: List[List[int]], start: Tuple[int, int], target: Tuple[int, int], max_depth: int) -> Tuple[
        bool, List[Tuple[int, int]]]:
        for depth in range(max_depth + 1):
            visited = set()
            found, path = self.dls(maze, start, target, depth, visited, [])
            if found:
                return True, path
        return False, []

def main():
    rows, cols = map(int, input("Size of Maze: ").split())
    print("Enter the maze elements row by row :")
    maze = [list(map(int, input().split())) for _ in range(rows)]

    start_x, start_y = map(int, input("Start: ").split())
    target_x, target_y = map(int, input("Target: ").split())
    max_depth = int(input("Maximum Depth to Search: "))

    solver = MazeSolver(rows, cols)
    found, path = solver.iddfs(maze, (start_x, start_y), (target_x, target_y), max_depth)

    if found:
        print(f"Path found at depth {len(path) - 1} using IDDFS")
        print(f"Traversal Order: {[(x, y) for x, y in path]}")
    else:
        print(f"Path not found at max depth {max_depth} using IDDFS")

if __name__ == "__main__":
    main()