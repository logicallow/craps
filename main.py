#!/usr/bin/env python3

import random

bank = 100
#main menu
def menu():
        global bank
        print('-'*15)
        print("You have ${0}".format(bank))
        print("Bet menu")
        print("1. Hard Eight")
        print("2. Yo/Eleven")
        print("3. Quit")
        print("4. Set bank")
        menu_choice = input("Select bet: ")
        if menu_choice == '1':
                bank = hardeight()
        elif menu_choice == '2':
                yo()
        elif menu_choice == '3':
                print("Goodbye")
                return 1
        elif menu_choice == '4':
                bank = 100
        else:
                print("\nInvalid selection")

#function simulates two dice rolling; returns two value representing two die results
def rolldice():
        return (random.randint(1,6), random.randint(1,6))

#function acts a distinct "bet", in this case a hardway eight (both dice are exactly 4)
def hardeight():
        wager = int(input("Wager: "))
        firstdie, seconddie = rolldice()
        print("\n1st die: {0}".format(firstdie))
        print("2nd die: {0}".format(seconddie))
        print("9:1 if both dice are 4")
        if firstdie == 4 and seconddie == 4:
                print("\n+++ YOU WIN +++\n")
                return bank + wager
        else:
                print("\n=== You lose ===\n")
                return bank - wager

def yo():
        firstdie, seconddie = rolldice()
        print("\n1st die: {0}".format(firstdie))
        print("2nd die: {0}".format(seconddie))
        print("15:1 if 11")
        if firstdie + seconddie == 11:
                print("\n+++ YOU WIN +++\n")
        else:
                print("\n=== You lose ===\n")

exit_choice = 0
while exit_choice != 1:
        exit_choice = menu()
