# -*- codign: itf-8 -*-
def char_not_repeat(word):
    chars ={}

    for i, char in enumerate(word):
        if char not in chars:
            chars[char] = (i,1)
        else:
            chars[char] = (chars[char][0],chars[char][1]+1)
    
    final_chars = []
    for key, value in chars.items():
        if value[1]== 1:
            final_chars.append((key,value[0]))
        
    not_repeat_char =  sorted(final_chars,key = lambda value:value[1])

    if not_repeat_char:
        return not_repeat_char[0][0]
    else: 
        return '_'


if __name__ == '__main__':
    word = str(input('Ingresa una palabra: '))

    result =  char_not_repeat(word)

    if result == '_':
        print('Todas las letras se repiten')
    else:
        print('El primer caracter no repetido es: {}'.format(result))