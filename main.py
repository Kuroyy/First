def coffee(money):
    price = 35
    if money < price:
        print("Недостаточно денег")
        print("Вернул", money)
    else:
        cups =  money // price
        change = money % price
        print("Вставили", money)
        print("Налили", cups)
        print("Сдача", change)
user_money = int(input("Сколько денег вставить в автомат? "))
coffee(user_money)
