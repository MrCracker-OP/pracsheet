import random

def fitness(x):
    return -x**2 + 5

def create_individual():
    return random.uniform(0, 31)

def crossover(parent1, parent2):
    alpha = random.random()
    return alpha * parent1 + (1 - alpha) * parent2

def mutate(individual): 
    mutation_rate = random.uniform(1, 5)
    if random.random() < mutation_rate:
        individual += random.uniform(-1, 1)
        individual = max(0, min(31, individual))
    return individual

def tournament_selection(population, fitnesses, tournament_size=3):
    selected = random.sample(list(zip(population, fitnesses)), tournament_size)
    return max(selected, key=lambda x: x[1])[0]

def genetic_algorithm(pop_size=10, generations=100, convergence_threshold=1e-6, max_no_improvement_generations=10):
    population = [create_individual() for _ in range(pop_size)]
    best_fitness = -float('inf')
    no_improvement_generations = 0
    
    for generation in range(generations):
        fitnesses = [fitness(ind) for ind in population]
        best_individual = max(population, key=fitness)
        current_best_fitness = fitness(best_individual)

        if current_best_fitness == best_fitness:
            no_improvement_generations += 1
        else:
            no_improvement_generations = 0

        if no_improvement_generations >= max_no_improvement_generations:
            print(f"Converged early after {generation + 1} generations.")
            break
        
        best_fitness = current_best_fitness
        
        new_population = []
        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            child = crossover(parent1, parent2)
            new_population.append(mutate(child))
        
        population = new_population
        
        print(f"Generation {generation+1}: Best Fitness = {best_fitness}")

        if abs(best_fitness - 5) < convergence_threshold:
            print(f"Optimal solution reached in generation {generation + 1}.")
            break

    return best_individual

best_solution = genetic_algorithm()
print("Best Solution Found:", best_solution)
