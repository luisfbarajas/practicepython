#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
# (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def takeFirstNumbers():
    print('Enter first number: ')
    return input()

def takeSecondNumber():
    print('Enter a second nuber')
    return input()

def max(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2

n1 = takeFirstNumbers()
n2 = takeSecondNumber()
print('El número mayor es '+ str(max(int(n1),int(n2))))
