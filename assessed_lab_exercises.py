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


