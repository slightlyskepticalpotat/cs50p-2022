import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"(\d+):(\d+) (AM|PM) to (\d+):(\d+) (AM|PM)", s):
        a, b, c, d = int(matches.group(1)), int(matches.group(2)), int(matches.group(4)), int(matches.group(5))
        if max(b, d) > 59:
            raise ValueError
        if matches.group(3) == "PM":
            if a > 12:
                raise ValueError
            a += 12
            a %= 24
        else:
            if a == 12:
                a = 0
        if matches.group(6) == "PM":
            if c > 12:
                raise ValueError
            if c < 12:
                c += 12
                c %= 24
        return f"{a:02d}:{b:02d} to {c:02d}:{d:02d}"
    elif matches := re.search(r"(\d+) (AM|PM) to (\d+) (AM|PM)", s):
        a, b, c, d = int(matches.group(1)), 0, int(matches.group(3)), 0
        if matches.group(2) == "PM":
            if a > 12:
                raise ValueError
            a += 12
            a %= 24
        else:
            if a == 12:
                a = 0
        if matches.group(4) == "PM":
            if c > 12:
                raise ValueError
            if c < 12:
                c += 12
                c %= 24
        return f"{a:02d}:{b:02d} to {c:02d}:{d:02d}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
