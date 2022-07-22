pip install opencv-python
pip install easyocr
pip install ipython
pip install matplotlib

import easyocr
import cv2
import matplotlib.pyplot as plt
import os
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize']=8,16
# os.getcwd()
# absolute_path = '/Users/ramdu/OneDrive/Desktop'
# os.chdir(absolute_path)

reader=easyocr.Reader(['en'])
Image("image.jpg")
output=reader.readtext('image.jpg')
print(output)

cord=output[-1][0]
x_min,y_min=[min(idx) for idx in zip(*cord)]
x_max,y_max=[max(idx) for idx in zip(*cord)]
image=cv2.imread('image.jpg')
cv2.rectangle(image,(x_min,y_min),(x_max,y_max),(0,0,255),3)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))