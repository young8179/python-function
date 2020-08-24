# c -> f
def conversion():
    c = int(input("type the number: "))
    f = (c * 9/5) + 32
    print(f)

conversion()
#------------------------------------
# f -> c

def conversion_1():
    f = int(input("type the number: "))
    c = (f - 32) * 5/9
    return c

result = conversion_1()
print(result)