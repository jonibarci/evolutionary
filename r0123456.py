import Reporter
import numpy as np
from length import tsp_length, tsp_fitness
from crossover import cycle_crossover, order_crossover, pmx
from mutation import inversion_mutation
from initialization import random_initialization, nearest_neighbor_initialization, greedy_initialization, random_greedy_initialization
from offspring import generate_offspring
from selection import k_tournament_selection

# Modify the class name to match your student number.
class r0123456:

	def __init__(self):
		self.reporter = Reporter.Reporter(self.__class__.__name__)

	# The evolutionary algorithm's main loop
	def optimize(self, filename):
		# Read distance matrix from file.		
		file = open(filename)
		distanceMatrix = np.loadtxt(file, delimiter=",")
		file.close()

		# parameters
		permutationSize = len(distanceMatrix[0])
		populationSize = 100
		offspringSize = int(0.6*populationSize)
		iterations = 500

		# Your code here.
		yourConvergenceTestsHere = True
		while( yourConvergenceTestsHere ):
			meanObjective = 0.0
			bestObjective = 0.0
			bestSolution = np.array([1,2,3,4,5])

			# population initializations
			population = random_initialization(populationSize, permutationSize, distanceMatrix)
			# population = nearest_neighbor_initialization(populationSize, distanceMatrix)
			# population = greedy_initialization(populationSize, distanceMatrix)
			# population = random_greedy_initialization(populationSize, distanceMatrix)


			# Your code here.
			for i in range (iterations):
				print(f"iterations {i}")

				# selection
				selection = k_tournament_selection(population=population, k=offspringSize, tournament_size=3, distance_matrix=distanceMatrix)

				# crossover + mutation (children)
				offspring = generate_offspring(population=selection, crossover=order_crossover, mutation=inversion_mutation, mutation_prob=0.05, offspring_size=offspringSize, distance_matrix=distanceMatrix)
				combined_population = offspring + population

				# elimination
				sorted_population = sorted(combined_population, key=lambda x: tsp_fitness(x, distanceMatrix))
				population = sorted_population[:populationSize]


				# reporting
				permutationScores = []
				for permutation in population:
					permutationScores.append(tsp_length(distanceMatrix, permutation))

				meanObjective = sum(permutationScores)/populationSize
				bestObjective = min(permutationScores)
				bestSolution = np.array(population[0])

				# Call the reporter with:
				#  - the mean objective function value of the population
				#  - the best objective function value of the population
				#  - a 1D numpy array in the cycle notation containing the best solution 
				#    with city numbering starting from 0
				timeLeft = self.reporter.report(meanObjective, bestObjective, bestSolution)
				if timeLeft < 0:
					break

			yourConvergenceTestsHere = False
		# Your code here.
		return 0
	
#program
solver = r0123456()
solver.optimize("matrices/tour50.csv")