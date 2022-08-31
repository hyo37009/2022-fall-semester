import numpy as np
from PIL import Image

img = Image.open('testmap1.jpg')
img.show()

x = np.array(img)
print(x)
print(x.shape)


