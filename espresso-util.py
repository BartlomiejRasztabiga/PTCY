functions = (
    (2, 6, 9, 10, 13, 14),
    (0, 2, 4, 6, 9, 11, 13, 15),
    (2, 3, 6, 7, 8, 9, 11, 13, 15)
)

variables = 4

print(f'.i {variables}')
print(f'.o {len(functions)}')

for number in range(2**variables):
    binary_input = bin(number)[2:]
    while len(binary_input) < variables:
        binary_input = '0' + str(binary_input)

    values = ' '
    for function in functions:
        values += str(int(number in function))
    print(binary_input + values)

print('.e')
