#-*- codign: utf-8 -*-

COUNTRIES = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile':18,
    'peru': 31
}

while True:
    country = str(input('Escribe un pais: ')).lower()

    try:
        print('La poblacion de {} es: {} millones'.format(country,COUNTRIES[country]))
    except KeyError:
        print('No tenemos el dato de la poblacion del pais {}'.format(country))