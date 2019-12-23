# -*- coding: utf-8 -*-

def palindromo2(word):
    reversed_word =  word[::-1]

    return same_word(word,reversed_word)

def same_word(word,reversed_wrod):
    if word == reversed_wrod:
        return True

    return False

def palindromo(word):
    reversed_letters = []

    for letters in word:
        reversed_letters.insert(0,letters)

    reversed_word =''.join(reversed_letters)

    return same_word(word,reversed_word)

if __name__ == '__main__':
    word = input('Ingresa una palabra: ')

    result = palindromo2(word)

    if result is True:
        print('{} si es palindromo'.format(word))

    else:
        print('{} no es palindromo'.format(word))