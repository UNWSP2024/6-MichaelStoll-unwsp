#title: dice
#author: michael stoll
#date: 2/28/25
import random
roll_list = []

def rand_dice():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_sum = roll1 + roll2
    return roll_sum

for count in range(100):
    roll_list += [rand_dice()]
sum_of_rolls = sum(roll_list)
print('Total sum of rolls:', sum_of_rolls)
print('Average number per roll:', f'{sum_of_rolls/100:0.2f}')