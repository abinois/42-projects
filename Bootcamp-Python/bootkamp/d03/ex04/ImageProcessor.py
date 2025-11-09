from matplotlib import image as mpli, pyplot as plt, rcParams as rcp
import numpy as np

class ImageProcessor():


    def load(self, file):
        try:
            img = mpli.imread(file)
            print('Loading image of dimensions {} x {}'.format(img.shape[0], img.shape[1]))
            return img
        except:
            exit('Error reading image.')

    def display(self, np_tab):
        if not isinstance(np_tab, np.ndarray):
            exit('Not a Numpy array.')
        rcp['axes.edgecolor'] = 'white' # change all 4 axes color
        rcp['axes.linewidth'] = 1.2
        rcp['figure.facecolor'] = 'black' # background color
        rcp['xtick.bottom'] = rcp['ytick.left'] = False  # hide little ticks
        plt.title('VOICI UNE IMAGE', {'fontname':'Charter', 'color':'white', 'fontsize':17.0, 'verticalalignment':'bottom'}) # params for title
        plt.xlabel('x', {'fontname':'Arial', 'color':'pink', 'fontsize':13.0}) # params for x axe
        plt.ylabel('y', {'fontname':'Arial', 'color':'pink', 'fontsize':13.0}) # params for y axe
        plt.xticks([]) # clear numbers
        plt.yticks([])
        rcp['keymap.quit'] = 'q' # map exit on 'q'
        plt.imshow(np_tab)
        plt.show()

if __name__ == '__main__':
    imp = ImageProcessor()
    arr1 = imp.load('42AI.png')
    arr2 = imp.load('42.png')
    print(arr1)
    imp.display(arr1)
    imp.display(arr2)
