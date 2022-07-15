n = int(input())
l = int(input())
for number in range(1, n):
    for number_1 in range(1, n):
        for number_2 in range(97, 97 + l):
            value = chr(number_2)
            for number_3 in range(97, 97 + l):
                value_1 = chr(number_3)
                for number_4 in range(number_1 + 1, n + 1):
                    print(f"{number}{number_1}{value}{value_1}{number_4}", end=" ")
