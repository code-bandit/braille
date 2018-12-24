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
    left=0
    right=0

    left_offset = get_left_offset(line_img)
    print("leftoffset"+str(left_offset))

    i=left_offset-2
    while i <line_width:
        #print(i)
        for j in range(line_height):
            if line_img[j][i] == 255 and leftfound == False: #if the scanned pixel is white...then thats the first column of that character
                left = i-5
                leftfound = True
                i=i+5
                break

            if line_img[j][i] == 255 and leftfound == True:
                right = i+5
                leftfound = False
                rightfound = False
                cell = line_img[...,left:right]
                cells.append(cell)
                i=i+5
                break

            
            if line_img[j][i] == 255 and i-right>45:#the case where only right column is there
                right = i+5
                left = i-30
                leftfound = False
                rightfound = False
                cell = line_img[...,left:right]
                cells.append(cell)
                i=i+5
                break
            
            if line_img[j][i] == 0 and i -left>39 and leftfound==True:#the case where only the left column exists
                right = i
                left = i-39
                leftfound = False
                rightfound = False
                cell = line_img[...,left:right]
                cells.append(cell)
                break
        i=i+1
    return cells


#create a function to read a cell given its image
def read_cell(cell):#cell is a numpy image which has black background and white braille dots
    #divide the cell into 6 parts
    height = cell.shape[0]
    width = cell.shape[1]
    #1,3,5 in the left column and 2,4,6 in the right column
    cell1 = cell[0:height/3, 0:width/2]
    cell2 = cell[0:height/3, (width/2)+1:width]
    cell3 = cell[(height/3)+1:2*height/3, 0:width/2]
    cell4 = cell[(height/3)+1:2*height/3, (width/2)+1:width]
    cell5 = cell[(2*height/3)+1:height, 0:width/2]
    cell6 = cell[(2*height/3)+1:height, (width/2)+1:width]

    read = []

    if get_white_count(cell1) > 0:
        read.append(1)
    else:
        read.append(0)

    if get_white_count(cell2) > 0:
        read.append(1)
    else:
        read.append(0)

    if get_white_count(cell3) > 0:
        read.append(1)
    else:
        read.append(0)

    if get_white_count(cell4) > 0:
        read.append(1)
    else:
        read.append(0)

    if get_white_count(cell5) > 0:
        read.append(1)
    else:
        read.append(0)

    if get_white_count(cell6) > 0:
        read.append(1)
    else:
        read.append(0)

    return read

def get_white_count(mini_cell):#mini cell is a sixth of a cell numpy array
    whites = 0
    height = mini_cell.shape[0]
    width = mini_cell.shape[1]
    for i in range(height):
        for j in range(width):
            if mini_cell[i][j] == 255:
                whites = whites + 1

    return whites

cells  = read_line(leftres)




leftres = 255 - leftres

print("Number of cells is "+str(len(cells)))
m=0
for cell in cells:
    scipy.misc.imsave('sample_results/cell'+str(m)+'.png', cell)
    m=m+1
scipy.misc.imsave('sample_results/leftres.png', leftres)

