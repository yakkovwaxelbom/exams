from ciphers.base import Cipher


class Fence(Cipher):

    @staticmethod
    def __table(text, kay):
        table = [[None] * len(text) for _ in range(kay)]
        rails = list(range(kay - 1)) + list(range(kay - 1, 0, -1))
        for ind, val in enumerate(text):
            table[rails[ind % len(rails)]][ind] = val

        return [c for rail in table for c in rail if c is not None] or ['']

    @staticmethod
    def encode(text, key):
        return ''.join(Fence.__table(text, key))

    @staticmethod
    def decode(text, key):
        rng = range(len(text))
        pos = Fence.__table(rng, key)
        return ''.join(text[pos.index(n)] for n in rng)