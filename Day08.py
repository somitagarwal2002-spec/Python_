# True Love Calculaor -------------------------

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_count = (
        combined_names.count('t') +
        combined_names.count('r') +
        combined_names.count('u') +
        combined_names.count('e')
    )
    
    love_count = (
        combined_names.count('l') +
        combined_names.count('o') +
        combined_names.count('v') +
        combined_names.count('e')
    )

    love_score = int(str(true_count) + str(love_count))

    print(love_score)

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
calculate_love_score(name1, name2)
