number = int(input('What number do you want to know the remainder of?'))

def threeremainder(number2):
    asd = number2 % 3
    return asd


def evenodd(asd):
    if asd % 2 == 0:
        return 'The Remainder is Even.'
    else:
        return 'The Remainder is Odd.'

def evenoddremainder(number):
    if threeremainder(number) % 2 == 0:
        return True
    else:
        return False

print(evenoddremainder(number))