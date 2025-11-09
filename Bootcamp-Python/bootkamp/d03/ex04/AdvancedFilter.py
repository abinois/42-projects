import numpy
from sys import exit

class AdvancedFilter():
    """Two methods to blur an image as a numpy array."""

    def mean_blur(self, tab, size=3, out=0.2):
        """Tab is numpy array that represents an RVB image.
        Choose the kernel dimension with size (odd).
        To calculate the border's pixels, choose the value of
        the pixels out of range with out (0 >= out <= 1)."""
        if not size % 2 or size < 3:
            exit('Only positive odd number for size.')
        if type(out) is not float or out < 0 or out > 1:
            exit("Only float between 0 and 1 for 'out'.")
        if type(tab) is not numpy.ndarray:
            exit('The input is not a Numpy array.')
            
        kernel = numpy.full((size, size, 3), 1.0)
        offset = size // 2
        cp = numpy.full((tab.shape[0] + size - 1, tab.shape[1] + size - 1, 3), out)
        cp[offset:cp.shape[0] - offset, offset:cp.shape[1] - offset] = tab
        cp2 = numpy.copy(tab)
        for row in range(offset, cp.shape[0] - offset):
            for col in range(offset, cp.shape[1] - offset):
                mini_matrice = numpy.array(cp[row - offset : row + offset + 1, col - offset : col + offset + 1, :])
                for i in range(cp.shape[2]):
                    cp2[row - offset , col - offset, i] = numpy.sum(mini_matrice[:, :, i] * kernel[:, :, i]) / numpy.sum(kernel[:, :, i])
        return cp2

    def gaussian_blur(self, tab, size=5, out=0.2):
        """Tab is numpy array that represents an RVB image.
        Choose the kernel dimension with size (odd).
        To calculate the border's pixels, choose the value of
        the pixels out of range with out (0 >= out <= 1)."""
        if not size % 2 or size < 3:
            exit("Only positive odd number for 'size'.")
        if type(out) is not float or out < 0 or out > 1:
            exit("Only float between 0 and 1 for 'out'.")
        if type(tab) is not numpy.ndarray:
            exit('The input is not a Numpy array.')

        kernel = numpy.zeros((size, size, 3))
        offset = size // 2
        val = 0.5
        for x in range(size):
            val = val * 2 if x <= offset else val // 2
            for y in range(size):
                kernel[x, y] = val
                if y != size - 1:
                    val = val * 2 if y < offset else val // 2
        cp = numpy.full((tab.shape[0] + size - 1, tab.shape[1] + size - 1, 3), out)
        cp[offset:cp.shape[0] - offset, offset:cp.shape[1] - offset] = tab
        cp2 = numpy.copy(tab)
        for row in range(offset, cp.shape[0] - offset):
            for col in range(offset, cp.shape[1] - offset):
                mini_matrice = numpy.array(cp[row - offset : row + offset + 1, col - offset : col + offset + 1, :])
                for i in range(cp.shape[2]):
                    cp2[row - offset , col - offset, i] = numpy.sum(mini_matrice[:, :, i] * kernel[:, :, i]) / numpy.sum(kernel[:, :, i])
        return cp2

if __name__ == '__main__':

    from ImageProcessor import ImageProcessor as ip
    
    imp = ip()
    arr1 = imp.load('../ex03/landscape.png')
    filter = AdvancedFilter()
    imp.display(filter.mean_blur(arr1, 5))
    imp.display(filter.gaussian_blur(arr1, 5))