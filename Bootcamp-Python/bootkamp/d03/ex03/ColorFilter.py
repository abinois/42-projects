
from numpy import copy, zeros, linspace, amin, amax, array as a, swapaxes, stack

class ColorFilter():
    """Apply color modification on an numpy array"""

    def invert(self, array):
        cp = copy(array)
        return 1 - cp

    def to_blue(self, array):
        cp= copy(array)
        cp[:, :, :2] = 0
        return cp

    def to_red(self, array):
        cp = copy(array)
        cp[:, :, 1:] = 0
        return cp

    def to_green(self, array):
        cp = zeros(array.shape)
        cp[:, :, 1] = array[:, :, 1]
        return cp

    def celluloid(self, array, nb_shade):
        minr = amin(array[:, :, 0])
        maxr = amax(array[:, :, 0])
        minv = amin(array[:, :, 1])
        maxv = amax(array[:, :, 1])
        minb = amin(array[:, :, 2])
        maxb = amax(array[:, :, 2])
        seqr = a(linspace(minr, maxr, nb_shade))
        seqv = a(linspace(minv, maxv, nb_shade))
        seqb = a(linspace(minb, maxb, nb_shade))
        shade_tab = stack((seqr, seqv, seqb), axis=0).T
        cp = copy(array)
        for line in range(cp.shape[0]):
            for color in range(cp.shape[1]):
                cp[line][color] = self.find_shade(cp[line][color], shade_tab)
        return cp

    def find_shade(self, color, shade_tab):
        difmin = 1000
        res = None
        for shade in shade_tab:
            dif = 0
            for rvb_color, rvb_shade in zip(color, shade):
                dif += abs(rvb_color - rvb_shade)
            if  dif < difmin:
                difmin = dif
                res = shade
        return res




if __name__ == '__main__':

    from ImageProcessor import ImageProcessor as ip
    
    imp = ip()
    filter = ColorFilter()
    # arr1 = imp.load('../ex01/42AI.png')
    arr1 = imp.load('landscape.png')
    #print(arr1.shape)
    imp.display(arr1)
    imp.display(filter.invert(arr1))
    imp.display(filter.to_blue(arr1))
    imp.display(filter.to_red(arr1))
    imp.display(filter.to_green(arr1))
    imp.display(filter.celluloid(arr1, 3))



