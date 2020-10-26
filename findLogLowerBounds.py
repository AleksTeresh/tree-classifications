from postprocess import postprocess

def findLogLowerBounds(problem, idx, data):
  constrs = problem["constraint"]
  lowerBound = problem["lower-bound"]

  if lowerBound == "":
    children = [x[0] + x[2] for x in constrs]
    if len(children) == len(set(children)): # children uniquely determnine parents
      print(constrs)
      data[idx]["lower-bound"] = "Ω(log n)"
      return 1

  return 0

if __name__ == "__main__":
  postprocess(findLogLowerBounds)
