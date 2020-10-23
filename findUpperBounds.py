import sys
import json
from util import getCanonical

def findUpperBounds():
  filePath = sys.argv[1]
  with open(filePath) as json_file:
    ctr = 0
    data = json.load(json_file)
    for idx, problem in enumerate(data):
      constrs = set(problem["constraint"])
      upperBound = problem["upper-bound"]

      if upperBound == "":
        prevProblems = data[:idx]
        for prevProblem in prevProblems:
          prevConstrs = set(prevProblem["constraint"])
          prevUpperBound = prevProblem["upper-bound"]

          if prevUpperBound != "" and prevUpperBound != "O(n)" and prevUpperBound != "Θ(n)" and prevUpperBound != "unsolvable" and prevConstrs.issubset(constrs):
            data[idx]["upper-bound"] = prevUpperBound
            print(constrs, prevUpperBound)
            ctr += 1
            break

    print("Total number of updated upper bounds: %s" % ctr)

  with open(filePath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
   findUpperBounds()
