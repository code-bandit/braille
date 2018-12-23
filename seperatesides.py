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

    print(i)
    print(x,y)

    if x-side>0 and x+side<pilimg.shape[0] and y-updown>0 and y+updown<pilimg.shape[1]:
        some_portion = pilimg[x-side:x+side, y-updown:y+updown]
        scipy.misc.imsave('sample_results/portions/'+ str(i)+'.png', some_portion)




# height = leftres.shape[0]
# width = leftres.shape[1]

# #find the offset from the left side and the top
# def get_top_offset(img, height, width):
#     for i in range(height):
#         for j in range(width):
#             if img[i][j]==255:
#                 return i

#     return None

def get_left_offset(img):#img is a numpy array
    height = img.shape[0]
    width = img.shape[1]
    for i in range(width):
        for j in range(height):
            if img[j][i]==255:
                return i

    return None

max_scan_width = 60



def read_line(line_img):#line_img is a numpy array of a line out of the braille sheet
    cells = []
    line_height = line_img.shape[0]
    line_width = line_img.shape[1]
    
    leftfound = False
    rightfound = False

    left_offset = get_left_offset(line_img)
    print("leftoffset"+str(left_offset))

    for i in range(left_offset-2, line_width):
        for j in range(line_height):
            if line_img[j][i] == 255 and leftfound == False: #if the scanned pixel is white...then thats the first column of that character
                left = i-5
                leftfound = True
                break

            if line_img[j][i] == 255 and leftfound == True:
                right = i+5
                leftfound = False
                rightfound = False
                cell = line_img[...,left:right]
                cells.append(cell)
                break

            
            if line_img[j][i] == 255 and i-right>45:#the case where only right column is there
                right = i+5
                left = i-30
                leftfound = False
                rightfound = False
                cell = line_img[...,left:right]
                cells.append(cell)
                break
            
            if line_img[j][i] == 255 and i -left>33:#the case where only the left column exists
                right = i+33
                left = i-2
                leftfound = False
                rightfound = False
                cell = line_img[...,left:right]
                cells.append(cell)
                break

    return cells


#create a function to read a cell given its image


cells  = read_line(leftres)

leftres = 255 - leftres

print("Number of cells is "+str(len(cells)))
m=0
for cell in cells:
    scipy.misc.imsave('sample_results/cell'+str(m)+'.png', cell)
    m=m+1
scipy.misc.imsave('sample_results/leftres.png', leftres)

