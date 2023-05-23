while True:
    try:
        a, b = map(int, input("Fraction: ").split("/"))
        val = a/b*100
        if val > 100:
            raise
        if val >= 99:
            print("F")
        elif val <= 1:
            print("E")
        else:
            print(f"{round(val)}%")
    except:
        pass
    else:
        break