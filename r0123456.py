import Reporter
import numpy as np
from length import tsp_length, lambda_plus_mu_elimination
from crossover import pmx
from mutation import swap_mutation
from initialization import random_initialization

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

		permutationSize = len(distanceMatrix[0])
		populationSize = 100
		iterations = 1000

		# Your code here.
		yourConvergenceTestsHere = True
		while( yourConvergenceTestsHere ):
			meanObjective = 0.0
			bestObjective = 0.0
			bestSolution = np.array([1,2,3,4,5])
			population = random_initialization(populationSize, permutationSize, distanceMatrix)

			# Your code here.
			for i in range (iterations):
				population = lambda_plus_mu_elimination(population=population, lambda_offspring=15, mu_parents=populationSize, distance_matrix=distanceMatrix, crossover=pmx, mutation=swap_mutation, mutation_prob=0.25)

				permutationScores = []
				for permutation in population:
					permutationScores.append(tsp_length(distanceMatrix, permutation))

				meanObjective = sum(permutationScores)/populationSize
				bestObjective = min(permutationScores)
				print(population)
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