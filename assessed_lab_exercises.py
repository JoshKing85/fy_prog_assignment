def calculator(num1, num2, operator):

    if operator == "+":
        result = num1 + num2
        print(f"The result is: {result}")

    elif operator =='-':
        result = num1 - num2
        print(f"The result is: {result}")

    elif operator =='*':

        result = num1 *num2
        print(f"The result is: {result}")

    elif operator =='/':
        
        if num2 == 0:
            print('Error: result is undefined')
            return 'Undefined'
        else:
            result = num1/num2
            print(f"The result is: {result}")
    
    elif operator =='%':

        result = num1 % num2
        print(f"The result is: {result}")

    elif operator =='>':
        result = num1 > num2
        print(f"The result is: {result}")
    
    elif operator =='>=':
        result = num1 >= num2
        print(f"The result is: {result}")
    
    elif operator =='<':
        result = num1 < num2
        print(f"The result is: {result}")
    
    
    elif operator =='<=':
        result = num1 <= num2
        print(f"The result is: {result}")
    

    else:
        
        return 'Invalid opereator'

    return result

def max_of_three(num1, num2, num3):

    if num1 >= num2:
    # If selction to logically determine maximum number.
        if num1 >= 3:
            maximum = num1

        else: 
            maximum = num3
    
    # If selction to logically determine maximum number.
    else:
        if num2 >= num3:

            maximum = num2
        else:
            maximum = num3

    
    return maximum

def winning_numbers(user_list, winning_list):


    # Define list with prizes indexed
    str_list = ['No', 'Third', 'Second', 'First']


    #Convert lists to sets.
    set_list_one = set(user_list)
    set_list_two = set(winning_list)
    
    #Intersect to find repeating elements.
    total = set.intersection(set_list_one, set_list_two)
    prize = str_list[len(total)]
    
    # Length of new list equal to index of prize.
    if len(total) > 0:
        print(f'Congratulations you have won {prize} prize!')
    else:
        print(f'Unlucky this time you won {prize} prize.')
    
    return prize

def are_anagrams(str1, str2):
     
    # Check lengths match
    if len(str1) != len(str2):
        
        is_anagram = False
        
    else:
         # use sorted routine to rearrange strings for comparison. True if they equate
        if sorted(str1) == sorted(str2):
            is_anagram = True
        else:
            # Otherwise False value
            is_anagram = False
    
    return is_anagram

def calculate_average(numbers):

    total = 0
    # Loop list to and calculate interations
    for i in numbers:

        total += i
    # Use formula for the mean avarage to find average of list. 
    mean = total / len(numbers)
    
    return mean

def calculate_weekly_pay(hours_worked):

    # no overime multiply by hourly rate
    if hours_worked <= 35:
        wages = hours_worked*12
    
    # Add over time hours rate to total standard rate
    else:
        over_time = hours_worked - 35
        wages = (35*12) + (over_time*18)
    
    
    return wages

def sum_of_evens(min_value, max_value):
    
    total = 0
    # Loop difference, determine if interation is even.
    for i in range(min_value, (max_value + 1)):
        if i % 2 ==0:
            print(i)
            # If true add to total
            total += i
           
    return total

def is_prime(num):


    prime = False
    # Do not count 1 as prime.
    if num == 1:
        return prime
    
    else:
        count = 2
        while count < num:
            #Determine if divisible by count using modulus.
            if num % count == 0:
                break

            else:
                count += 1
    # If count is equal to num no integer other than num is a factor of num, therefore prime number.
    if count == num:
        prime = True

    return prime
