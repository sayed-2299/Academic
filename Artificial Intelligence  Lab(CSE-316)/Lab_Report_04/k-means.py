import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None

class KMeans:
    def __init__(self, points, clusters, grid_size=100):
        self.num_points = points
        self.num_clusters = clusters
        self.grid_size = grid_size
        self.points = []
        self.centroids = []
        self.matrix = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
        self.generate_data()
        self.start()

    def generate_data(self):
        coords = random.sample([(x, y) for x in range(self.grid_size) for y in range(self.grid_size)], self.num_points + self.num_clusters)
        self.points = [Point(x, y) for x, y in coords[:self.num_points]]
        self.centroids = [Point(x, y) for x, y in coords[self.num_points:]]
        with open('data.txt', 'w') as f:
            f.write("Points:\n")
            for p in self.points:
                f.write(f"{p.x},{p.y}\n")
            f.write("Centroids:\n")
            for c in self.centroids:
                f.write(f"{c.x},{c.y}\n")

    def manhattan_distance(self, p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)

    def start(self):
        while True:
            for p in self.points:
                min_dist = float('inf')
                for j, c in enumerate(self.centroids):
                    dist = self.manhattan_distance(p, c)
                    if dist < min_dist:
                        p.cluster = j
                        min_dist = dist
            old_centroids = [Point(c.x, c.y) for c in self.centroids]
            for j in range(self.num_clusters):
                x_sum, y_sum, count = 0, 0, 0
                for p in self.points:
                    if p.cluster == j:
                        x_sum += p.x
                        y_sum += p.y
                        count += 1
                if count > 0:
                    self.centroids[j].x = x_sum // count
                    self.centroids[j].y = y_sum // count
            error = sum(self.manhattan_distance(self.centroids[i], old_centroids[i]) for i in range(self.num_clusters))
            if error == 0:
                break
        for j in range(self.num_clusters):
            intra_dist = sum(self.manhattan_distance(p, self.centroids[j]) for p in self.points if p.cluster == j)
            print(f"Cluster {j + 1} Intra-distance = {intra_dist}")
        for j in range(self.num_clusters):
            for p in self.points:
                if p.cluster == j:
                    print(f"Point ({p.x}, {p.y}) Cluster - {j + 1}")
        for j, c in enumerate(self.centroids):
            print(f"Cluster {j + 1} - ({c.x}, {c.y})")
        for p in self.points:
            self.matrix[p.y][p.x] = 'P'
        for c in self.centroids:
            self.matrix[c.y][c.x] = 'C'
        print("\n2D Visualization (P = Point, C = Centroid, . = Empty):")
        print("   " + " ".join(f"{x:2}" for x in range(self.grid_size)))
        for y in range(self.grid_size - 1, -1, -1):
            row = [self.matrix[y][x] for x in range(self.grid_size)]
            print(f"{y:2} {' '.join(f'{cell:2}' for cell in row)}")

def main():
    kmeans = KMeans(points=100, clusters=10)

if __name__ == "__main__":
    main()