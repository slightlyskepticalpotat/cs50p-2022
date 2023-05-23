def main():
    text = input("What time is it? ")
    x = convert(text)
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")

def convert(time):
    a, b = map(float, time.split(":"))
    return a + b/60

if __name__ == "__main__":
    main()
