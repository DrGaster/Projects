number = int(input('What is the number that you want to know if it is even?'))
def evenodd(number):
    if number % 2 == 0:
        return 'It is Even'
    else:
        return 'It is False'
print(evenodd(number)) 