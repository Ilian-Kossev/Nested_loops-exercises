n1 = int(input())
n2 = int(input())
for number_1 in range(n1, n2 + 1):
    pass
    for number_2 in range(n1, n2 + 1):
        pass
        for number_3 in range(n1, n2 + 1):
            pass
            for number_4 in range(n1, n2 + 1):
                if number_1 % 2 == 0:
                    if number_4 % 2 == 0:
                        continue
                else:
                    if number_4 % 2 == 1:
                        continue
                if number_4 >= number_1:
                    continue
                if (number_2 + number_3) % 2 == 1:
                    continue
                print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")
