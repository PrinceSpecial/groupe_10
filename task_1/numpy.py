from typing import Union, List
class Array:
    def __init__(self, data: Union[List[int], List[List[int]]]):
        self.data = data
        for i in data:
            if i == list:
                self.shape = (len(data), len(data[0]))
            else:
                self.shape = (1, len(data))

    def __add__(self, other: "Array"):
        print(len(other.data))
        if self.shape == other.shape:
            return [other.data[i] + self.data[i] for i in range(len(other.data)) if other.data == List[int]]


b = Array([1, 2, 3, 4])
a = Array([1, 2, 3, 4])
c = a + b
print(c)
