from . import Heuristic
from costs.L2DistanceCost import compute

# Use the L2 aerial distance (in meters)
class L2DistanceHeuristic(Heuristic):
    def estimate(self, problem, state):
        # TODO : Return the correct distance
        return compute(state, problem.target)

