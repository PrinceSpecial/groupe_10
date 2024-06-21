from typing import Union, List
from ErrorHandler import *
import sys

sys.excepthook = custom_exception_hook

class Array:
    def __init__(self, data: Union[List[int], List[List[int]]]):
        if not isinstance(data, list):
            raise InvalidDataError()
        self.data = data

        # Verifiez si c'est 1D ou 2D
        if all(isinstance(i, list) for i in data):
            # Verifiez si c'est 2D
            if any(isinstance(j, list) for row in data for j in row):
                raise InvalidDataError()
            self.shape = (len(data), len(data[0]))
        else:
            # Verifiez si c'est 1D
            if any(isinstance(i, list) for i in data):
                raise InvalidDataError()
            self.shape = (len(data),)

        # La longueur dans 2D doit etre la meme
        if len(self.shape) == 2:
            if any(len(row) != self.shape[1] for row in data):
                raise ValueError("Toutes les lignes du tableau 2D doivent avoir la même longueur.")

    def __repr__(self):
        return f"Array({self.data})"


# Test
f = Array([[4,4],[4]])
print(f)
print(f.shape)

f = Array([[4,4],[2, 1]])
print(f)
print(f.shape)

