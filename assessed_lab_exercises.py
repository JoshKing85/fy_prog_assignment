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
def celsius_to_fahrenheit(celsius):

    #formula for conversion (9/5) * C + 32   
    fahrenheit = ((9/5)*celsius) + 32   
    
    return fahrenheit

def decrypt_cypher_text(encrypted_text, key):
    

    new_char = ''
    plain_text = ''
    
    for character in encrypted_text:
        
        # Use chr() routine inconjuction wtih ord() routine subracted by key to determine string character.
        new_char = chr(ord(character)- key)

        plain_text = plain_text + new_char


    return plain_text

def find_maximum_difference(a, b):

    
    max_diff = 0    

    # Initiate variable for array minumum and maxium values using min() and max() function.
    max_1, max_2, min_1, min_2 = max(a), max(b), min(a), min(b)
    
    # Determine difference of min, max of both lists.
    first_max = max_1 - min_2
    second_max = max_2 - min_1

    #Select greatest difference.
    if first_max >= second_max:
        max_diff = first_max

    else:
        max_diff = second_max
    
    
    return max_diff

def fuel_cost(distance_miles):
    # contants for for formula
    MPG = 50
    LITRES = 4.5
    PRICE_PER_LITRE = 1.49

    f_cost = PRICE_PER_LITRE * (distance_miles / MPG) * LITRES # Formula with constants and variable miles_travelled

    return f_cost

def is_golden_number(n):

    is_gold = False
    
    # Nested loop to find summation of n
    for a in range(n):
        for b in range(n):
            
            # Checks if argument meets all propositional statements.
            if a + b == n and a*b % 1000 == 0:
                is_gold = True
                break
            
                
    return is_gold 

def km_to_miles(kilometers):

    # Constant conversion as directly proportionate.
    MILE_CON = 0.62

    miles = kilometers * MILE_CON 
    miles = round(miles, 3) # Library routine, round()  for decimal required.
    
    return miles

def letter_occurrence(input_string):

    # Ordinal for A, a.
    ord_ca, ord_a  = 65, 97
    
    # Set variable to be returned.
    total = 0
    
    for char in input_string:

        if ord(char) == ord_ca or ord(char) == ord_a:
            
            total += 1

    return total

def annual_net_income(gross_salary):


    net = 0
    # Deductions determined from equal or greater if selections.
    if gross_salary  >= 45000:
        net = gross_salary  * (1 - 0.5) # All deductions use same formula (1 - n) for percentage reduction.
    
    elif gross_salary  >= 30000:
        net = gross_salary  * (1 - 0.3)

    else:
        net = gross_salary  * (1 - 0.15)
    
    return net
