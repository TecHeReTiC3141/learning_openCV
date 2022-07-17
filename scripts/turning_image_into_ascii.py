import cv2
import numpy as np

capture = cv2.VideoCapture(2)
print(capture.get(3), capture.get(4))
seg_size = 10
ascii_symbs = ('Ñ@#W$9876543210?!abc;:+=-,._    ')[::-1]
bright_per_symb = 256 // len(ascii_symbs)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades
                                     + 'haarcascade_frontalcatface.xml')
x = 0
while True:

    tr, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #
    # faces = face_cascade.detectMultiScale(gray, 1.05, 6, minSize=(30, 30))
    # gray = gray.astype('int16')
    # for x, y, width, height in faces:
    #     gray[y:y + height, x:x + width] += 64
    #
    # np.clip(gray, 0, 255)
    # gray = gray.astype('int8')

    mean_seg = np.zeros((gray.shape[0] // seg_size, gray.shape[1] // seg_size), dtype='uint8')
    blank = np.zeros(gray.shape, dtype='uint8')
    ascii_img = cv2.resize(np.zeros(gray.shape, dtype='uint8'), (0, 0), fx=1, fy=1.5)

    for i in range(0, gray.shape[0], seg_size):
        cur_str = ''
        for j in range(0, gray.shape[1], seg_size):
            mean_seg[i // seg_size, j // seg_size] = gray[i:i + seg_size, j:j + seg_size].mean()
            me = int(mean_seg[i // seg_size, j // seg_size])
            cv2.rectangle(blank, (j, i), (j + seg_size, i + seg_size),
                          tuple(me for _ in '...'), -1)
            cur_str += ascii_symbs[me // bright_per_symb]

        cv2.putText(ascii_img, cur_str, (0, int((i + seg_size) * 1.5)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1, cv2.LINE_AA)
        if x == 5:
            print(cur_str)


    blank_res = cv2.resize(blank, (0, 0), fx=1.5, fy=1.5)
    ascii_res = cv2.resize(ascii_img, (0, 0), fx=1, fy=1)

    cv2.imshow('Rects', blank_res)
    cv2.imshow('Ascii', ascii_res)

    if cv2.waitKey(5) == ord('q'):
        break
    x += 1
capture.release()
cv2.destroyAllWindows()
