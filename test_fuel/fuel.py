def main():
    while True:
        try:
            a = input("Fraction: ")
            num = convert(a)
            print(gauge(num))
        except Exception as e:
            pass
        else:
            break

def convert(fraction):
    a, b = map(int, fraction.split("/"))
    val = a/b*100
    val = round(val)
    return val

def gauge(val):
    if val > 100:
        raise
    if val >= 99:
        return "F"
    elif val <= 1:
        return "E"
    else:
        return f"{val}%"

if __name__ == "__main__":
    main()
