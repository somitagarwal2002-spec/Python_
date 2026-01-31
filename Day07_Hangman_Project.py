# Hangman Project -------------------------------- 

import random

letters = ["apple", "banana", "orange", "kiwi", "guava"]

chosen_word = random.choice(letters)
# print(chosen_word)

blanks = ""
for i in chosen_word:
    blanks += '_'

print(blanks)
game_over = False

correct_words = []
lives = 6
while not game_over:
    guess = input("Guess any letter:\n").lower()
    if guess in correct_words:
        print("Already Guessed")

    display= ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_words.append(guess)
        elif letter in correct_words:
            display += letter
        else:
            display += "_"
            
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(lives," Lives Remaining Only")
        if lives == 0:
            game_over = True
            print("You lose")
            print("The word was", chosen_word)
    if "_" not in display:
        game_over = True
        print("You Win")

    

        
