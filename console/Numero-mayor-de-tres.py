#  Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 

def takeANumber():
    print('Enter a number: ')
    return input()

def maxNumber(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n2 and n2> n2:
        return n2
    else:
        return n3

n1 = int(takeANumber())
n2 = int(takeANumber())
n3 = int(takeANumber())

print ('El número mayor es: '+ str(maxNumber(n1,n2,n3)))
