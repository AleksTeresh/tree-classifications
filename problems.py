import itertools
import json

UNSOLVABLE = "unsolvable"
CONSTANT = "Θ(1)"

constraints = [
  "111",
  "112",
  "212",
  "121",
  "122",
  "222"
]

def getCanonical(constr):
  return min(constr, constr[::-1])

def getIsomorphism(constrSet):
  isomorphise = lambda y: '2' if y == '1' else '1'
  canonize = lambda x: getCanonical("".join(list(map(isomorphise, x))))
  return set(map(canonize, constrSet))

def pruneSet(constrSet):
  parentLabelSet = set(map(lambda x: x[1], constrSet))
  if len(parentLabelSet) == 1:
    allowedLabel = list(parentLabelSet)[0]
    return set(filter(lambda x: x == len(x) * allowedLabel[0], constrSet))
  else:
    return constrSet

def constraintToProblem(constrSet):
  if len(constrSet) == 0:
    complexity = UNSOLVABLE
  elif "111" in constrSet or "222" in constrSet:
    complexity = CONSTANT
  else:
    complexity = ""

  return {
    "constraint": sorted(list(constrSet)),
    "upper-bound": complexity,
    "lower-bound": complexity,
    "unsolvable-count": "",
    "solvable-count": ""
  }

def generate():
  allSets = []
  for L in range(0, len(constraints)+1):
    combinations = itertools.combinations(constraints, L)
    combinations = list(map(lambda x: set(x), combinations))

    for constraintSet in combinations:
      prunedConstraintSet = pruneSet(constraintSet)
      ismr = getIsomorphism(prunedConstraintSet)
      if not prunedConstraintSet in allSets and not ismr in allSets:
        allSets.append(prunedConstraintSet)

  allProblems = [constraintToProblem(s) for s in allSets]

  print("In total: %s problems" % len(allProblems))
  print("Solvable in constant time: %s" % len([x for x in allProblems if x["upper-bound"] == CONSTANT]))
  print("Unsolvable: %s" % len([x for x in allProblems if x["upper-bound"] == UNSOLVABLE]))
  print("TBD: %s" % len([x for x in allProblems if x["upper-bound"] == ""]))
  
  with open('./problems/2labels-temp.json', 'w', encoding='utf-8') as f:
    json.dump(allProblems, f, ensure_ascii=False, indent=4)

generate()
