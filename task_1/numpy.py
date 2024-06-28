from typing import Callable, Union, List, Tuple
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

    def __repr__(self) -> str:
        return f"Array({self.data})"

    def __str__(self) -> str:
        return self.__repr__()
        
    def __add__(self, other: "Array") -> "Array":
        return self.operation(other, lambda x, y: x + y, "Addition")
    
    def __sub__(self, other: "Array") -> "Array":
        return self.operation(other, lambda x, y: x - y, "Soustraction")
    
    def __mul__(self, other: "Array") -> "Array":
        return self.operation(other, lambda x, y: x * y, "Multiplication")
    
    def __truediv__(self, other: "Array") -> "Array":
        return self.operation(other, lambda x, y: x / y, "Division")
        
    def operation(self, other: "Array", operation: Callable[[int, int], int], operation_name: str) -> "Array":
        if isinstance(other, Array):
            if self.shape != other.shape:
                raise ValueError(f"Erreur : {operation_name} doit etre fait entre des tableau de meme shape")
            if len(self.shape) == 1:
                return Array([operation(x, y) for x, y in zip(self.data, other.data)])
            else:
                return Array([[operation(x, y) for x, y in zip(row, other_row)] for row, other_row in zip(self.data, other.data)])
        else:
            if len(self.shape) == 1:
                return Array([operation(x, other) for x in self.data])
            else:
                return Array([[operation(x, other) for x in row] for row in self.data])
            
    def __len__(self) -> int:
        return len(self.data)
    
    def __matmul__(self, other: "Array") -> int:
        if not isinstance(other, Array):
            raise TypeError("Le produit scalaire est fait sur deux Arrays")
        if len(self.shape) != 1 or len(other.shape) != 1:
            raise ValueError("Produit scalaire supporté pour les 1D, veuillez reesayer avec un array 1D")
        if len(self) != len(other):
            raise ValueError("Les deux Arrays doivent avoir la même longueur")
        
        return sum(x * y for x, y in zip(self.data, other.data))
    
    def __contains__(self, item: Union[int, float]) -> bool:
        if len(self.shape) == 1:
            return item in self.data
        else:
            return any(item in row for row in self.data)
        
    def __getitem__(self, index: Union[int, slice, Tuple[Union[int, slice], ...]]) -> Union[int, float, "Array"]:
        if isinstance(index, tuple):
            if len(self.shape) == 1:
                raise IndexError("Trop d'indices, c'est un array 1D")
            if len(index) != 2:
                raise IndexError("Trop d'indices")
            row_index, col_index = index

            if isinstance(row_index, slice):
                rows = self.data[row_index]
            else:
                rows = [self.data[row_index]]

            result = [row[col_index] for row in rows]
            
            if len(result) == 1:
                result = result[0]
            
            return Array(result) if isinstance(result, list) else result
        else:
            if isinstance(index, slice):
                return Array(self.data[index])
            else:
                if index >= len(self.data):
                    raise IndexError("Indice hors de portée")
                return self.data[index]

