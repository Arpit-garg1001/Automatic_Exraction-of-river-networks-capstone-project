# Automatic_Exraction-of-river-networks-capstone-project
This Project will extract river networks from Landsat images using different image
processing methods. Enhancement, Segmentation and Clutter removal methods will be
implemented using OpenCV.

In this project,
Enhancement is done using power law transformation:- A variety of devices for image capture, printing, and display respond according to a power law. The exponent in power law equation is referred to as gamma Þ process used to correct this power law response phenomena is called gamma correction. eg. CRT devices have intensity.. vs voltage response as a power function with  varying from 1.8 to 2.5. With =2.5, the CRT would produce images darker than intended.

Segmentation is the process of splitting images into multiple layers, represented by a smart, pixel-wise mask is known as Image Segmentation. It involves merging, blocking, and separating an image from its integration level. The segmentation Techniques used are :
 1. Histogram based Thresholding:- The process of thresholding involves comparing each pixel value of the image (pixel intensity) to a specified threshold. This divides all the pixels of the input image into 2 groups:
 Pixels having intensity value lower than threshold.
 Pixels having intensity value greater than threshold.
 These 2 groups are now given different values, depending on varioussegmentation types.
 ![image](https://user-images.githubusercontent.com/74719330/148251735-ce64a561-51e0-49dc-bbf9-e3d2cfdfab6c.png)
 2. Otsu Thresholding:- Otsu's method, named after Nobuyuki Otsu, is used to perform automatic image thresholding. In the simplest form, the algorithm returns a single intensity threshold that separate pixels into two classes, foreground and background. This threshold is determined by minimizing intra-class intensity variance, or equivalently, by maximizing inter-class variance. Otsu's method is a one-dimensional discrete analog of Fisher's Discriminant Analysis, is related to Jenks optimization method, and is equivalent to a globally optimal k-means performed on the intensity histogram.
User can select the type of segmentation

Clutter Removal:-Clutter removal is a process in which small unwanted objects in the image are removed by using an area opening morphological operator. Per the image characteristics, a maximum pixel amount to be imputed. As a result, all objects having fewer than the selected number of pixels will be removed from the image.

System Screenshots:-
![image](https://user-images.githubusercontent.com/74719330/148254620-e6ecd224-ea73-4302-a925-c13fe2cade80.png)
Website Interface with options for choosing different segmentation method
![image](https://user-images.githubusercontent.com/74719330/148254645-dad175cc-abf7-4a40-a818-035b7a97f919.png)
Interface for adding satellite file
![image](https://user-images.githubusercontent.com/74719330/148254718-5d078a50-f60a-4a55-ae8c-17fb27db0d98.png)
Original Image(left) and Enhancement result(right)
![image](https://user-images.githubusercontent.com/74719330/148254808-9ee3e0c9-a612-4fbc-a720-88ffa39215f6.png)
Histogram Thresholding Segmentation result(left), after clutter removal(right)
![image](https://user-images.githubusercontent.com/74719330/148254883-0aa51ed1-b2c7-42c5-b675-799128bcf399.png)
Otsu’s Thresholding result(left), image after clutter removal(right)

