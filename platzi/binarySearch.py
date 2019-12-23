# -*- coding: utf-8 -*-
def binarySearch(numbers,number_to_find,low,high):
    if low > high:
        return False

    mid =  int((low + high)/2)

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid]> number_to_find:
        return binarySearch(numbers,number_to_find,low,mid-1)
    else:
        return binarySearch(numbers,number_to_find,mid+1,high)

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,11,20,36,46,89,99,100,123,456,789]

    number_to_find =  int(input('Ingresa un numero: '))

    result = binarySearch(numbers, number_to_find,0, len(numbers)-1)

    if result == True:
        print('El numero si esta en la lista!!! yei! c:')
    else:
        print('El numero no esta en la lista, no yei :c')
