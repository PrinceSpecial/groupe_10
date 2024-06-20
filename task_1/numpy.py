from typing import Union, List
class Array:
    def __init__(self, data: Union[List[int], List[List[int]]]):
        self.data = data
        for i in data:
            if i == list:
                self.shape = (len(data), len(data[0]))
            else:
                self.shape = (1, len(data))
