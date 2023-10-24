import random
#TODO - Check that we don't create children with infinty length.

# 1. Order Crossover (OX)
def order_crossover(parent1, parent2):
    size = len(parent1)
    # Choose random start and end indices for the slice
    start, end = sorted(random.sample(range(size), 2))
    
    # Initialize offspring with 'None' values
    child1 = [None] * size
    child2 = [None] * size

    # Copy the sub-path from parent1 to child1 and from parent2 to child2
    child1[start:end] = parent1[start:end]
    child2[start:end] = parent2[start:end]

    # Fill the remaining positions
    for i in range(size):
        if child1[i] is None:
            for city in parent2:
                if city not in child1:
                    child1[i] = city
                    break

        if child2[i] is None:
            for city in parent1:
                if city not in child2:
                    child2[i] = city
                    break

    return child1, child2

# 2. Partially Mapped Crossover (PMX)
def pmx(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))

    child1 = [-1] * size
    child2 = [-1] * size

    # Copy the segment from parents to children
    child1[start:end] = parent1[start:end]
    child2[start:end] = parent2[start:end]

    # Create mapping for cities in the segments
    mapping = {}
    for i in range(start, end):
        mapping[parent1[i]] = parent2[i]

    # Resolve conflicts using the mapping
    for i in list(range(start)) + list(range(end, size)):
        while parent2[i] in child1:
            parent2[i] = mapping[parent2[i]]
        child1[i] = parent2[i]

        while parent1[i] in child2:
            parent1[i] = mapping[parent1[i]]
        child2[i] = parent1[i]

    return child1, child2

# 3. Cycle Crossover (CX)
def cycle_crossover(parent1, parent2):
    size = len(parent1)
    used_indices = set()
    cycles = []

    while len(used_indices) < size:
        current_index = next(i for i in range(size) if i not in used_indices)
        current_cycle = []

        while current_index not in used_indices:
            used_indices.add(current_index)
            current_cycle.append(current_index)
            current_index = parent1.index(parent2[current_index])

        cycles.append(current_cycle)

    child1, child2 = parent1.copy(), parent2.copy()
    for i in range(len(cycles)):
        if i % 2 == 0:
            child1[cycles[i]] = parent1[cycles[i]]
            child2[cycles[i]] = parent2[cycles[i]]
        else:
            child1[cycles[i]] = parent2[cycles[i]]
            child2[cycles[i]] = parent1[cycles[i]]

    return child1, child2

# You can continue with the implementations for ERX, SCX, and POS using a similar approach.
