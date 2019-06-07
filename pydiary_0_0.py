"""teplate for diary_0_0.py"""

from datetime import date

def add(target, day = date.today(), *notes ) :
    observation = {
    'target:' : 'date.today()'
    }

    return observation

def show(observations) :
    print("Here are all observations.")
    print()


def main():
    condition = True
    while condition:
        notes = input("Give your note: ")
        observations = dict()
        counter = 0
        if not notes:
            print("Please give note first: ")
        elif notes == "Q":
            condition = False
        else:
            add(counter)
            show()
            counter += 1


if __name__ == '__main__':
    '''
    if the program is started from a script
    '''
    main()