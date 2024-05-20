rom_nums={'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000,}
int_val = 0
user_input = input('Enter Roman numeral: ').upper()
for i in range(len(user_input)):
    if user_input[i] in rom_nums:
        if i + 1 < len(user_input) and rom_nums[user_input[i]] < rom_nums[user_input[i + 1]]:
            int_val -= rom_nums[user_input[i]]
        else:
            int_val += rom_nums[user_input[i]]
    else:
        print('Error: invalid input.')
        break
print(f'Int equivalent to {user_input} is: {int_val}')