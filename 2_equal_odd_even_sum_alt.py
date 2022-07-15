number_1 = int(input())
number_2 = int(input())

for number in range(number_1, number_2 + 1):
    sum_odd = 0
    sum_even = 0
    number_to_string = str(number)
    for index, digit in enumerate(number_to_string):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)
    if sum_even == sum_odd:
        print(number, end=" ")