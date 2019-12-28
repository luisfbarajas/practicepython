# -*- coding: utf-8 -*-
def run():
    counter = 0
    try:
        with open('platzi/cuento.txt',encoding='utf-8') as f:
            for line in f:
                counter += line.count('Beatriz')
    except FileNotFoundError:
        print('No se encontro el archivo')
    else:
        print('Betty bb se encuentra {} veces en el cuento'.format(counter))


if __name__ == '__main__':
    run()