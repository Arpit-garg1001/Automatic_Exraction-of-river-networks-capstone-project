import cv2
import numpy as np
import matplotlib.pyplot as plt
im = cv2.imread('landsat1.tif')
cv2.imshow("origi",im)
img=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
img = img/255.0
im_power_law_transformation = cv2.pow(img,0.6)
plt.imshow(img)
cv2.waitKey(0)
plt.imshow(im_power_law_transformation)
cv2.waitKey(0)
import glob
import skimage.io
import skimage.color
import skimage.filters


# load the image
image = skimage.io.imread("landsat1.tif")
image=im_power_law_transformation
gray_image = skimage.color
histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))

plt.plot(bin_edges[0:-1], histogram)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim(0, 1.0)
plt.show()
t = 0.4
binary_mask = blurred_image < t

fig, ax = plt.subplots()
plt.imshow(binary_mask, cmap='gray')

plt.show()
selection = np.zeros_like(image)
selection[binary_mask] = image[binary_mask]

fig, ax = plt.subplots()
plt.imshow(selection)
cv2.imshow("selectn.jpg",image)
plt.show()