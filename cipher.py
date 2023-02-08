# Шифрование сообщения шифром цезаря
import string


# Функция шифрования
def cipher(s, value):
    alphabet = string.ascii_lowercase  # английский алфавит в нижнем регистре
    caesar = ''
    if value > 26:
        value %= 26
    for item in s:
        if item in alphabet:
            if ord(item) + value > ord('z'):
                caesar += chr((ord(item) + value) - 26)
            else:
                caesar += chr(ord(item) + value)
    return caesar


# Функция дешифратор
def decipher(s, value):
    alphabet = string.ascii_lowercase  # английский алфавит в нижнем регистре
    caesar = ''
    if value > 26:
        value %= 26
    for item in s:
        if item in alphabet:
            if ord(item) + value < ord('a'):
                caesar += chr((ord(item) - value) + 26)
            else:
                caesar += chr(ord(item) - value)
    return caesar


s = input('Введите текст - ')
value = int(input('Введите ключ - '))
# print(decipher(s, value))
print(cipher(s, value))
