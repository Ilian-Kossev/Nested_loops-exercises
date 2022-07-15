N = int(input())
for number_1 in range(1, 10):
    for number_2 in range(1, 10):
        for number_3 in range(1, 10):
            for number_4 in range(1, 10):
                sum1 = number_1 + number_2
                sum2 = number_3 + number_4
                if sum1 == sum2:
                    if N % sum1 == 0:
                        print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")
