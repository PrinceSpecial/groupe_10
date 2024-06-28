from typing import Union, List
from ErrorHandler import *
import sys

sys.excepthook = custom_exception_hook

# print("Custom numpy module imported")

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

    def __str__(self):
        return self.__repr__()
        
    def __add__(self, other: "Array"):
        return self.operation(other, lambda x, y: x + y, "Addition")
    
    def __sub__(self, other: "Array"):
        return self.operation(other, lambda x, y: x - y, "Soustraction")
    
    def __mul__(self, other: "Array"):
        return self.operation(other, lambda x, y: x * y, "Multiplication")
    
    def __truediv__(self, other: "Array"):
        return self.operation(other, lambda x, y: x / y, "Division")
        
    def operation(self, other, operation, operation_name):
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError("Erreur : " + operation_name + " doit etre fait entre des tableau de meme shape")
            if len(self.shape) == 1:
                return Array([operation(x, y) for x, y in zip(self.data, other.data)])
            else:
                return Array([[operation(x, y) for x, y in zip(row, other_row)] for row, other_row in zip(self.data, other.data)])
        else:
            if len(self.shape) == 1:
                return Array([operation(x, other) for x in self.data])
            else:
                return Array([[operation(x, other) for x in row] for row in self.data])
            
    def __len__(self):
        return len(self.data)
    
    def __matmul__(self, other):
        if not isinstance(other, Array):
            raise TypeError("Le produit scalaire est fait sur deux Arrays")
        if len(self.shape) != 1 or len(other.shape) != 1:
            raise ValueError("Produit scalaire supporté pour les 1D, veuillez reesayer avec un array 1D")
        if len(self) != len(other):
            raise ValueError("Les deux Arrays doivent avoir la même longueur")
        
        return sum(x * y for x, y in zip(self.data, other.data))
