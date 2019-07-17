array = [1, 2, 3, 4, 5]
numbera = int(input('What is the Number?'))
def firstfivemultiples(number):
    for i in array:
        number = numbera * i
        print(number)
print(firstfivemultiples(numbera))