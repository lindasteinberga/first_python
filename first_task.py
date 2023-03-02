def max_number(num1, num2, num3):
    highest_number = 0
    numbers = [num1, num2, num3]
    for number in numbers:
        if number > highest_number:
            highest_number = number
    print(highest_number)
    return highest_number

#new
#Write a Python function to find the Max of three numbers.
def max_of_two( a, b ):
    if a > b:
        return a
    return b
def max_of_three( a, b, c ):
    return max_of_two( a, max_of_two( b, c ) )
print(max_of_three(10, 20, 30))


#ChatGPT option
def find_max(a, b, c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num

print(find_max(50, 10, 3))