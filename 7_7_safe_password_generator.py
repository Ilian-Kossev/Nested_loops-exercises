a = int(input())
b = int(input())
max_number_passwords = int(input())
password_counter = 0
value_symbol_1 = 34
value_symbol_2 = 63
max_number_passwords_reached = False
for x in range(1, a + 1):
    for y in range(1, b + 1):
        password_counter += 1
        value_symbol_1 += 1
        if value_symbol_1 > 55:
            value_symbol_1 = 35
        symbol_1 = chr(value_symbol_1)
        value_symbol_2 += 1
        if value_symbol_2 > 96:
            value_symbol_2 = 64
        symbol_2 = chr(value_symbol_2)
        print(f"{symbol_1}{symbol_2}{x}{y}{symbol_2}{symbol_1}|", end='')
        if password_counter == max_number_passwords:
            max_number_passwords_reached = True
            break
    if max_number_passwords_reached:
        break




