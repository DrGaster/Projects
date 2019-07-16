a = int(input("what is the first number you wish to compare?"))
b = int(input("what is the second number you wish to compare?"))
def higher(a, b):
    if (a < b):
        c = b
    else :
        c= a
    return c
print(higher(a, b))