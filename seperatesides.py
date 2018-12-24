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

leftres = np.zeros((pilimg.shape[0],pilimg.shape[1]))

side = 10
updown = 10

centrepad = 3

for i in range(len(centroids)-1):
    x = centroids[i][1]
    y = centroids[i][0]
    
    leftres[x][y] = 255

leftres = leftres[175:leftres.shape[0],...]

def seperateintolines(img):
    height = img.shape[0]
    width = img.shape[1]

    updown = 60

    upfound = True
    lines = []

    i=0

    while i < height:
        for j in range(width):
            if img[i][j] == 255:
                line = img[i-10:i+70,...]
                lines.append(line)
                scipy.misc.imsave('sample_results/lines/'+str(len(lines)) +'.png', line)
                i=i+70
                break
        i=i+1

seperateintolines(leftres)
scipy.misc.imsave('sample_results/leftresseperate.png', leftres)