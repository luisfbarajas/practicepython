# -*- coding: utf-8 -*-
import random

def Generate_List_Of_Temps(quantity):
    List_Of_Temps = list()

    for i in range(quantity):
        List_Of_Temps.append(random.randint(0,50))

    return List_Of_Temps

def Average_Of_Temps(temps):
    sums_of_temps = 0

    for temp in temps:
        sums_of_temps += temp

    return sums_of_temps / len(temps)

if __name__ == '__main__':
    How_Many =  int(input('Cuantas temperaturas: '))

    Temps = Generate_List_Of_Temps(How_Many)

    average =  Average_Of_Temps(Temps)

    print('Temperaturas: {}'.format(Temps))
    print('La temperatura promedio es {}'.format(average))