shopping = {}

while True:
    try:
        item = input().upper()
        if item in shopping:
            shopping[item] += 1
        else:
            shopping[item] = 1
    except:
        break
for i in sorted(shopping.keys()):
    print(f"{shopping[i]} {i}")