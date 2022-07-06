import cv2
import numpy as np

board = cv2.imread('../resources/images/chessboard.png')
board = cv2.resize(board, (0, 0), fx=.75, fy=.75)

corners: np.array = cv2.goodFeaturesToTrack(cv2.cvtColor(board, cv2.COLOR_BGR2GRAY),
                                            100, 0.05, 10).astype('uint16')

corners = np.reshape(corners, (len(corners), 2))


for corn in corners:
    cv2.circle(board, corn, 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        color = tuple(map(int, np.random.randint(0, 255, 3, dtype='uint8')))
        print(color)
        cv2.line(board, tuple(corners[i]), tuple(corners[j]),
                 color, thickness=2)

cv2.imshow('ChessBoard', board)
cv2.waitKey(0)
cv2.destroyAllWindows()
