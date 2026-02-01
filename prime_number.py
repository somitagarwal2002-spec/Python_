def is_prime(num):
    if (num <= 1):
        return "Not a Prime Number"

    for i in range(2, num):
        if (num % i == 0):
            return "Not a Prime Number"

    return "Prime Number"
            
number = int(input("Enter any number to check prime: "))
print(is_prime(number))

# ********************** OR ****************************************

# Isse loop kam time tk chalega aur anwer bhi jaldi milega


# def is_prime(num):
#     if (num <= 1):
#         return "Not a Prime Number"

#     for i in range(2, int(number ** 0.5) + 1):
#         if (num % i == 0):
#             return "Not a Prime Number"

#     return "Prime Number"
