import cv2
import numpy as np

res = np.ones((128, 2176, 3))
tile_row = np.ones((128, 128, 3))
for b in range(256):
    # for g in range(0, 256, 16):
    #     for r in range(0, 256, 16):
    color_tile = np.full((128, 128, 3), np.random.randint(0, 255, size=(3,), dtype='uint8'))
    if not b % 16:
        tile_row = color_tile.copy()
    else:
        tile_row = np.hstack([tile_row.copy(), color_tile])

    if b == 15:
        res = tile_row.copy()
        tile_row = np.ones((128, 128, 3))

    elif not (b + 1) % 16:
        res = np.vstack([res, tile_row])

        tile_row = np.ones((128, 128, 3))
        print(res.shape)
        cv2.waitKey(100)

# tileset = tileset.reshape((2 ** 10, 2 ** 10, 3))

np.save('tileset.npy', res)
with open('tileset.npy', 'rb') as tile:
    tileset = np.load(tile)
    print(tileset.shape)
cv2.imshow('tileset', tileset)
cv2.imwrite('tileset.jpg', tileset)
cv2.waitKey(2500)
cv2.destroyAllWindows()