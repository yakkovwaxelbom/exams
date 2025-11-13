from ciphers.base import Cipher


class Caesar(Cipher):

    @staticmethod
    def encode(text, key):
        result = []

        for i in range(len(text)):
            char = text[i]
            if not char.isalpha():
                temp = char
            elif char.isupper():
                temp = chr((ord(char) + key - 65) % 26 + 65)
            else:
                temp = chr((ord(char) + key - 97) % 26 + 97)

            result.append(temp)
        return "".join(result)

    @staticmethod
    def decode(text, key):
        return Caesar.decode(text, 26 - key)