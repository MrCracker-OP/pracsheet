import random

# Constants
POP_SIZE = 10
GENOME_LENGTH = 5
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7

# Fitness function
def fitness(x):
    return -x**2 + 5

# Create a random individual
def create_individual():
    return [random.randint(0, 1) for _ in range(GENOME_LENGTH)]

# Decode binary genome to integer
def decode_genome(genome):
    return int("".join(map(str, genome)), 2)

# Mutation: bit-flip with probability
def mutate(individual):
    mutated = individual[:]
    for i in range(len(mutated)):
        if random.random() < MUTATION_RATE:
            mutated[i] = 1 - mutated[i]
            print(f"    Mutation occurred at bit {i}")
    return mutated

# Crossover: one-point with probability
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, GENOME_LENGTH - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        print(f"    Crossover point: {point}")
    else:
        child1, child2 = parent1[:], parent2[:]
        print("    No crossover occurred")
    return child1, child2

# Main function: One generation
def genetic_algorithm_one_iteration():
    population = [create_individual() for _ in range(POP_SIZE)]

    print("--- Initial Population ---")
    for i, ind in enumerate(population):
        x = decode_genome(ind)
        print(f"  {i}: {ind} -> x={x}, fitness={fitness(x)}")

    new_population = []
    random.shuffle(population)  # Random mating

    for i in range(0, POP_SIZE, 2):
        parent1 = population[i]
        parent2 = population[i+1]
        print(f"\nMating pair: {parent1} x {parent2}")
        child1, child2 = crossover(parent1, parent2)

        print("  Child 1 before mutation:", child1)
        child1 = mutate(child1)
        print("  Child 1 after mutation: ", child1)

        print("  Child 2 before mutation:", child2)
        child2 = mutate(child2)
        print("  Child 2 after mutation: ", child2)

        new_population.extend([child1, child2])

    print("\n--- New Population ---")
    for i, ind in enumerate(new_population):
        x = decode_genome(ind)
        print(f"  {i}: {ind} -> x={x}, fitness={fitness(x)}")

    best_individual = max(new_population, key=lambda ind: fitness(decode_genome(ind)))
    best_x = decode_genome(best_individual)
    print(f"\nBest individual: {best_individual} -> x={best_x}, fitness={fitness(best_x)}")

genetic_algorithm_one_iteration()