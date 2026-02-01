# Secret Bidding Program --------------------------------------------------

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print("The highes bidder is",winner,"with a bid of $",highest_bid)

more = True
print("Welcome to the secret auction program:")
dictionary = {}
while more is True:

    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    dictionary[name] = bid
    restart = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    print("\n"*100)

    if restart == "no":
        find_highest_bidder(dictionary)
        more = False
        
print(dictionary)



