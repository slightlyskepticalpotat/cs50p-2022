import random, sys

while True:
    try:
        n = int(input("Level: "))
        if n < 1:
            continue
        break
    except:
        pass
secret = random.randint(1, n)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break
    except:
        pass
