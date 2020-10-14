import sys
import json
from util import getCanonical

def postprocessLowerBounds():
  filePath = sys.argv[1]
  with open(filePath) as json_file:
    ctr = 0
    data = json.load(json_file)
    for idx, problem in enumerate(data):
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
            ctr += 1
            break

    print("Total number of updated lower bounds: %s" % ctr)

  with open(filePath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
   postprocessLowerBounds()
