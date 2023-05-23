import sys, csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

name = sys.argv[1]
students = []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"first": row["name"].split(",")[1][1:], "last": row["name"].split(",")[0], "house": row["house"]})
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)
except:
    sys.exit(f"Could not read {sys.argv[1]}")