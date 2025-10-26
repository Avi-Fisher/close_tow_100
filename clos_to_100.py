import random

def roll_two_d6():

    c1 = random.randint(1,6)
    c2 = random.randint(1,6)

    return c1 + c2

def is_bust(turn,not_turn,number):

    if number > 100:
        print(f"{not_turn} winnnnn!!!")
        exit("goodbye")

    elif number == 100:
        print(f"{turn} winnnnn!!!")
        exit("goodbye")

def equal(name1,name2):
    while True:

        print(input(f"{name1} your turn "))
        play1 = roll_two_d6()
        print(f"you have {play1} point")

        print(input(f"{name2} your turn "))
        play2 = roll_two_d6()
        print(f"you have {play2} point")

        if play1 > play2:
            print("play1 win")
            exit("goodbye")
        elif play1 < play2:
            print("play2 win")
            exit("goodbye")
        else:
            print("The score is equal ")

def menu():

    p1 = {"name":input("enter name player1"),"point":0}
    p2 = {"name":input("enter name player2"),"point":0}

    turn = p1
    not_turn = p2

    pess = 0

    while True:
        print(f"turn {turn["name"]}")
        play = input("enter 'r' for roll or 'p' for pess:  " )

        if play == "r":
            turn["point"] += roll_two_d6()
            print(f"your scor is {turn["point"]}")


            is_bust(turn["name"],not_turn["name"],turn["point"])

            turn,not_turn = not_turn,turn
            pess = 0
            continue

        if play == "p":
            turn,not_turn = not_turn,turn
            pess += 1

        if pess == 2:
            if p1["point"] > p2["point"]:
                exit(f"{p1["name"]} win!!!!!  ")
            elif p1["point"] < p2["point"]:
                exit(f"{p2["name"]} win!!!!!  ")
            else:
                equal(turn["name"],not_turn["name"])

            continue




















































