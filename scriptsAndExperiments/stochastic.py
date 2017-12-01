from consts import Consts
from astar import AStar
from ways import load_map_from_csv
from busSolvers import GreedyBestFirstSolver, GreedyStochasticSolver
from problems import BusProblem
from costs import L2DistanceCost
from heuristics import L2DistanceHeuristic
import numpy as np

REPEATS = 150

# Load the files
roads = load_map_from_csv(Consts.getDataFilePath("israel.csv"))
prob = BusProblem.load(Consts.getDataFilePath("HAIFA_100.in"))

mapAstar = AStar(L2DistanceHeuristic(), shouldCache=True)

scorer = L2DistanceCost(roads)

# Run the greedy solver
pickingPath = GreedyBestFirstSolver(roads, mapAstar, scorer).solve(prob)
greedyDistance = pickingPath.getDistance() / 1000
print("Greedy solution: {:.2f}km".format(greedyDistance))

# Run the stochastic solver #REPATS times
solver = GreedyStochasticSolver(roads, mapAstar, scorer,
                                Consts.STOCH_INITIAL_TEMPERATURE,
                                Consts.STOCH_TEMPERATURE_DECAY_FUNCTION,
                                Consts.STOCH_TOP_SCORES_TO_CONSIDER)
results = np.zeros((REPEATS,))
print("Stochastic repeats:")
for i in range(REPEATS):
    #print("{}..".format(i+1), end=" ", flush=True)
    currRes = solver.solve(prob).getDistance() / 1000
    if i == 0 or currRes < results[i - 1]:
        results[i] = currRes
    else:
        results[i] = results[i - 1]
    print("{}..result {}".format(i + 1, results[i]))

print("\nDone!")

# TODO : Part1 - Plot the diagram required in the instructions
from matplotlib import pyplot as plt
#plt.axis([0, REPEATS + 5, 0, 2000])
plt.title("Stochastic solver results")
plt.ylabel("Distance")
plt.xlabel("Number of iteration")
plt.grid()
plt.plot(results)
plt.show(block=False)
plt.waitforbuttonpress()



# TODO : Part2 - Remove the exit and perform the t-test
#raise NotImplementedError