def calculate_food_total(food_amount: float, tip_percentage: int)-> float:
    tip = food_amount * tip_percentage/100
    total = food_amount + tip

    print('\n💰💰💰----------------------------------💰💰💰\n')
    print(f'🍔Food Amount: ${food_amount}')
    print(f'💰Tip Amount: ${tip}\n')
    print("----------------------")
    print(end='')
    print(f'💰Total Amount: ${total}')
    print("----------------------")
    print(end='')
    print('\n💰💰💰------------------------------------💰💰💰')
    return total
# print((calculateFoodTotal(100, 10))

