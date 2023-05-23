import sys, csv, tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
name = sys.argv[1]
if name[-4:] != ".csv":
    sys.exit("Not a CSV file")

pizzas = []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            pizzas.append(row)
        print(tabulate.tabulate(pizzas[1:], pizzas[0], tablefmt="grid"))
except Exception as e:
    print(e)
    sys.exit("File does not exist")