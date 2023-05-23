months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        old = input("Date: ").strip()
        if "," in old:
            old = old.replace(",", "")
            a, b, c = old.split(" ")
            a = months.index(a) + 1
            if 1 <= int(a) <= 12 and 1 <= int(b) <= 31:
                print(f"{c.zfill(4)}-{str(a).zfill(2)}-{b.zfill(2)}")
                break
        else:
            a, b, c = old.split("/")
            if 1 <= int(a) <= 12 and 1 <= int(b) <= 31:
                print(f"{c.zfill(4)}-{a.zfill(2)}-{b.zfill(2)}")
                break
    except Exception as e:
        pass