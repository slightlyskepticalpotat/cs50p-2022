def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")

def shorten(word):
    ans = ""
    for i in word:
        if i.lower() in "aeiou":
            pass
        else:
            ans += i
    return ans

if __name__ == "__main__":
    main()
