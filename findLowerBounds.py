import sys
import json
from util import getCanonical

def finLowerBounds():
  filePath = sys.argv[1]
  with open(filePath) as json_file:
    ctr = 0
    data = json.load(json_file)
    for idx, problem in enumerate(data):
      constrs = set(problem["constraint"])
      lowerBound = problem["lower-bound"]

      if lowerBound == "":
        prevProblems = data[idx+1:]
        for prevProblem in prevProblems:
          prevConstrs = set(prevProblem["constraint"])
          prevLowerBound = prevProblem["lower-bound"]

          if prevLowerBound != "" and prevLowerBound != "O(1)" and prevLowerBound != "Θ(1)" and prevLowerBound != "unsolvable" and constrs.issubset(prevConstrs):
            data[idx]["lower-bound"] = prevLowerBound
            print(constrs, prevConstrs, prevLowerBound)
            ctr += 1
            break

    print("Total number of updated lower bounds: %s" % ctr)

  with open(filePath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
   finLowerBounds()
