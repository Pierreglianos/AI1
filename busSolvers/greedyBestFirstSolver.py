from . import GreedySolver
import numpy as np

class GreedyBestFirstSolver(GreedySolver):
    def __init__(self, roads, astar, scorer):
        super().__init__(roads, astar, scorer)

    # Find the next state to develop
    def _getNextState(self, problem, currState):
        successors = list(problem.expand(currState))
        bestIdx = None
        minScore = np.inf
        for i in range(len(successors)):
            currScore = self._scorer.compute(currState, successors[i])
            if currScore < minScore:
                minScore = currScore
                bestIdx = i
        return successors[bestIdx]
