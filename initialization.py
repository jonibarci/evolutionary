import random

# 1. Random Initialization
def random_initialization(num_individuals, cities):
    population = []
    for _ in range(num_individuals):
        individual = cities.copy()
        random.shuffle(individual)
        population.append(individual)
    return population

# 2. Nearest Neighbor Initialization
def nearest_neighbor_initialization(num_individuals, distance_matrix):
    def nearest_city(current_city, unvisited):
        return min(unvisited, key=lambda city: distance_matrix[current_city][city])

    population = []
    for _ in range(num_individuals):
        start_city = random.choice(range(len(distance_matrix)))
        unvisited = set(range(len(distance_matrix)))
        unvisited.remove(start_city)
        individual = [start_city]
        
        while unvisited:
            next_city = nearest_city(individual[-1], unvisited)
            individual.append(next_city)
            unvisited.remove(next_city)
            
        population.append(individual)
    
    return population

# If you're considering Cluster-Based Initialization, it would require a clustering algorithm (like K-means) 
# and then solving TSP for each cluster, potentially using a simpler method or heuristic.
