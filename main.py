import streamlit as st
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import glob
import skimage.io
import skimage.color
import skimage.filters
from skimage import morphology
import skimage
from matplotlib import cm
import time
menu = ['Simple thresholding','Otsu thresholding']
import base64
# import inference as inf

# main_bg = "backgroundImg.jpeg"
# main_bg_ext = "jpg"

# side_bg = "backgroundImg.jpeg"
# side_bg_ext = "jpg"

# st.markdown(
#     f"""
#     <style>
#     .reportview-container {{
#         background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )
logo = cv2.imread('logo.png')
logo=cv2.cvtColor(logo,cv2.COLOR_BGR2RGB)
coll1,c,d,e,f,g,h,i,j,m=st.columns(10)
with coll1:
	st.image(logo)

st.sidebar.header('Mode Selection')
choice = st.sidebar.selectbox('Select type of segmentation:', menu)
st.title('Extraction of river networks from satellite images')
immm = st.file_uploader('Upload your satellite image here',type=['jpg','jpeg','png','tif'])

if choice=='Simple thresholding':
	if immm is not None:
		col1, col2=st.columns(2)
		col3 , col4 = st.columns(2)
		image = Image.open(immm)
		img_array = np.array(image)
		with col1:
			st.image(img_array,"Satellite Image")
		
		time.sleep(5) # Sleep for 5 seconds
		# im = cv2.imread(img_array)
		img=cv2.cvtColor(img_array,cv2.COLOR_BGR2RGB)
		img = img/255.0
		im_power_law_transformation = cv2.pow(img,0.6)
		cv2.waitKey(0)
		cv2.waitKey(0)
		image=im_power_law_transformation
		with col2:
			st.image(image,"Enhanced Image")
		time.sleep(5) # Sleep for 5 seconds
		gray_image = skimage.color.rgb2gray(im_power_law_transformation)	
		blurred_image = skimage.filters.gaussian(gray_image, sigma=1.0)
		fig, ax = plt.subplots()
		plt.imshow(blurred_image, cmap='gray')
		histogram, bin_edges = np.histogram(blurred_image, bins=256, range=(0.0, 1.0))
		plt.plot(bin_edges[0:-1], histogram)
		plt.title("Grayscale Histogram")
		plt.xlabel("grayscale value")
		plt.ylabel("pixels")
		plt.xlim(0, 1.0)
		t = 0.4
		binary_mask = blurred_image < t
		fig, ax = plt.subplots()
		selection = np.zeros_like(image)
		selection[binary_mask] = image[binary_mask]
		fig, ax = plt.subplots()
		with col3:
			st.image(selection,"Segmented Image")
		time.sleep(5) # Sleep for 5 seconds
		

		#ClutterRemoval
		# read the image, grayscale it, binarize it, then remove small pixel clusters
		im = selection
		grayscale = skimage.color.rgb2gray(im)
		binarized = np.where(grayscale>0.1, 1, 0)
		processed = morphology.remove_small_objects(binarized.astype(bool), min_size=2, connectivity=2).astype(int)
		# black out pixels
		mask_x, mask_y = np.where(processed == 0)
		im[mask_x, mask_y, :3] = 0
		# plot the result
		plt.figure(figsize=(10,10))
		with col4:
			st.image(im,"After Clutter Removal")
		plt.imsave("segmented.png", im, cmap='Greys')
		with open("segmented.png", "rb") as file1:
			btn = st.download_button(label="Download Segmented Image",data=file1,file_name="thresholding.png",mime="image/png")

elif choice=='Otsu thresholding':
	if immm is not None:
		col1, col2=st.columns(2)
		col3 , col4 = st.columns(2)
		image = Image.open(immm)
		img_array = np.array(image)
		with col1:
			st.image(img_array,"Satellite Image")
		time.sleep(5) # Sleep for 5 seconds
		# im = cv2.imread(img_array)
		img=cv2.cvtColor(img_array,cv2.COLOR_BGR2RGB)
		img = img/255.0
		im_power_law_transformation = cv2.pow(img,0.6)
		cv2.waitKey(0)
		cv2.waitKey(0)
		image=im_power_law_transformation
		with col2:
			st.image(image,"Enhanced Image")
		time.sleep(5) # Sleep for 5 seconds
		# path to input image is specified and
		# image is loaded with imread command
		  
		# cv2.cvtColor is applied over the
		# image input with applied parameters
		# to convert the image in grayscale
		img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
		  
		# applying Otsu thresholding
		# as an extra flag in binary 
		# thresholding     
		ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV + 
		                                            cv2.THRESH_OTSU)     
		 
		# the window showing output image         
		# with the corresponding thresholding         
		# techniques applied to the input image  
		with col3:
			st.image(thresh1,"Segmented Image")
		time.sleep(5) # Sleep for 5 seconds
		se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
		se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
		mask = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, se1)
		mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)

		mask = np.dstack([mask, mask, mask]) / 255
		with col4:
			st.image(mask,"After Clutter Removal")
		# st.write(type(mask))
		# st.write(mask.shape)
		# im = Image.fromarray(np.uint8(cm.gist_earth(mask)*255))
		plt.imsave("segmented.png", mask, cmap='Greys')
		# im = Image.fromarray(mask)
		# st.image(im)
		# im.save('gfg_dummy_pic.png')
		with open("segmented.png", "rb") as file1:
			btn = st.download_button(label="Download Segmented Image",data=file1,file_name="otsu.png",mime="image/png")
elif choice=='Segmentation3':
	if immm is not None:
		immg=Image.open(imm)
		# inf.main(immg)