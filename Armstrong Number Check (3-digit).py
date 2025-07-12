number = int(input("Enter a 3-digit number: "))
original_number = number
digit1 = number % 10
number = number // 10
digit2 = number % 10
digit3 = number // 10
armstrong_sum = digit1**3 + digit2**3 + digit3**3
if original_number == armstrong_sum:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is NOT an Armstrong number.")
