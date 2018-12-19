sample_folder = "../../samples/"
sample_result_folder = "../../sample_results/"

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

sample_path = sample_folder + "test1.png"
sample_result_path = sample_result_folder + "test1_threshbinary.png"
img = cv.imread(sample_path, cv.IMREAD_GRAYSCALE)
# cv.imwrite('test1_result1.png', img)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
cv.imwrite(sample_result_path, thresh1)
# ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
# ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
# ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in range(0,6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()