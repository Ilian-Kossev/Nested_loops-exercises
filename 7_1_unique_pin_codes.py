n1 = int(input())
n2 = int(input())
n3 = int(input())
for number_1 in range(1, n1 + 1):
    if number_1 % 2 == 1:
        continue
    for number_2 in range(2, n2 + 1):
        if number_2 == 4 or number_2 == 6:
            continue
        for number_3 in range(1, n3 + 1):
            if number_3 % 2 == 1:
                continue
            print(f"{number_1} {number_2} {number_3}")
# judge dava 40/100 !!!