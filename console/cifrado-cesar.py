#Cifrado Cesar
#clave
TAM_MAX_CLAVE = 26
#get the encryp mod
def getmod():
    while True:
        print('You wanna encryp or unencryp the message?')
        mod = input().lower()
        if mod in 'encrypte e unencrypte u'.split():
            return mod
        else:
            print('enter "encrypte" or "e" or "unencrypte" or "u"')
#get the message
def getMessage():
    print('Enter the message my man:')
    return input()

#get the key number
def getKey():
    key = 0
    while True:
        print('Enter the key number ')
        key = int(input())
        if (key >=1 and key <= TAM_MAX_CLAVE):
            return key

def getMessageEncrypted(mod, messagge, key):
    if mod[0] == 'u':
         key = -key
    traduccion = ''

    for simbolo in messagge:
         if simbolo.isalpha():
             num = ord(simbolo)
             num += int(key)

             if simbolo.isupper():
                 if num > ord('Z'):
                     num -= 26
                 elif num < ord('A'):
                     num += 26
             elif simbolo.islower():
                 if num > ord('z'):
                     num -= 26
                 elif num < ord('a'):
                     num += 26

             traduccion += chr(num)
         else:
             traduccion += simbolo
    return traduccion

mod = getmod()
message = getMessage()
key = getKey()

print('You text translated is: ')
print(getMessageEncrypted(mod,message,key))
