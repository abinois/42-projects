from numpy import array, full, identity
from numpy.random import random_sample as rs

class NumPyCreator():
    """Numpy array manager"""
    def __init__(self, dtype=None):
        if dtype is not None and type(dtype) is not type:
            exit('{} is an invalid type.'.format(str(dtype)))
        self.dtype = dtype

    def from_list(self, liste):
        if type(liste) is not list:
            exit('Not a list.')
        return array(liste, dtype=self.dtype)

    def from_tuple(self, t):
        if type(t) is not tuple:
            exit('Not a tuple.')
        return array(t, dtype=self.dtype)

    def from_iterable(self, i):
        if not hasattr(i, '__iter__'):
            exit('Not an iterable.')
        return array(i, dtype=self.dtype)

    def from_shape(self, shape, value=0):
        if type(shape) not in (int, tuple):
            exit('Int or tuple expected for shape.')
        return full(shape, value, dtype=self.dtype)
    
    def random(self, shape):
        if type(shape) not in (int, tuple):
            exit('Int or tuple expected for shape.')
        return rs(shape)

    def identity(self, n):
        if type(n) is not int:
            exit('Not an int.')
        return identity(n, dtype=self.dtype)


if __name__ == '__main__':
    npc = NumPyCreator()
    print(npc.from_list([[1,2,3],[6,3,4]]))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))
    shape = (6,3)
    print(npc.from_shape(shape))
    print(npc.random(shape))
    print(npc.identity(4))