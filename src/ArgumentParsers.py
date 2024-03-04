import sys
import getopt

x, y = getopt.getopt(sys.argv[1:], "f:m:", ['fileName', 'message'])

print(x)
print(y)

# Command
# python ArgumentParsers.py -f "Collect" -m "Build a series of Evidences" "Optional Parameter"