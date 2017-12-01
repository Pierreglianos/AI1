from . import GreedySolver
import numpy as np

class GreedyStochasticSolver(GreedySolver):
    _TEMPERATURE_DECAY_FACTOR = None
    _INITIAL_TEMPERATURE = None
    _N = None

    def __init__(self, roads, astar, scoarrer, initialTemperature, temperatureDecayFactor, topNumToConsider):
        super().__init__(roads, astar, scorer)

        self._INITIAL_TEMPERATURE = initialTemperature
        self._TEMPERATURE_DECAY_FACTOR = temperatureDecayFactor
        self._N = topNumToConsider

    def _getSuccessorsProbabilities(self, currState, successors):
        # Get the scores
        X = np.array([self._scorer.compute(currState, target) for target in successors])


        # Initialize an all-zeros vector for the distribution
        P = np.zeros((len(successors),))

        # TODO: Fill the distribution in P as explained in the instructions.
        # TODO : No changes in the rest of the code are needed
        idxList = self._getMinN(X)
        alpha = min(X);
        denom = np.sum(np.power(X[idxList]/alpha, -1/self.T))
        for i in idxList:
            P[i] = [np.power(X[i]/alpha, -1/self.T)/denom]

        # Update the temperature
        self.T *= self._TEMERATURE_DECAY_FACTOR

        return P

    # Find the next state to develop
    def _getNextState(self, problem, currState):
        successors = list(problem.expand(currState))
        P = self._getSuccessorsProbabilities(currState, successors)

        # TODO : Choose the next state stochastically according to the calculated distribution.
        # You should look for a suitable function in numpy.random.
        nextIdx = None


        return successors[nextIdx]

    # Find the N smallest values in the array, returns these indices in a list
    def _getMinN(self, arr):
        indexList = []
        newArr = np.copy(arr)
        listSize = min(self._N, len(newArr))
        for i in range(listSize):
            minIndex = np.argmin(newArr)
            indexList.append(minIndex)
            newArr[minIndex] = np.inf
        return indexList

    # Override the base solve method to initialize the temperature
    def solve(self, initialState):
        self.T = self._INITIAL_TEMPERATURE
        return super().solve(initialState)
