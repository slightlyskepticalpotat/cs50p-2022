import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        a, b, c, d = map(int, ip.split("."))
        return 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255
    except:
        return False

if __name__ == "__main__":
    main()
