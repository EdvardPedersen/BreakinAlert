import time
import cv2 as cv

webcam = cv.VideoCapture(0)
last_frame = None

''' Things to review

cv.VideoCapture - to get the web camera
cv.VideoCapture.read - to read from the web camera
cv.cvtColor - to convert to grayscale
cv.image.copy - to copy an image
cv.absdiff - to get the difference between two images
cv.reduce - to average the dimensions of the image
cv.imwrite - to write image to disk
time.strftime - to get the current time

cv.imshow - to show an image
cv.waitKey - to wait for a keypress (and update windows)

Functions
Return values
Images
Strings
Global variables
'''


def get_webcam_image():
    '''
    Gets a single image from the web camera in grayscale
    '''
    ret, frame = webcam.read()
    if not ret:
        return last_frame
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

def get_difference(image1, image2):
    '''
    Get difference between two images
    '''
    diff = image1.copy()
    cv.absdiff(image1, image2, diff)
    reduction = cv.reduce(diff, 0, cv.REDUCE_AVG)
    reduction = cv.reduce(reduction, 1, cv.REDUCE_AVG)
    return reduction

def get_current_time():
    return time.strftime("%Y%m%d-%H:%M:%S")

last_frame = get_webcam_image()
since_last = 0

while True:
    new_image = get_webcam_image()
    reduction = get_difference(new_image, last_frame)
    if reduction > 10 and since_last > 10:
        print("GOTCHA!")
        cv.imwrite("{}.jpg".format(get_current_time()), new_image)
        since_last = 0

    since_last += 1
    last_frame = new_image
