import random

def daily_sales(available_items, inventory_records, current_day):
    # if day is 0 or multiple of 7 no sales made, return available items as updated in previous function call.
    if current_day == 0 or current_day %7 == 0:
        return available_items
    
    #Generate random value between 0 to 200 as daily sales. Subtract sales from available items, update inventory records.
    else:
        sold_items = random.randint(0, 200)
        available_items -= sold_items

        inventory_records = inventory_records.append([current_day, sold_items, 0, available_items])


    return available_items