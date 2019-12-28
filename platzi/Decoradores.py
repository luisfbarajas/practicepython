# -*- codign: utf-8 -*-

def protected(func):

    def wrapper(password):
        if password == 'fuckyou':
            return func()
        else:
            print('valiste malle')
    return wrapper

@protected
def protected_func():
    print('tu contraseña es correcta.')

if __name__ == '__main__':
    password =  str(input('escribele mijo: '))

    protected_func(password)