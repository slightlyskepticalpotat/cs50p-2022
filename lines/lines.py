import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

name = sys.argv[1]
if name[-3:] != ".py":
    sys.exit("Not a Python file")

lines = 0
try:
    with open(sys.argv[1], "r") as file:
        for line in file.readlines():
            if line.strip() == "":
                continue
            if line.strip()[0] == "#":
                continue
            if line.strip()[:3] == "'''":
                continue
            lines += 1
    print(lines)
except:
    sys.exit("File does not exist")