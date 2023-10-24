import random

def tsp_length(matrix, permutation):
    """
    Calculate the length of the cycle for a given permutation in TSP.
    
    Args:
    - matrix (list of list of ints): The nonsymmetric distance matrix.
    - permutation (list of ints): The cyclic permutation (a permutation of vertices).
    
    Returns:
    - int: The length of the cycle for the given permutation.
    """
    n = len(permutation)
    total_distance = 0
    
    for i in range(n - 1):
        total_distance += matrix[permutation[i]][permutation[i + 1]]
    
    # Adding the distance from the last city to the first one to complete the cycle.
    total_distance += matrix[permutation[n - 1]][permutation[0]]
    
    return total_distance

# For optimization, you'd typically use a library or framework like genetic algorithms or other optimization methods.
# Here's a naive approach just to demonstrate how you'd use the tsp_length function.
def solve_tsp(matrix):
    """
    Naive TSP solver. Returns the shortest path found after checking all permutations.
    
    Args:
    - matrix (list of list of ints): The nonsymmetric distance matrix.
    
    Returns:
    - tuple: The best permutation and its length.
    """
    import itertools
    
    n = len(matrix)
    best_permutation = None
    best_length = float('inf')
    
    # Check all possible permutations
    for perm in itertools.permutations(range(n)):
        current_length = tsp_length(matrix, perm)
        if current_length < best_length:
            best_length = current_length
            best_permutation = perm
    
    return best_permutation, best_length


def tsp_fitness(route, distance_matrix):
    """Compute the total distance of the route."""
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1)) + distance_matrix[route[-1]][route[0]]

def lambda_plus_mu_elimination(population, lambda_offspring, mu_parents, distance_matrix, crossover, mutation, mutation_prob):
    """Apply λ+μ elimination strategy."""
    offspring = []
    
    # Generate λ offspring
    for _ in range(lambda_offspring):
        length1 = float('inf')
        length2 = float('inf')
        while ((length1 == float('inf')) | (length2 == float('inf'))):
            parent1, parent2 = random.choices(population, k=2)  # Randomly select two parents
            child1, child2 = crossover(parent1, parent2)                 # Apply crossover
            length1 = tsp_length(distance_matrix, child1)
            length2 = tsp_length(distance_matrix, child2)

        # Apply mutation with a given probability
        if random.random() < mutation_prob:
            child1 = mutation(child1)
            
        offspring.append(child1)

        # Apply mutation with a given probability
        if random.random() < mutation_prob:
            child2 = mutation(child2)
            
        offspring.append(child2)

    # Combine parents and offspring
    combined_population = population + offspring
    
    # Sort by fitness
    sorted_population = sorted(combined_population, key=lambda x: tsp_fitness(x, distance_matrix))
    
    # Select top μ individuals
    next_generation = sorted_population[:mu_parents]
    
    return next_generation

def k_tournament_selection(population, k, tournament_size):
    selected = []
    for i in range(k):
        tournament = random.sample(population, tournament_size)
        winner = max(tournament, key=lambda x: x.fitness)
        selected.append(winner)
    return selected