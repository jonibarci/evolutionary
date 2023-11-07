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


def tsp_fitness(route, distance_matrix):
    """Compute the total distance of the route."""
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route)-1)) + distance_matrix[route[-1]][route[0]]