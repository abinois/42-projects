import numpy as np

class ScrapBooker():
    """Numpy array reshaper"""
    def crop(self, array, dimensions, position=(0,0)):
        """Crop array from position to dimensions."""
        for i in range(2):
            if position[i] + dimensions[i] > array.shape[i]:
                exit('Dimensions too big.')
            return np.array([elem[position[1]:position[1] + dimensions[1]:] for elem in array[position[0]:position[0] + dimensions[0]:]])

    def thin(self, array, n, axis):
        """Delete a row or a column, each n."""
        to_del = [i for i, elem in enumerate((array, array[0])[axis]) if not (i + 1) % n] 
        return np.delete(array, to_del, axis=axis)
        # return np.delete(array, np.s_[::n], axis) # problem avec cette methode: suppr la 0-index row/column

    def juxtapose(self, array, n, axis):
        """Juxtapose n copy of array along the specified axe."""
        big_list = []
        for _ in range(n):
            big_list.append(array)
        return np.concatenate(tuple(big_list), axis=axis)

    def mosaic(self, array, dimensions):
        """Create a big array of concatenated copy of array"""
        row = self.juxtapose(array, dimensions[1], 1)
        return self.juxtapose(row, dimensions[0], 0)

if __name__=='__main__':
    matrix = np.array([
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
        [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]])
    sb = ScrapBooker()
    print(matrix)
    print(sb.crop(matrix, (3, 3), position=(1, 1)))
    print(sb.thin(matrix, 3, 0))
    print(sb.thin(matrix, 3, 1))
    print(sb.juxtapose(matrix, 3, 0))
    print(sb.mosaic(matrix, (2, 2)))