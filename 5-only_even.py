
## only even
def only_even(numbers):
    onlyEven = []
    for num in numbers:
        if num % 2 == 0:
            onlyEven.append(num)
    print(onlyEven)    

check_number= [2, 10, 5, 42, 3, 7, 22, 44, 55, 86, 96]
only_even(check_number)

#--------------------------
def only_even(numbers):
    onlyEven = []
    for num in numbers:
        if num % 2 == 0:
            onlyEven.append(num)
    return onlyEven   

check_number= [2, 10, 5, 42, 3, 7, 22, 44, 55]
result = only_even(check_number)
print(result)

##---------------------------------
## only odds

def is_odds(numbers):
    odd_num = []
    for num in numbers:
        if num % 2 != 0:
            odd_num.append(num)
    return odd_num

check1_num = [3, 6, 4, 11, 12, 20, 23, 40, 47, 48]
result = is_odds(check1_num)
print(result)