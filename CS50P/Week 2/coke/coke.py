due = 50

while due > 0:
    print('Amount Due: ', due)
    coin = int(input('Insert Coin: '))
    if coin in [5, 10, 25]: due -= coin
    elif coin >= due:
        break

print('Change Owed: ', abs(due))