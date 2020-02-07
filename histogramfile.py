'''
CBIR
https://www.youtube.com/watch?v=vsaHwpYP7wQ'''
import numpy as np
from PIL import Image
import os

histogramdict = {}

for i in np.arange(0,1000):
    photo = str(i) + '.jpg'
    if os.path.isfile(photo):
        spec_photo = Image.open(photo)
        histogramdict[photo] = spec_photo.histogram()
    else:
        continue

file = open('histodict.txt','w')
file.write(str(histogramdict))