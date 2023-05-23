text = input("camelCase: ").strip()
ans = ""
for i in text:
    if i.isupper():
        ans += ("_"+i.lower())
    else:
        ans += i
print(f"snake_case: {ans}")
