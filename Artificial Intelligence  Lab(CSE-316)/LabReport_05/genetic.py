import random
import numpy as np


def calculate_fitness(individual):
    n = len(individual)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    return -conflicts


def genetic_algorithm(n=8, pop_size=100, max_generations=1000):
    population = [list(np.random.permutation(n)) for _ in range(pop_size)]
    for _ in range(max_generations):
        fitnesses = [calculate_fitness(ind) for ind in population]
        best_idx = np.argmax(fitnesses)
        if fitnesses[best_idx] == 0:
            return population[best_idx]

        new_population = [population[best_idx]]
        for _ in range(pop_size - 1):
            parent1, parent2 = random.choices(population, weights=[f + max(-min(fitnesses), 1) for f in fitnesses], k=2)

            start, end = sorted(random.sample(range(n), 2))
            child = [-1] * n
            child[start:end] = parent1[start:end]
            p2_idx = 0
            for i in range(n):
                if child[i] == -1:
                    while parent2[p2_idx] in child:
                        p2_idx += 1
                    child[i] = parent2[p2_idx]
                    p2_idx += 1

            if random.random() < 0.1:
                i, j = random.sample(range(n), 2)
                child[i], child[j] = child[j], child[i]

            new_population.append(child)
        population = new_population
    return population[np.argmax([calculate_fitness(ind) for ind in population])]


def print_board(solution):
    n = len(solution)
    board = [['.' for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(solution):
        board[row][col] = 'Q'
    return '\n'.join([' '.join(row) for row in board])


if __name__ == "__main__":
    solution = genetic_algorithm()
    print(print_board(solution))