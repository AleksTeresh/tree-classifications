import sys
import json
from util import getCanonical, flatMap

def findSolvableByCyclePathClassifier():
  filePath = sys.argv[1]
  with open(filePath) as json_file:
    ctr = 0
    data = json.load(json_file)
    for idx, problem in enumerate(data):
      problemId = problem["id"]
      constrs = problem["constraint"]
      lowerBound = problem["lower-bound"]
      upperBound = problem["upper-bound"]

      if lowerBound != "" and upperBound != "":
        continue

      # TODO: refactor the mess below
      parentChildPairs = sorted(list(set(flatMap(lambda x: [x[0:2][::-1], x[1:]], constrs))))
      lastParent = ""
      childrenOfTheSameParent = []
      canUse = True
      ctr = 0
      
      for pair in parentChildPairs:
        p = pair[0]
        c = pair[1]
        if (c + p + c) in constrs:
          if lastParent == p:
            if len([x for x in childrenOfTheSameParent if not (getCanonical(x + p + c) in constrs)]) == 0:
              ctr += 1
              ctr += len(childrenOfTheSameParent)
              childrenOfTheSameParent.append(c)
            else:
              canUse = False
              break
          else:
            lastParent = p
            childrenOfTheSameParent = [c]
            ctr += 1
        else:
          canUse = False
          break
        
      if canUse and ctr == len(constrs):
        print(constrs, problemId)
  
if __name__ == "__main__":
   findSolvableByCyclePathClassifier()
