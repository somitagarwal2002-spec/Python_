# Password Generator (Simple and Advanced Method) -------------------------------
import random

alpha = ["A","a","B","b","C","c","D","d","E","e"]
num = ["1","2","3","4","5","6","7","8","9","0"]
special = ["!","@","#","<",">","*","&"]

a = int(input("how many alphabets \n"))
b = int(input("how many numbers \n"))
c = int(input("how many special characters \n"))

# password = ""
# Simple method 
# for char in range(1, a+1):
#     random_char = random.choice(alpha)
#     password += random_char

# for char in range(1, b+1):
#     password += random.choice(num)

# for char in range(1, c+1):
#     password += random.choice(special)

# print(password)

# Advanced version 

password_list = []

for char in range(1, a+1):
    password_list.append(random.choice(alpha))

for char in range(1, b+1):
    password_list.append(random.choice(num))

for char in range(1, c+1):
    password_list.append(random.choice(special))

print(password_list)
random.shuffle(password_list)
print(password_list)

advanced_password = ""
for each in password_list:
    advanced_password += each

print("Your final password is",advanced_password)
