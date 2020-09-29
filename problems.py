import itertools
import json

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
    complexity = "unsolvable"
  elif "111" in constrSet or "222" in constrSet:
    complexity = "Θ(1)"
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
  allProblems = []
  for L in range(0, len(constraints)+1):
    combinations = itertools.combinations(constraints, L)
    combinations = list(map(lambda x: set(x), combinations))

    for subset in combinations:
      prunedSubset = pruneSet(subset)
      ismr = getIsomorphism(prunedSubset)
      if not prunedSubset in allProblems and not ismr in allProblems:
        allProblems.append(prunedSubset)

  print("In total: %s problems" % len(allProblems))

  with open('./problems/2labels-temp.json', 'w', encoding='utf-8') as f:
    json.dump([constraintToProblem(s) for s in allProblems], f, ensure_ascii=False, indent=4)

generate()
