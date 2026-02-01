# Leap Year Program-------------------------------------------------------

def is_leap_year(year):
    """This area is known as 'docstring' and here we can given documentation
       for our function like any other function that what this function will
        be performing and this will not be executed"""
    
    if (year%4==0):
        if (year%100 == 0):
            if (year%400 == 0):
                return True
            else:
                return False
        return True
    else:
        return False
       
print(is_leap_year(2024))
