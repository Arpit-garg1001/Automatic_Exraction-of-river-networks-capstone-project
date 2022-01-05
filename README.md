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
 
![0](https://user-images.githubusercontent.com/74719330/148257978-31b1d68e-c8a1-4cca-8cc0-599545df2dd1.png)

 2. Otsu Thresholding:- Otsu's method, named after Nobuyuki Otsu, is used to perform automatic image thresholding. In the simplest form, the algorithm returns a single intensity threshold that separate pixels into two classes, foreground and background. This threshold is determined by minimizing intra-class intensity variance, or equivalently, by maximizing inter-class variance. Otsu's method is a one-dimensional discrete analog of Fisher's Discriminant Analysis, is related to Jenks optimization method, and is equivalent to a globally optimal k-means performed on the intensity histogram.
User can select the type of segmentation

Clutter Removal:-Clutter removal is a process in which small unwanted objects in the image are removed by using an area opening morphological operator. Per the image characteristics, a maximum pixel amount to be imputed. As a result, all objects having fewer than the selected number of pixels will be removed from the image.

System Screenshots:-
![1](https://user-images.githubusercontent.com/74719330/148256672-566ed875-967b-43a4-baf8-f394d72d5ef2.png)
Website Interface with options for choosing different segmentation method

![2](https://user-images.githubusercontent.com/74719330/148256727-6540348c-16b2-4a33-bbe2-faf9c31d321d.png)
Interface for adding satellite file

![3](https://user-images.githubusercontent.com/74719330/148257287-1960b50d-b2de-4b65-ac4f-61ff296e3f9d.png)
Original Image(left) and Enhancement result(right)

![4](https://user-images.githubusercontent.com/74719330/148257303-756b14c2-8c67-4411-8a68-d2c609ebed78.png)
Histogram Thresholding Segmentation result(left), after clutter removal(right)

![5](https://user-images.githubusercontent.com/74719330/148257368-cee84825-5b1f-455f-90df-acb3dcd3f23c.png)
Otsu’s Thresholding result(left), image after clutter removal(right)

