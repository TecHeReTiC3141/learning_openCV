import cv2 as cv
sea = cv.imread('../resources/images/sea.jpg')

cv.imshow('sea', sea)

cv.waitKey(0)

capture = cv.VideoCapture('../resources/videos/Fireplace - 1971.mp4')

while True:
    try:
        _, frame = capture.read()
        cv.imshow('Campfire', frame)
    except cv.error as e:
        print(e)
        break

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()