import sys
import json
from util import getCanonical, flatMap

def findLogLowerBounds():
  filePath = sys.argv[1]
  with open(filePath) as json_file:
    ctr = 0
    data = json.load(json_file)
    for idx, problem in enumerate(data):
      constrs = problem["constraint"]
      lowerBound = problem["lower-bound"]

      if lowerBound == "":
        children = [x[0] + x[2] for x in constrs]
        if len(children) == len(set(children)): # children uniquely determnine parents
          ctr += 1
          print(constrs)
          data[idx]["lower-bound"] = "Ω(log n)"
          

        
  print(ctr)
  with open(filePath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
   findLogLowerBounds()
