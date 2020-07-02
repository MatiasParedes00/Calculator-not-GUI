import functions as fun
import decorators as deco
import sys

while True:
    deco.decorator1 ("Enter the number:")
    print ("1) One number operation.\n")
    print ("2) Two numbers operation.\n")
    deco.decorator2 ("3) Quit")
    inp = input(": ")
    if inp == "1":
        print ("test")
    elif inp == "2":
        print ("test")
    elif inp == "3":
        while True:
            inp = input("Are you sure? (Y/N): ")
            if inp == "Y" or inp == "y":
                sys.exit(0)
            elif inp == "N" or inp == "n":
                break
            else:
                print ("Incorrect input.\n")
                continue
    else:
        print ("Incorrect input.\n")
        continue
