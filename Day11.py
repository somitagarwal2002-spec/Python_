import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
cont = True

def blackjack():
    while cont:
        game = input("You want to play black jack game, Type 'y' for yes and 'n' for no: \n")
        your_cards = []
        computer_cards = []
        if game == "y":
            your_cards.append(random.choice(cards))
            your_cards.append(random.choice(cards))
            print("Your cards are",your_cards)
            computer_cards.append(random.choice(cards))
            print("Computer's first card is",computer_cards)
            computer_cards.append(random.choice(cards))

            next = input("Type 'y' to get anothe card, type 'n' to pass")
            if next == "y":
                print()

            else:
                print("Your final cards are",your_cards,"Sum of cards is",sum(your_cards))
                if (sum(your_cards)>21):
                    print("You lose")

                print("Computer final cards are",computer_cards,"Sum of cards is",sum(computer_cards))
                if (sum(computer_cards)>21):
                    print("You win")
        else:
            cont = False
            print("Thank you")

blackjack()
