number = int(input())
for number_1 in range(1, 10):
    if number % number_1 != 0:
        continue
    for number_2 in range(1, 10):
        if number % number_2 != 0:
            continue
        for number_3 in range(1, 10):
            if number % number_3 != 0:
                continue
            for number_4 in range(1, 10):
                if number % number_4 != 0:
                    continue
                print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")
