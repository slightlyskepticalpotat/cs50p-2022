import sys
import inflect

from datetime import date, datetime, timedelta

def main():
    p = inflect.engine()
    try:
        birthday = get_date(input("Date of Birth: "))
        raw = p.number_to_words(round(get_diff(date.today(), birthday)))
        print(raw[0].upper() + raw[1:].replace("and ", "") + " minutes")
    except:
        sys.exit("Invalid date")

def get_date(s):
    return date.fromisoformat(s)

def get_diff(a, b):
    return (a - b).total_seconds() / 60

if __name__ == "__main__":
    main()
