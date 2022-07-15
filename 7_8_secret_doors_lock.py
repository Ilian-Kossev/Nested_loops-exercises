num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
if num_2 > 7:
    num_2 = 7
for number_1 in range(1, num_1 + 1):
    if number_1 % 2 == 1:
        continue
    for number_2 in range(2, num_2 + 1):
        if number_2 == 4 or number_2 == 6:
            continue
        for number_3 in range(1, num_3 + 1):
            if number_3 % 2 == 1:
                continue
            print(number_1, number_2, number_3)

