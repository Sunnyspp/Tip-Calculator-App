def bigger_guy(num1, num2):
    num1 = int(input('Enter num1: '))
    num2 = int(input('Enter num2: '))
    print("🔦🔦🔦🔦🔦🔦who is the bigger guy🔦🔦🔦🔦🔦🔦🔦")
    print(f"num1 = {num1} and num2 = {num2}")
    print("🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦\n")
    if num1 > num2:
        print('🤷‍🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🤷‍')
        return(f"👉 {num1} is the bigger guy🤵"
              f"\n'🤷🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🤷‍")
    else:
        print('🤷🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🤷‍')
        return(f"👉 {num2} is the bigger guy🤵"
              f"\n🤷🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🔦🤷‍")
print(bigger_guy(int, int))
