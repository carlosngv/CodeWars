""" In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it. """

def alphabet_position(text):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    aux = ''
    for char in text:
        if char.isalpha():
            aux += str(alphabet.index(char.lower()) + 1) + ' '
    return aux[0:len(aux) - 1]

print(alphabet_position("The sunset sets at twelve o' clock."))