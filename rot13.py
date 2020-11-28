""" 
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, 
they should be returned as they are. Only letters from the latin/english alphabet should be shifted, 
like in the original Rot13 "implementation". 
"""

def rot13(message):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    aux = ''
    for char in message:
        if char == ' ' or not char.isalpha():
            aux += char
            continue
        index = alphabet.index(char.lower()) + 13
        if index > len(alphabet) - 1:
            index = index - len(alphabet)
        if char.isupper():
            aux += alphabet[index].upper()
        else:
            aux += alphabet[index]
    return aux

