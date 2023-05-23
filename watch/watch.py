import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    link = None
    if matches := re.search(r"\/embed\/(\w*)\"", s):
        link = "https://youtu.be/" + matches.group(1)
    return link

if __name__ == "__main__":
    main()
