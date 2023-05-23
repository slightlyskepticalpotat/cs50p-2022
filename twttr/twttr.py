ans = ""
text = input("Input: ")
for i in text:
    if i.lower() in "aeiou":
        pass
    else:
        ans += i
print(f"Output: {ans}")