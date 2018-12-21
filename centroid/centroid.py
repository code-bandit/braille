sample_folder = "../samples/"
sample_result_folder = "../sample_results/"
import cv2 as cv

sample_path = sample_folder + "img009.jpg"
img = cv.imread(sample_path, cv.IMREAD_GRAYSCALE)
_,img = cv.threshold(img,0,255,cv.THRESH_OTSU)
h, w = img.shape[:2]
# cv.waitKey(0)
# cv.destroyAllWindows()
im2, contours0, hierarchy = cv.findContours( img.copy(), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
moments  = [cv.moments(cnt) for cnt in contours0]
# Nota Bene: I rounded the centroids to integer.
# cv.drawContours(img, contours0, -1, (0,255,0), 3)
# centroids = [( int(round(m['m10']/m['m00'])),int(round(m['m01']/m['m00'])) ) for m in moments]
centroids = []
for m in moments:
    if m['m00']:
        centroids.append((int(round(m['m10']/m['m00'])), int(round(m['m01']/m['m00']))))

# print(len(centroids))
print('cv2 version:', cv.__version__)
print('centroids:', centroids)

for c in centroids:
    # print(c)
    # I draw a black little empty circle in the centroid position
    cv.circle(img,c,5,(0,0,0))

cv.imshow('image', img)
0xFF & cv.waitKey()
cv.destroyAllWindows()