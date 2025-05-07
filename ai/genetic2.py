import random

# Fitness function: maximum at x = 0
def fitness(x):
    return -x**2 + 5

# Create a random individual
def create_individual():
    return random.uniform(0, 31)

# Crossover between two parents
def crossover(p1, p2):
    return (p1 + p2) / 2

# Mutate an individual
def mutate(x):
    if random.random() < 0.1:  # 10% chance
        x += random.uniform(-1, 1)
        x = max(0, min(31, x))  # keep within bounds
    return x

# Select one individual using tournament
def select(population, fitnesses):
    group = random.sample(list(zip(population, fitnesses)), 3)
    return max(group, key=lambda x: x[1])[0]

# Genetic Algorithm
def genetic_algorithm():
    population = [create_individual() for _ in range(10)]

    for generation in range(100):
        fitnesses = [fitness(x) for x in population]
        best = max(population, key=fitness)
        best_fit = fitness(best)

        print(f"Generation {generation+1}: Best Fitness = {best_fit}")

        if abs(best_fit - 5) < 1e-6:
            print(f"Optimal solution reached at generation {generation+1}")
            break

        new_population = []
        for _ in range(10):
            p1 = select(population, fitnesses)
            p2 = select(population, fitnesses)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    return best

# Run the algorithm
best = genetic_algorithm()
print("Best Solution Found:", best)
print("Fitness of Best Solution:", fitness(best))