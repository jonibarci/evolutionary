import random
from length import tsp_length
from mutation import mutation_interface


def generate_offspring(population, crossover, mutation, distance_matrix, mutation_prob, offspring_size):
    offspring = []
    for _ in range(int(offspring_size/2)):
        length1 = float('inf')
        length2 = float('inf')
        while ((length1 == float('inf')) | (length2 == float('inf'))):
            parent1, parent2 = random.choices(population, k=2)  # Randomly select two parents
            child1, child2 = crossover(parent1, parent2)                 # Apply crossover
            length1 = tsp_length(distance_matrix, child1)
            length2 = tsp_length(distance_matrix, child2)

        # Apply mutation with a given probability
        if random.random() < mutation_prob:
            child1 = mutation_interface(child1, distance_matrix, mutation)
            
        offspring.append(child1)

        # Apply mutation with a given probability
        if random.random() < mutation_prob:
            child2 = mutation_interface(child2, distance_matrix, mutation)
            
        offspring.append(child2)
    return offspring