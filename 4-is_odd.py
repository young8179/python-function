num_1 = int(input("type the number: "))
def is_even(num):
    
    return num % 2 == 0

result = is_even(num_1)
print(result)


def is_odd():
    if result == True:
        return False
    else:
        return True

isOdd = is_odd()
print(isOdd)
# ------------------------------------------
# alternative-1
def is_odd(num):
    return not is_even(num)

isOdd = is_odd(num_1)
print(isOdd)

# alternative-2
def is_odd(num):
    return not result

isOdd = is_odd(num_1)
print(isOdd)

    
    