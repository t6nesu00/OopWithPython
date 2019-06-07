'''
a program that is operating in a loop waiting for
a user to enter amount of dices to roll, and shows the result
'''
import random


def roll(number_of_dice):
    total = 0
    for i in range(0, int(number_of_dice)):
        roll = random.randint(1, 6)
        total = total + roll
        print(roll, end=" ")
    print(", sum= ", total)


def main():
    number_of_dice = 1
    while number_of_dice != None:
        number_of_dice = str(input("Number of dice to roll or ENTER to exit: "))
        if number_of_dice != "":
            roll(number_of_dice)
        else:
            break


if __name__ == '__main__':
    main()



