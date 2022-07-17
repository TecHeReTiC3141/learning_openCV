import cv2
import numpy as np
from time import localtime, asctime

capture = cv2.VideoCapture(2)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades
                                     + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades
                                    + 'haarcascade_eye.xml')
# glasses_cascade = cv2.CascadeClassifier(cv2.data.haarcascades
#                                     + 'haarcascade_eye_tree_eyeglasses.xml')
while True:

    _, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(35, 35))
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h),
                      (0, 255, 0), 6, )
        roi = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi, 1.1, 6, minSize=(10, 10))
        # glasses = glasses_cascade.detectMultiScale(roi, 1.1)
        # print(eyes, glasses)

        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh),
                          (255, 0, 0), 3)
        # for ex, ey, ew, eh in glasses:
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh),
        #                   (0, 0, 255), 3)

    cv2.putText(frame, asctime(localtime()), (5, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), thickness=2,
                lineType=cv2.LINE_AA)
    cv2.imshow('VideoCam', frame)

    if cv2.waitKey(20) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
