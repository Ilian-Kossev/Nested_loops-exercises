number_men = int(input())
number_women = int(input())
number_tables = int(input())
counter_dates = 0
no_tables_left = False
for number_m in range(1, number_men + 1):
    for number_w in range(1, number_women + 1):
        if counter_dates == number_tables:
            no_tables_left = True
            break
        print(f"({number_m} <-> {number_w})", end=" ")
        counter_dates += 1
    if no_tables_left:
        break