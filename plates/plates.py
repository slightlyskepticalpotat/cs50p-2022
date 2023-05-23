def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    first_num = True
    if not 2 <= len(s) <= 6:
        return False
    if not s[0].isalpha():
        return False
    if not s[1].isalpha():
        return False
    if not s.isalnum():
        return False
    for i in range(len(s)):
        if s[i].isnumeric():
            if s[i] == "0" and first_num:
                return False
            else:
                first_num = False
        else:
            if first_num == False:
                return False
    return True

main()
