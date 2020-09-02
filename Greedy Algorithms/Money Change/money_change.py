# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins = money // 10
    leftover = money % 10
    money = leftover

    coins += money // 5
    leftover = money % 5
    money = leftover

    coins += money
    return coins



if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
