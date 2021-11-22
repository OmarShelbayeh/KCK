import matplotlib.image as mpimg
from pylab import *
from skimage import feature
import matplotlib.pyplot as plt
def find(x, y, z, u, i):
    image = mpimg.imread(x)
    fig, ax = plt.subplots(2, 1)
    ax[0].imshow(image)
    params = [(q[0], q[1], q[2]) for q in feature.blob_dog(-image.mean(axis=2), y, z, threshold=u, overlap=i)]

    for param in params:
        y, x, r = param
        c = plt.Circle((x, y), r+2, color='blue', linewidth=1.5, fill=False)
        ax[1].add_patch(c)
    plt.imshow(image)
    ax[0].axis('off')
    ax[1].axis('off')
    plt.title('liczba oczek: ' + str(len(params)))
    plt.show()

find('kostki.jpg', 7, 15, 233, 0.6)
find('kostki2.jpg', 15, 23, 130, 0.6)
find('kostki3.jpg', 7, 15, 233, 0.6)
find('kostki4.jpg', 14, 17, 331, 0.6)
find('kostki5.jpg', 7, 15, 263, 0.6)
find('kostki6.jpg', 7, 17, 230, 0.6)
find('kostki7.jpg', 7, 17, 170, 0.6)
find('kostki8.jpg', 8.5, 17, 261, 0.6)
