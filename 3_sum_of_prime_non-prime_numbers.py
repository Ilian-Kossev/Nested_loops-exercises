command = input()
sum_prime_numbers = 0
sum_non_prime_numbers = 0
non_prime_number_found = False
while command != "stop":
    number = int(command)
    if number == 0:
        command = input()
        continue
    elif number < 0:
        print(f"Number is negative.")
        command = input()
        continue
    for num in range(2, number):
        if number % num == 0:
            non_prime_number_found = True
            break
    if non_prime_number_found:
        sum_non_prime_numbers += number
    else:
        sum_prime_numbers += number
    non_prime_number_found = False
    command = input()
print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_non_prime_numbers}")



