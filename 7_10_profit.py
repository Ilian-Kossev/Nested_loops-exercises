coins_1_lv = int(input())
coins_2_lv = int(input())
notes_5_lv = int(input())
input_sum = int(input())
for number_1 in range(coins_1_lv + 1):
    value_1 = 1
    for number_2 in range(coins_2_lv + 1):
        value_2 = 2
        for number_3 in range(notes_5_lv + 1):
            value_3 = 5
            result = number_1 * value_1 + number_2 * value_2 + number_3 * value_3
            if result == input_sum:
                print(f'{number_1} * 1 lv. + {number_2} * 2 lv. + {number_3} * 5 lv. = {result} lv.')



