import sys
import itertools
import json

UNSOLVABLE = "unsolvable"
CONSTANT = "Θ(1)"

def getCanonical(constr):
  return min(constr, constr[::-1])

def isomorphise1(y):
  if y == '1':
    return '2'
  elif y == '2':
    return '1'
  else:
    return y
def isomorphise2(y):
  if y == '1':
    return '3'
  elif y == '3':
    return '1'
  else:
    return y
def isomorphise3(y):
  if y == '2':
    return '3'
  elif y == '3':
    return '2'
  else:
    return y
def isomorphise4(y):
  if y == '1':
    return '2'
  elif y == '2':
    return '3'
  else:
    return '1'
def isomorphise5(y):
  if y == '1':
    return '3'
  elif y == '3':
    return '2'
  else:
    return '1'

def canonize(isomorphize):
  return lambda x: getCanonical("".join(list(map(isomorphize, x))))

def getIsomorphism(constrSet, colorCount):
  if colorCount == 2:
    return [constrSet, set(map(canonize(isomorphise1), constrSet))]
  elif colorCount == 3:
    return [
      constrSet,
      set(map(canonize(isomorphise1), constrSet)),
      set(map(canonize(isomorphise2), constrSet)),
      set(map(canonize(isomorphise3), constrSet)),
      set(map(canonize(isomorphise4), constrSet)),
      set(map(canonize(isomorphise5), constrSet)),
    ]


def pruneSet(constrSet):
  parentLabelSet = set(map(lambda x: x[1], constrSet))
  return set(filter(lambda x: set(x) <= parentLabelSet, constrSet))

def constraintToProblem(constrSet):
  if "111" in constrSet or "222" in constrSet or "333" in constrSet or ("112" in constrSet and "122" in constrSet):
    complexity = CONSTANT
  elif len(constrSet) == 0:
    complexity = UNSOLVABLE
  else:
    complexity = ""

  return {
    "constraint": sorted(list(constrSet)),
    "upper-bound": complexity,
    "lower-bound": complexity,
    "unsolvable-count": "",
    "solvable-count": ""
  }

def getConstraints(colorCount):
  colorPalete = [str(x) for x in list(range(1, colorCount + 1))]
  prod = list(itertools.product(colorPalete, repeat=3))
  return [getCanonical("".join(list(x))) for i, x in enumerate(prod) if not getCanonical(x) in prod[:i]]

def generate():
  colorCount = int(sys.argv[1])
  constraints = getConstraints(colorCount)

  allSets = []
  for L in range(0, len(constraints)+1):
  # for L in range(0, 3):
    combinations = itertools.combinations(constraints, L)
    combinations = list(map(lambda x: set(x), combinations))
    print(L)

    for constraintSet in combinations:
      prunedConstraintSet = constraintSet
      for _ in range(colorCount-1):
        prunedConstraintSet = pruneSet(prunedConstraintSet)
      print(constraintSet, prunedConstraintSet)
      ismrs = getIsomorphism(prunedConstraintSet, colorCount)
      if len([1 for ismr in ismrs if ismr in allSets]) == 0:
        allSets.append(prunedConstraintSet)

  allProblems = [constraintToProblem(s) for s in allSets]

  print("In total: %s problems" % len(allProblems))
  print("Solvable in constant time: %s" % len([x for x in allProblems if x["upper-bound"] == CONSTANT]))
  print("Unsolvable: %s" % len([x for x in allProblems if x["upper-bound"] == UNSOLVABLE]))
  print("TBD: %s" % len([x for x in allProblems if x["upper-bound"] == ""]))
  
  with open('./problems/problems-temp.json', 'w', encoding='utf-8') as f:
    json.dump(allProblems, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
   generate()
