import sys, json

def getStatistics():
  filePath = sys.argv[1]

  with open(filePath) as json_file:
    data = json.load(json_file)

    lowerBoundConstant = 0
    upperBoundConstant = 0
    constSolvable = 0

    lowerBoundLog = 0
    upperBoundLog = 0
    logSolvable = 0

    lowerBoundLinear = 0
    upperBoundLinear = 0
    linearSolvable = 0

    unsolvable = 0

    for p in data:
      lowerBound = p["lower-bound"]
      upperBound = p["upper-bound"]

      if "1" in lowerBound:
        lowerBoundConstant += 1
      if "1" in upperBound:
        upperBoundConstant += 1
      if "1" in lowerBound and "1" in upperBound:
        constSolvable += 1

      if "log n" in lowerBound:
        lowerBoundLog += 1
      if "log n" in upperBound:
        upperBoundLog += 1
      if "log n" in lowerBound and "log n" in upperBound:
        logSolvable += 1

      if "(n)" in lowerBound:
        lowerBoundLinear += 1
      if "(n)" in upperBound:
        upperBoundLinear += 1
      if "(n)" in lowerBound and "(n)" in upperBound:
        linearSolvable += 1

      if "unsolvable" in lowerBound:
        unsolvable += 1

    totalSize = len(data)

    print("In total: %s problems" % totalSize)
    print("Solvable in constant time: %s " % constSolvable)
    print("Solvable in log time: %s " % logSolvable)
    print("Solvable in linear time: %s " % linearSolvable)
    print("Unsolvable: %s" % unsolvable)
    print("TBD: %s" % (totalSize - unsolvable - constSolvable - logSolvable - linearSolvable))
    print()

    print("Lower bounds")
    print("Constant time: %s " % lowerBoundConstant)
    print("Log time: %s " % lowerBoundLog)
    print("Linear time: %s " % lowerBoundLinear)
    print("TBD: %s" % (totalSize - unsolvable - lowerBoundConstant - lowerBoundLog - lowerBoundLinear))
    print()

    print("Upper bounds")
    print("Constant time: %s " % upperBoundConstant)
    print("Log time: %s " % upperBoundLog)
    print("Linear time: %s " % upperBoundLinear)
    print("TBD: %s" % (totalSize - unsolvable - upperBoundConstant - upperBoundLog - upperBoundLinear))

if __name__ == "__main__":
  getStatistics()