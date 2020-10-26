import json, sys

def postprocess(fn):
  return postprocessFile(sys.argv[1], fn, True if len(sys.argv) > 2 and (sys.argv[2] == "write" or sys.argv[2] == "w") else False)

def postprocessFile(filePath, fn, updateFile):
  ctr = 0
  with open(filePath) as json_file:
    data = json.load(json_file)
    for idx, problem in enumerate(data):
      ctr += fn(problem, idx, data)

  print("Total number of updates: %s" % ctr)
  if updateFile:
    with open(filePath, 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=2)
  
  return ctr
