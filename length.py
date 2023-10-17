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

# Example usage
if __name__ == "__main__":
    matrix = [[0, 1, 2, 3], [1, 0, 4, 5], [2, 4, 0, 6], [3, 5, 6, 0]]
    best_permutation, best_length = solve_tsp(matrix)
    print("Best permutation:", best_permutation)
    print("Best length:", best_length)