import sys
from .classify import classify
from .generateProblems import generate
from .statistics import getStatistics

if __name__ == "__main__":
  command = sys.argv[1]
  args = sys.argv[2:]

  if command == 'generate':
    generate(int(args[0]))
  elif command == 'classify':
    classify(args[0], len(args) > 1 and (args[1] == "--write" or args[1] == "-w"))
  elif command == 'statistics':
    getStatistics(args[0])
  else:
    print('The first argument needs to be the command. One of "generate", "classify", "statistics"')
