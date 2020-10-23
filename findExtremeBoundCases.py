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
      upperBound = problem["upper-bound"]

      if "(n)" in lowerBound and upperBound == "":
        print(constrs, "Θ(n)")
        data[idx]["upper-bound"] = lowerBound
      elif "(1)" in upperBound and lowerBound == "":
        print(constrs, "Θ(1)")
        data[idx]["lower-bound"] = upperBound
            
  print(ctr)
  with open(filePath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
   findLogLowerBounds()
