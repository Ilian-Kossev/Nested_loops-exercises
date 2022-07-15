number_1 = int(input())
number_2 = int(input())

for number in range(number_1, number_2 + 1):
    sum_odd = 0
    sum_even = 0
    counter = 0
    final_number = str(number)
    for digit in final_number:
        value = int(digit)
        counter += 1
        if counter % 2 == 1:
            sum_odd += value
        else:
            sum_even += value
    if sum_odd == sum_even:
        print(number, end=" ")
