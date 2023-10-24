import Reporter
import numpy as np
from length import tsp_length, lambda_plus_mu_elimination
from crossover import pmx
from mutation import swap_mutation

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

		parent1 = np.array([1,2,0,3,4,5,8,6,7])
		parent2 = np.array([8,6,7,1,2,5,0,4,3])
		population = [parent1, parent2]

		# child1, child2 = pmx(parent1, parent2)
		# print(child1)
		# print(child2)

		lambda_plus_mu_elimination(population=population, lambda_offspring=1, mu_parents=4, distance_matrix=distanceMatrix, crossover=pmx, mutation=swap_mutation, mutation_prob=0.1)

		# Your code here.
		yourConvergenceTestsHere = True
		while( yourConvergenceTestsHere ):
			meanObjective = 0.0
			bestObjective = 0.0
			bestSolution = np.array([1,2,3,4,5])


			# Your code here.
			for i in range (10):
				break

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