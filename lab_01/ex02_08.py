def divisible_by_5(binary_num):
    decimal_num = int(binary_num, 2)
    if decimal_num % 5 == 0:
        return True
    else:
        return False

binary_string = input("Enter binary numbers (separated by commas): ")

binary_list = binary_string.split(',')
divisible_list = [b for b in binary_list if divisible_by_5(b)]

if len(divisible_list) > 0:
    result = ', '.join(divisible_list)
    print("Binary numbers divisible by 5 are:", result)
else:
    print("There are no binary numbers divisible by 5 in the entered list.")
