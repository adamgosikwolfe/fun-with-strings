#Dice Rolling Simulator
#Choose how many sides the die hash
#Choose how many to roll of each die

import random

print("Let's roll!")

rolling = True
dice_type = ["2", "4", "6", "8", "10", "12", "20", "100"]
while rolling==True:
  correct_type = False
  while correct_type == False:
    correct_type = True
    dice_sides = input("\nWhat sided dice to roll? Choose from 2, 4, 6, 8, 10, 12, 20, and 100. Separate the dice type with commas.").split(",")
    for die in dice_sides:
      if die not in dice_type:
        correct_type=False
    if correct_type==False:
      print("Please choose correct dice sizes") 

  dice_qty = input("How many of each die to roll? Separate dice type with commas.").split(",")

  count_total = 0
  reroll = True

  while reroll==True:
    for n, die in enumerate(dice_sides):
      sub_total=0
      for q in range(0,int(dice_qty[n])):
        die_roll=random.randint(0,int(die))
        count_total = count_total + die_roll
        sub_total = sub_total + die_roll
        print("d"+ str(die).strip() + ": " + str(die_roll))
      print("d" + str(die).strip() + " Subtotal:" + str(sub_total))

    print("Dice total: " + str(count_total))
    roll_check = input("Reroll?")
    reroll = bool(roll_check.lower() == "y")
    print("\n")