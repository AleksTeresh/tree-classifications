from postprocess import postprocess

def getMinimal(problem, idx, data):
  constrs = set(problem["constraint"])
  lowerBound = problem["lower-bound"]
  upperBound = problem["upper-bound"]

  if lowerBound != "" and upperBound != "":
    return 0

  prevProblems = data[:idx]
  for prevProblem in prevProblems:
    prevConstrs = set(prevProblem["constraint"])
    prevLowerBound = prevProblem["lower-bound"]
    prevUpperBound = prevProblem["upper-bound"]

    if prevLowerBound != "" and prevUpperBound != "":
      for c in constrs:
        constrs.remove(c)
        if constrs == prevConstrs:
          constrs.add(c)
          print(constrs, prevConstrs, c, prevProblem["lower-bound"], prevProblem["upper-bound"], problem["id"])
          break  

        constrs.add(c)

  return 0

if __name__ == "__main__":
  postprocess(getMinimal)