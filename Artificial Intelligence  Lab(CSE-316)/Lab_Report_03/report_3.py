def is_safe(node, graph, color, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, m, color, node):
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if graph_coloring(graph, m, color, node + 1):
                return True
            color[node] = 0

    return False

def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    n, m, k = map(int, lines[0].split())
    graph = [[] for _ in range(n)]

    for line in lines[1:]:
        u, v = map(int, line.split())
        graph[u].append(v)
        graph[v].append(u)

    color = [0] * n
    if graph_coloring(graph, k, color, 0):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", color)
    else:
        print(f"Coloring Not Possible with {k} Colors")

if __name__ == "__main__":
    main()
