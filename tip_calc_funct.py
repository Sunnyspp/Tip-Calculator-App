def calculate_food_total(food_amount: float, tip_percentage: int)-> float:
    tip = food_amount * tip_percentage/100
    total = food_amount + tip

    print('\nπ°π°π°----------------------------------π°π°π°\n')
    print(f'πFood Amount: ${food_amount}')
    print(f'π°Tip Amount: ${tip}\n')
    print("----------------------")
    print(end='')
    print(f'π°Total Amount: ${total}')
    print("----------------------")
    print(end='')
    print('\nπ°π°π°------------------------------------π°π°π°')
    return total
# print((calculateFoodTotal(100, 10))

