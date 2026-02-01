def add(first, second):
    return first+second

def sub(first, second):
    return first-second

def mul(first, second):
    return first*second

def divide(first, second):
    return first/second

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":divide,
}
def calculator():
    first = float(input("Enter first number: "))
    # print(operations["*"](4,2))
    should_accumulate = True
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        choice = input("Pick an operation: ")
        second = float(input("Enter second number: "))
        answer = operations[choice](first, second)
        print(f"{first} {choice} {second} = {answer}")

        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")

        if cont == "y":
            first = answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()

calculator()
