## find the shortest string

list_string = ["apple", "fog", "eggs", "oh", "airplane", "a" ]

def shortest_string(strings_list):
    short_string = list_string[0]
    for string in list_string:
        if len(string) < len(short_string):
           short_string = string 
    return short_string    

result = [shortest_string(list_string)]
print(result)

#-----------------------------------
## find the longest sting
list_string = ["apple", "fog", "eggs", "oh", "airplane", "a" ]

def longest_string(string_list):
    long_string = ""
    for string in list_string:
        if len(long_string) > len(string):
            long_string = long_string
        else:
            long_string = string
    return long_string
        
        
result = [longest_string(list_string)]
print(result)