import random

def play_dice(user_money):
    bet = (input("Сколько ставишь? "))
    
    # тест ставки
    if bet > user_money:
    	print("У тебя столкьо нет!")
    	play_dice(user_money)
    elif bet <= 0:
    	print("Ставки от 1!")
    	play_dice(user_money)
    else:
    	user_dice = random.randint(2, 12)
    	casino_dice = random.randint(2, 12)

    	# проверить выпавшее
    	е
    	print("У вас")
    if user_dice > casino_dice:
        print("Ты выиграл") 
        user_money += bet
    elif user_dice == casino_dice:
        print("Ничья")
    else:
        print("Ты проиграл!")   
        user_money -= bet
    return user_money


user_money = 5000
play_dice(user_money)
