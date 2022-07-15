num_1 = int(input())
num_2 = int(input())
magic_num = int(input())
counter_combinations = 0
combination_found = False
number_1 = 0
number_2 = 0
for number_1 in range(num_1, num_2 + 1):
    for number_2 in range(num_1, num_2 + 1):
        counter_combinations += 1
        result = number_1 + number_2
        if result == magic_num:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f"Combination N:{counter_combinations} ({number_1} + {number_2} = {magic_num})")
else:
    print(f'{counter_combinations} combinations - neither equals {magic_num}')


