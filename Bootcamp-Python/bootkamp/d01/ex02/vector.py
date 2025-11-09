class Vector():
    """Class du terrible Vector"""

    def __init__(self, liste):
        if type(liste) is not list:
            exit("Vector needs a LIST of values.")
        for val in liste:
            if type(val) is not float:
                exit("Vector needs a list of FLAOT.")
        self.values = liste
        self.length = len(liste)
    
    def __str__(self):
        return ("(Vector " + str(self.values) + ")")

    def __repr__(self):
        return self.__str__()

    def __add__(self, toAdd):
        """will add the value to all values of the vector"""
        if isinstance(toAdd, Vector):
            return Vector([val1 + val2 for val1, val2 in zip(self.values, toAdd.values)])
        elif type(toAdd) is int or type(toAdd) is float:
            return Vector([val + toAdd for val in self.values])
        else:
            exit("Only operations between Vector and Vector/int/float is allowed.")

    def __radd__(self, toAdd):
        """same as __add__"""
        return (self + toAdd)

    def __mul__(self, toMul):
        """will multiply the value to all values of the vector"""
        if isinstance(toMul, Vector):
            return Vector([val1 * val2 for val1, val2 in zip(self.values, toMul.values)])
        elif type(toMul) is int or type(toMul) is float:
            return Vector([val * toMul for val in self.values])
        else:
            exit("Only operations between Vector and Vector/int/float is allowed.")

    def __rmul__(self, toMul):      
        """same as __mul__"""
        return self.__mul__(toMul)

    def __sub__(self, toSub):
        """will substract the value to all values of the vector"""
        if isinstance(toSub, Vector):
            return Vector([val1 - val2 for val1, val2 in zip(self.values, toSub.values)])
        elif type(toSub) is int or type(toSub) is float:
            return Vector([val - toSub for val in self.values])
        else:
            exit("Only operations between Vector and Vector/int/float is allowed.")

    def __rsub__(self, toSub):
        """same as sub but reversed"""
        if isinstance(toSub, Vector):
            return Vector([val2 - val1 for val1, val2 in zip(self.values, toSub.values)])
        elif type(toSub) is int or type(toSub) is float:
            return Vector([toSub - val for val in self.values])
        else:
            exit("Only operations between Vector and Vector/int/float is allowed.")
    
    def __truediv__(self, toDiv):
        """will divide the value to all values of the vector"""
        if isinstance(toDiv, Vector):
            return Vector([val1 / val2 for val1, val2 in zip(self.values, toDiv.values)])
        elif type(toDiv) is int or type(toDiv) is float:
            return Vector([val / toDiv for val in self.values])
        else:
            exit("Only operations between Vector and Vector/int/float is allowed.")

    def __rtruediv__(self, toDiv):
        """same as __truediv__ but reversed"""
        if isinstance(toDiv, Vector):
            return Vector([val2 / val1 for val1, val2 in zip(self.values, toDiv.values)])
        elif type(toDiv) is int or type(toDiv) is float:
            return Vector([toDiv / val for val in self.values])
        else:
            exit("Only operations between Vector and Vector/int/float is allowed.")