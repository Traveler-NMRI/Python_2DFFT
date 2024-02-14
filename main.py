import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('./TEST.png') #Load image (e.g. C:/TEST.png)
f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)
mg=20*np.log(np.abs(fshift)) #Convert to grayscale images of order 0-255
plt.subplot(121) 
plt.imshow(img,cmap='gray')
plt.title('original') #Title of the source image
plt.axis('off') #Do not show the axis
plt.subplot(122)
plt.imshow(mg,cmap='gray')
plt.title('result') #Title of the result image
plt.axis('off') #Do not show the axis
plt.show() #Show the result
#----- End of the program -----