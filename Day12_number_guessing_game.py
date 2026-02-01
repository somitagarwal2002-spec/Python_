# Number Guessing Game -------------------------------------------------

import random

def guess(lives):
    while lives>0:
            guess = int(input("Guess any number between 1 to 100: "))

            if(num == guess):
                print("You guessed the right number")
     
            elif (num - 10 < guess < num):
                print("You are close but think high")
                lives -= 1
                print("You have only",lives,"remaining")

            elif (guess < num):
                print("You are too low")
                lives -= 1
                print("You have only",lives,"remaining")

            elif (num < guess < num + 10):
                print("You are close but think low")
                lives -= 1
                print("You have only",lives,"remaining")

            elif (guess > num):
                print("Your are too high")
                lives -= 1
                print("You have only",lives,"remaining")

            else:
                print("Wrong input")

num = random.randint(1,100)
print(num)
level = input("Chose your level 'easy' or 'hard': ")
if level == "easy":
    guess(10)
elif level == "hard":
    guess(5)  
else:
    print("enter correct level")    

