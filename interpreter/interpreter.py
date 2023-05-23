a, b, c = input("Expression: ").split()
a, c = float(a), float(c)
x = eval(str(a)+b+str(c))
print(f"{x:.1f}")