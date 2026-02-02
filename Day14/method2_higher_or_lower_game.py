# Without using global keyword ----------------------------------------

import random

def ans(random1, random2, score):
    print("Compare A:", random1)
    print("Against B:", random2)

    choose = input("Choose between 'A' and 'B': ").upper()

    if choose == "A":
        if teams[random1] > teams[random2]:
            score += 1
            print("Correct guess. Your current score is:", score)
            return score, True
        else:
            print("You lose. Your final score is:", score)
            return score, False

    elif choose == "B":
        if teams[random2] > teams[random1]:
            score += 1
            print("Correct guess. Your current score is:", score)
            return score, True
        else:
            print("You lose. Your final score is:", score)
            return score, False


teams = {
    "csk":93, "mi":108, "rcb":105, "kkr":74, "gt":70, "pbks":66,
    "lsg":59, "dc":58, "srh":56, "rr":53
}

team_names = list(teams.keys())
score = 0
condition = True

random1, random2 = random.sample(team_names, 2)

score, condition = ans(random1, random2, score)

while condition:
    random1 = random2
    random2 = random.choice(team_names)

    while random2 == random1:
        random2 = random.choice(team_names)

    score, condition = ans(random1, random2, score)
