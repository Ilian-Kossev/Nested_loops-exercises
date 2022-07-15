letter_1 = input()
letter_2 = input()
letter_3 = input()
number_to_letter_1 = ord(letter_1)
number_to_letter_2 = ord(letter_2)
number_to_letter_3 = ord(letter_3)
counter = 0

for number_1 in range(number_to_letter_1, number_to_letter_2 + 1):
    if number_1 == number_to_letter_3:
        continue
    for number_2 in range(number_to_letter_1, number_to_letter_2 + 1):
        if number_2 == number_to_letter_3:
            continue
        for number_3 in range(number_to_letter_1, number_to_letter_2 + 1):
            if number_3 == number_to_letter_3:
                continue
            result_1 = chr(number_1)
            result_2 = chr(number_2)
            result_3 = chr(number_3)
            counter += 1
            print(f"{result_1}{result_2}{result_3}", end=" ")
print(counter)

