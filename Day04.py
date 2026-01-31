# Random Module
# import random 

# randominteger = random.randint(1,10)
# print(randominteger)

# randomnum = random.random()
# this will print floating random numbers between 0 to 1 where 1 is ecluded
# print(randomnum)

# randomnum = random.random()*10 
# this will print number between 0 to 10 but will exclude 10
# print(randomnum)

# toss = random.randint(0,1)
# if(toss==1):
#     print("Heads")
# elif(toss==0):
#     print("Tails")
# else:
#     print("Invalid Input")

###########################################################################

# List

# list ka index 0 se shuru hota hai

list1 = [1,2,3,4]
list1.append(5)
print(list1)

list1.extend([10,20,30])
print(list1)

import random

# randomly selects anything from the list 
print(random.choice(list1))

random_index = random.randint(0,7)
print(list1[random_index])

# list inside list 

a = [1,2,3,4]
b = [10,20,30,40]
c = [a,b]

print(c)

