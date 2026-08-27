# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import imutils
import cv2
import numpy as np

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#        help="path to the input image")
# args = vars(ap.parse_args())

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread("map3.jpeg")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
kernel = np.ones((5, 5), np.uint8)
# dilation = cv2.dilate(image,ratio,iterations = 2)
# cv2.imwrite("alperennnn.png",dilation)
# convert the resized image to grayscale, blur it slightly,
# and threshold it

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]
#thresh = cv2.bitwise_not(threshed)


# find contours in the thresholded image and initialize the
# shape detector
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

stencil = np.zeros(resized.shape).astype(resized.dtype)
color = [255, 255, 255]
cv2.fillPoly(stencil, contours, color)
result = cv2.bitwise_and(resized, stencil)
result[np.where((result == [0, 0, 0]).all(axis=2))] = [192, 192, 192]
threshed = cv2.threshold(result, 150, 255, cv2.THRESH_BINARY)[1]
threshed = cv2.bitwise_not(threshed)
threshed = cv2.cvtColor(threshed, cv2.COLOR_BGR2GRAY)


cnts = cv2.findContours(threshed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# cv2.drawContours(image, cnts, -1, (0, 255, 0), 3)
sd = ShapeDetector()
cv2.imshow("Image", image)
cv2.waitKey(0)
# loop over the contours
for c in cnts:
    # compute the center of the contour, then detect the name of the
    # shape using only the contour
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    area = cv2.contourArea(c)
    shape = sd.detect(c)
    if shape == "5 cm circle" or shape == "10 cm circle":
        radius = np.sqrt(area / np.pi)
        epsilon = 0.05 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        (x, y), (MA, ma), angle = cv2.fitEllipse(c)
        x *= ratio
        y *= ratio
        radius *= ratio
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(image, center, radius, (255, 0, 0), 2)
        cv2.circle(image, center, 1, (0, 0, 255), thickness=-1)
        cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        #cv2.circle(image, center, 5, (0, 0, 255), thickness=-1)
    else:
        epsilon = 0.05 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        (x, y), (MA, ma), angle = cv2.fitEllipse(c)
        x *= ratio
        y *= ratio

        center = (int(x), int(y))
        approx = approx.astype("float")
        approx *= ratio
        approx = approx.astype("int")
        c = c.astype("float")
        c *= ratio
        c = c.astype("int")
        cv2.circle(image, center, 1, (0, 0, 255), thickness=-1)
        cv2.drawContours(image, [approx], -1, (255, 0, 0), 2)
        cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image

    # show the output image
cv2.imshow("Image", image)
cv2.imwrite("utku2.png", image)
cv2.waitKey(0)
