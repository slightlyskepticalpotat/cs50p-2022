names = []
while True:
    try:
        names.append(input())
    except:
        break

if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
else:
    print("Adieu, adieu, to ", end = "")
    print(", ".join(names[:-1]), end = "")
    print(f", and {names[-1]}")