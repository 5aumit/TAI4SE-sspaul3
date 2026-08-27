import cv2
import time
from imutils.video import VideoStream
import imutils

#fuction that should be run as a thread and that interrupts when motion is detected
def MotionDetectionThread(thresholdBackground, minAreaToBeDetectedBackground,
                          thresholdMotion, minAreaToBeDetectedMotion,frameUpdateFreq):

    videoStr = VideoStream(src = 0).start()
    time.sleep(3)

    print("Created video stream")

    firstFrame              = None
    mostRecentMotionFrame   = None
    grayFrame               = None

    frameUpdateCounter = 0


    consecutiveMotionDetected = 0
    consecutiveNoMotion       = 0

    #Loop forever trying to detect motion
    while True:

        frameUpdateCounter += 1

        if frameUpdateCounter == frameUpdateFreq:
            mostRecentMotionFrame = grayFrame
            frameUpdateCounter = 0


        #print("CALCULATING FRAMES")
        hasDiffToFirst   = False
        hasDiffToLast    = False

        currentFrame = videoStr.read()

        if currentFrame is None:
            print("Received empty frame")
            break

        # Resize, convert to gray scale and blur to smooth out and ease calculations
        currentFrame = imutils.resize(currentFrame, width=500)
        grayFrame    = cv2.cvtColor(currentFrame,cv2.COLOR_BGR2GRAY)
        grayFrame    = cv2.GaussianBlur(grayFrame, (21,21), 0)

        if firstFrame is None:
            firstFrame            = grayFrame
            mostRecentMotionFrame = grayFrame
            continue


        ## --- CALCULATES DIFF TO LAST UPDATED FRAME ---

        # Calculate Diff between current frame and last frame
        frameDiff     = cv2.absdiff(mostRecentMotionFrame, grayFrame)
        frameThresh = frameDiff

        # Remove frame diff below the threshold
        frameThresh   = cv2.threshold(frameDiff, thresholdMotion, 255, cv2.THRESH_BINARY)[1]

        # Dilating image to fill the possible holes between pixel groups
        frameThresh   = cv2.dilate(frameThresh, None, iterations=2)

        # Calculating contours of the moving pixels
        frameContours = cv2.findContours(frameThresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        frameContours = frameContours[0] if imutils.is_cv2() else frameContours[1]

        # Loop over every contour in the frame

        for contour in frameContours:

            # If the contour is bigger than minArea, than there is motion
            if cv2.contourArea(contour) < minAreaToBeDetectedMotion:
                continue

            hasDiffToLast = True

        ## --- CALCULATES DIFF TO FIRST FRAME ---

        # Calculate Diff between current frame and starting frame
        frameDiff     = cv2.absdiff(firstFrame, grayFrame)

        # Remove frame diff below the threshold
        frameThresh   = cv2.threshold(frameDiff, thresholdBackground, 255, cv2.THRESH_BINARY)[1]

        # Dilating image to fill the possible holes between pixel groups
        frameThresh   = cv2.dilate(frameThresh, None, iterations=2)

        # Calculating contours of the moving pixels
        frameContours = cv2.findContours(frameThresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        frameContours = frameContours[0] if imutils.is_cv2() else frameContours[1]


        # Loop over every contour in the frame

        for contour in frameContours:

            # If the contour is smaller than minArea, it is ignored
            if cv2.contourArea(contour) < minAreaToBeDetectedBackground:
                continue

            hasDiffToFirst = True


        if hasDiffToLast:
            consecutiveMotionDetected += 1
            consecutiveNoMotion = 0

            if consecutiveMotionDetected > 40:
                print("MOTION DETECTED")
                consecutiveMotionDetected = 0
        else:
            consecutiveMotionDetected = 0
            consecutiveNoMotion += 1

            if consecutiveNoMotion > 40:
                print("NO MOTION")
                consecutiveNoMotion = 0

                if hasDiffToFirst:
                    print("SOMETHING WAS LEFT")

        frameUpdateCounter += 1

    videoStr.stop()


MotionDetectionThread(100, 500, 10, 50, 100)








