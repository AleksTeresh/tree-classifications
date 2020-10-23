import json, sys

filePath = sys.argv[1]
ctr = 0
with open(filePath) as json_file:
  ctr = 0
  data = json.load(json_file)
  for idx, problem in enumerate(data):
    constrs = set(problem["constraint"])
    lowerBound = problem["lower-bound"]
    upperBound = problem["upper-bound"]

    if lowerBound != "" and upperBound != "":
      continue

    prevProblems = data[idx+1:]
    for prevProblem in prevProblems:
      prevConstrs = set(prevProblem["constraint"])
      prevLowerBound = prevProblem["lower-bound"]
      prevUpperBound = prevProblem["upper-bound"]

      if prevLowerBound != "" and prevUpperBound != "":
        for c in prevConstrs:
          prevConstrs.remove(c)
          if constrs == prevConstrs and c != c[0] * len(c):
            prevConstrs.add(c)
            print(constrs, prevConstrs, c, prevProblem["lower-bound"], prevProblem["upper-bound"])
            break

          prevConstrs.add(c)
