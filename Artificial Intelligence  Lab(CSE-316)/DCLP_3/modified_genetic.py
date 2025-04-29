import random
t=0
g=0

def calculate_fitness(individual):
    global t
    sum_first_two = individual[0] + individual[1]
    if sum_first_two > t:
        return 0
    else:
        return t - abs(t - sum_first_two)

def get_fittest_individuals(population):
    sorted_pop = sorted(population, key=calculate_fitness, reverse=True)
    return sorted_pop[0], sorted_pop[1]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    mutation_point = random.randint(0, len(individual) - 1)
    individual[mutation_point] = random.randint(0, 9)
    return individual

def get_least_fittest_index(population):
    min_fitness = float('inf')
    min_index = 0
    for i in range(len(population)):
        fitness = calculate_fitness(population[i])
        if fitness < min_fitness:
            min_fitness = fitness
            min_index = i
    return min_index

def generate_random_population(size, gene_length):
    population = []
    for _ in range(size):
        individual = [random.randint(0, 9) for _ in range(gene_length)]
        population.append(individual)
    return population

def main():
    global t
    population_size = 10
    t=int(input("Insert the target: "))
    gene_length = int(input("Insert value of K: "))
    global g
    g=gene_length
    population = generate_random_population(population_size, gene_length)

    generation = 0
    fittest_score = calculate_fitness(max(population, key=calculate_fitness))
    print(f"Generation: {generation} Fittest: {fittest_score}")

    while fittest_score != t:
        generation += 1
        parent1, parent2 = get_fittest_individuals(population)
        child1, child2 = crossover(parent1[:], parent2[:])
        child1 = mutate(child1[:])
        child2 = mutate(child2[:])
        fittest_child = child1 if calculate_fitness(child1) > calculate_fitness(child2) else child2
        least_fittest_idx = get_least_fittest_index(population)
        population[least_fittest_idx] = fittest_child
        fittest_score = calculate_fitness(max(population, key=calculate_fitness))
        print(f"Generation: {generation} Fittest: {fittest_score}")

    fittest_individual = max(population, key=calculate_fitness)
    print(f"\nSolution found in generation {generation}")
    print(f"Fitness: {calculate_fitness(fittest_individual)}")
    print("Genes: ", end="")
    for gene in fittest_individual:
        print(gene, end=" ")
    print()

if __name__ == "__main__":
    main()