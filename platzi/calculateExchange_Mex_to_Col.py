# -*- coding: utf-8 -*- 
#primera linea para especificar la codificacion

def run():
    print('CALCULADORA DE TIPO DE CAMBIO')
    print('PESOS MEXICANOS A COLUMBIANOS')
    print('')

    ammount = float(input('Cantidad de pesos mexicanos: '))

    result = change_Mex_to_Col(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount,result))
    print('')

def change_Mex_to_Col(ammount):
    Mex_exchange = 145.97

    return Mex_exchange * ammount
#indica donde inicia el programa
if __name__ == '__main__':
    run()

