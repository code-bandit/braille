from PIL import Image
import json
import numpy as np
import scipy.misc

centroids_file = 'sample_results/centroids.json'
centroids = open(centroids_file, 'r')
if centroids:
    centroids = json.load(centroids)

img = Image.open('sample_results/res.png')
pilimg = np.asarray(img)

side = 10
updown = 10

centrepad = 3


for i in range(50):
    x = centroids[i][1]
    y = centroids[i][0]

    print(i)
    print(x,y)

    if x-side>0 and x+side<pilimg.shape[0] and y-updown>0 and y+updown<pilimg.shape[1]:
        some_portion = pilimg[x-side:x+side, y-updown:y+updown]
        scipy.misc.imsave('sample_results/portion'+ str(i)+'.png', some_portion)