from util import getCanonical
from postprocess import postprocess

def findLowerBoundsByReplacement(problem, idx, data):
  constrs = problem["constraint"]
  lowerBound = problem["lower-bound"]

  if lowerBound == "":
    newConstr1 = set([getCanonical(x.replace("3", "1")) for x in constrs])
    newConstr2 = set([getCanonical(x.replace("2", "1")) for x in constrs])
    newConstr3 = set([getCanonical(x.replace("3", "2")) for x in constrs])
    newConstrs = [newConstr1, newConstr2, newConstr3]

    prevProblems = data[:idx]
    for prevProblem in prevProblems:
      prevConstrs = set(prevProblem["constraint"])
      prevLowerBound = prevProblem["lower-bound"]

      if prevLowerBound != "" and prevLowerBound != "Θ(1)" and prevConstrs in newConstrs:
        data[idx]["lower-bound"] = prevLowerBound
        print(constrs, prevLowerBound)
        return 1
  
  return 0

if __name__ == "__main__":
  postprocess(findLowerBoundsByReplacement)
