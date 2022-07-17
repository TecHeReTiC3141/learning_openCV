import numpy as np
import cv2
from pathlib import Path

# Rearranging blocks' images
blocks = Path('../minecraft_blocks')
stone = blocks / 'stone'
# if not stone.is_dir():
#     stone.mkdir()
# else:
#     for file in stone.glob('*.png'):
#         file.unlink()

wood = blocks / 'wood'
# if not wood.is_dir():
#     wood.mkdir()
# else:
#     for file in wood.glob('*.png'):
#         file.unlink()

misc = blocks / 'misc'
# if not misc.is_dir():
#     misc.mkdir()
#
# else:
#     for file in misc.glob('*.png'):
#         file.unlink()
#
# for block_nam in blocks.glob('*.png'):
#     scr = Path(block_nam)
#     if 'stone' in scr.stem.lower():
#         dst = stone / scr.name
#     elif 'log' in scr.stem.lower() \
#             or 'planks' in scr.stem.lower():
#         dst = wood / scr.name
#     else:
#         dst = misc / scr.name
#
#     if not dst.exists():
#         dst.touch()
#     print(dst)
#     dst.write_bytes(scr.read_bytes())
#     scr.unlink()

stone_size = (8, 12)
wood_size = (6, 6)
mics_size = (4, 13)

wood_img = np.ones((128, 128 * 12, 3))
tile_row = np.ones((128, 128, 3))
for ind, wood_block in enumerate(wood.glob('*.png')):

    img = cv2.imread(str(wood_block))
    try:
        if not ind % wood_size[1]:
            tile_row = img.copy()
        else:
            tile_row = np.hstack([tile_row, img])

        if ind == wood_size[1] - 1:
            wood_img = tile_row.copy()
            tile_row = np.ones((128, 128, 3))

        elif not (ind + 1) % wood_size[1]:
            wood_img = np.vstack([wood_img, tile_row.copy()])

            tile_row = np.ones((128, 128, 3))
            print(wood_img.shape)
            cv2.imshow(f'Wood {(ind + 1) // wood_size[1]}', wood_img)

    except Exception:
        img = np.zeros((128, 128, 3))
        if not ind % wood_size[1]:
            tile_row = img.copy()
        else:
            tile_row = np.hstack([tile_row, img])

        if ind == wood_size[1] - 1:
            wood_img = tile_row.copy()
            tile_row = np.ones((128, 128, 3))

        elif not (ind + 1) % wood_size[1]:
            wood_img = np.vstack([wood_img, tile_row.copy()])

            tile_row = np.ones((128, 128, 3))
            print(wood_img.shape)


cv2.imshow('Wood_tileset', wood_img)

cv2.imwrite(str(blocks / 'Wood_tileset.png'), wood_img)

cv2.waitKey()
cv2.destroyAllWindows()