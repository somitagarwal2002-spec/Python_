import random

a = int(input("Chose between 0 for rock,1 for paper and 2 for scissor \n"))
b = random.randint(0,2)
if (b==0):
    print("Computer choses rock")
elif (b==1):
    print("Computer choses paper")
elif (b==2):
    print("Computer choses scissor")
else:
    print("Wrong ")
    
if(a==b):
    print("It's Draw")
elif(a==0 and b == 1):
    print(" Computer wins")
elif(a==0 and b == 2):
    print(" You win")
elif(a==1 and b == 0):
    print(" You wins")
elif(a==1 and b == 2):
    print(" Computer wins")
elif(a==2 and b == 0):
    print(" Computer wins")
elif(a==2 and b == 1):
    print(" You wins")
else:
    print("Not Valid        ")
