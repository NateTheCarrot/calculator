def calculate():
    operation = input('''
Which operation would you like? Type it in to do it.
+ for addition,
- for subtraction,
x for multiplication,
and / for division.
''')

    number_1 = int(input('Enter the first number: '))
    number_2 = int(input('Enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == 'x':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Oh, that\'s not a valid response... Please run the program again to try again.')


calculate()









#I see you looking at me >_>

#i still wonder how to get decimals in this

#cya

