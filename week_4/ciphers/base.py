from abc import ABC, abstractmethod


class Cipher(ABC):

    @staticmethod
    @abstractmethod
    def encode(text, key):
        pass

    @staticmethod
    @abstractmethod
    def decode(text, key):
        pass