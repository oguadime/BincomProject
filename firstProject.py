green = 10
yellow = 5
brown = 6
pink = 5
blue = 31
orange = 9
red = 9
white = 16
arsh = 1
cream = 2
black = 1

# 1. Mean color of shirt (ANS: ORANGE/RED)
def mean(list_of_nums):
    total = 0
    for num in list_of_nums:
        total += num
    return total / len(list_of_nums)

print(mean([green, yellow, brown, pink, blue, orange, red, white, arsh, cream, black])) 

#2. Color mostly worn throughout the week, that is the mode. (ANS: BLUE)
def mode(list_of_nums):
    max_count = (0, 0)
    for num in list_of_nums:
        occurences = list_of_nums.count(num)
        if occurences > max_count[0]:
            max_count = (occurences, num)
    return max_count[1]

print(mode([green, green, green, green, green, green, green, green, green, green, orange, orange, orange, orange, orange, orange, orange, orange, orange,
            yellow, yellow, yellow, yellow, yellow, arsh, black, cream, cream, pink, pink, pink, pink, pink, red, red, red, red,red, red,red, red,red, 
            brown, brown, brown,brown, brown, brown, white, white, white, white,white, white,white, white,white, white,white, white,white, white,white, white,
            blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, 
            blue, blue, blue, blue, blue])) 

#3 Median color (ANS: GREEN)
def median(list_of_nums):
    list_of_nums.sort()
    if len(list_of_nums) % 2 != 0:
        middle_index = int((len(list_of_nums) - 1) / 2)
        return list_of_nums[middle_index]
    elif len(list_of_nums) % 2 == 0:
        middle_index_1 = int(len(list_of_nums) / 2)    
        middle_index_2 = int(len(list_of_nums) / 2) - 1
        return mean([list_of_nums[middle_index_1], list_of_nums[middle_index_2]])   

print(median([green, green, green, green, green, green, green, green, green, green, orange, orange, orange, orange, orange, orange, orange, orange, orange,
            yellow, yellow, yellow, yellow, yellow, arsh, black, cream, pink, pink, pink, pink, pink, red, red, red, red,red, red,red, red,red, 
            brown, brown, brown,brown, brown, brown, white, white, white, white,white, white,white, white,white, white,white, white,white, white,white, white,
            blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, 
            blue, blue, blue, blue, blue])) 

#4. Variance of the colors (ANS: 65.5)
def variance(val):
    numb = len(val)
    m = sum(val) / numb #mean value
    devi = [(x - m) ** 2 for x in val] #square deviation
    variance = sum(devi) / numb
    return variance

print(variance([green, yellow, brown, pink, blue, orange, red, white, arsh, cream, black]))     
           
#5 Probability of picking a red color randomly (ANS: 0.095)
list_of_nums =  sum([green, yellow, brown, pink, blue, orange, red, white, arsh, cream, black]) 
prob = red / list_of_nums

print(prob)  

#7. Recursive searching algorithm 
def search(list1, key):
    for i in range(len(list1)):
        if key == list1[i]:
            print("Key element is found")
            break
    else:
        print("Element is not found")
list1 = [34,23,5,6,7,1,23,8]
key = int(input("Enter the key element:"))
search(list1, key)  

#8. Generating random number from 0 to 1 and converting to decimal
import random
num = random.random()
value = 0
for i in range(len(num)):
    digit = num.pop()
    if digit == "1":
        value = value + pow(2, i)

print(value)        
