last_sector = input()
rows_in_sector_A = int(input())
number_seats_in_odd_row = int(input())
number_last_sector = ord(last_sector)
number_rows = rows_in_sector_A - 1
counter = 0

for sectors in range(65, number_last_sector + 1):
    sector = chr(sectors)
    number_rows += 1
    number_seats = number_seats_in_odd_row
    for rows in range(1, number_rows + 1):
        if rows % 2 == 0:
            number_seats += 2
        elif rows % 2 != 0 and rows != 1:
            number_seats -= 2
        for seats in range(97, 97 + number_seats):
            seat = chr(seats)
            print(f"{sector}{rows}{seat}")
            counter += 1
print(counter)



