from decider.log_decider import is_log_solvable
from decider.log_star_decider import is_log_star_solvable
from util import complexities

def findContradictionsByDecider(problem, idx, data):
  constraints = set(problem["constraint"])
  lowerBound = problem["lower-bound"]
  upperBound = problem["upper-bound"]

  if upperBound != "unsolvable" or lowerBound != "unsolvable":
    # decidedUpperBound = upperBound
    # decidedLowerBound = lowerBound

    if is_log_star_solvable(constraints) and lowerBound != "" and complexities.index(lowerBound) > complexities.index("(log* n)"):
      print(constraints, "lower-bound", lowerBound, "but log* solvable")
      return 1
    elif not is_log_star_solvable(constraints) and upperBound != "" and complexities.index(upperBound) <= complexities.index("(log* n)"):
      print(constraints, "upper-bound", upperBound, "but NOT log* solvable")
      return 1

    if is_log_solvable(constraints) and lowerBound != "" and complexities.index(lowerBound) > complexities.index("(log n)"):
      print(constraints, "lower-bound", lowerBound, "but log solvable")
      return 1
    elif not is_log_solvable(constraints) and upperBound != "" and complexities.index(upperBound) <= complexities.index("(log n)"):
      print(constraints, "upper-bound", upperBound, "but NOT log solvable")
      return 1

  return 0
