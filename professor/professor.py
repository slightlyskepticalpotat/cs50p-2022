import random

def main():
    level = get_level()
    correct = 0
    for i in range(10):
        a, b = generate_integer(level), generate_integer(level)
        c = a + b
        for j in range(3):
            try:
                ans = int(input(f"{a} + {b} = "))
                if c != ans:
                    raise
                else:
                    correct += 1
                    break
            except:
                print("EEE")
                if j == 2:
                    print(f"{a} + {b} = {c}")
    print(f"Score: {correct}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
