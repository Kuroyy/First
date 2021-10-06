import random


def play_dice(bet):
    result = 0
    user_dice = random.randint(2, 12)
    casino_dice = random.randint(2, 12)
    if user_dice > casino_dice:
        result += bet
    elif user_dice == casino_dice:
        result = result
    else:
        result -= bet
    return result

user_money = 5000
print(f"У вас в начале {user_money} денег")

for i in range(3):
    user_money += play_dice(500)  # +500 или -500

print(f"У вас в финале {user_money} денег")
