left = 50
while left > 0:
    print(f"Amount Due: {left}")
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        left -= coin
print(f"Change Owed: {-left}")