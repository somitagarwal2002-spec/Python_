import random

cars = ["bmw","mercedes","ford","mahindra","audi"]
word = random.choice(cars)
print(word)
blanks = ""
for i in word:
    blanks += "_"
print(blanks)

game_over = False
lives = 6
correct_words = []
while not game_over:

    guess = input("Guess any alphabet ").lower()
    if guess in correct_words:
        print("Already Guessed")
        
    display = ""
    for letter in word:
        if letter == guess:
            display += guess
            correct_words.append(guess)
            
        elif letter in correct_words:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in correct_words:
        lives -= 1
        print(lives, "  Lives Remaining Only")
        if lives == 0:
            game_over = True
            print("You lose")
        
    if guess == word:
        game_over = True
        print("You win")