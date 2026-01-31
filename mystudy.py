# a = "ello"
# print(a.replace("e","y"))

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("End")
# show(3)



def calc(n):
    if n == 0:
        return 0
    return calc(n-1) + n

sum = calc(10)
print(sum)
