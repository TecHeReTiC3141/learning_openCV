import numpy as np
import cv2

base_img = cv2.resize(cv2.imread('../resources/images/soccer_practice.jpg',
                      cv2.IMREAD_GRAYSCALE), (0, 0), fx=.8, fy=.8)
shoe = cv2.resize(cv2.imread('../resources/images/shoe.png',
                  cv2.IMREAD_GRAYSCALE), (0, 0), fx=.8, fy=.8)
templ_h, templ_w = shoe.shape


methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in range(len(methods)):
    cop = base_img.copy()
    res = cv2.matchTemplate(cop, shoe, methods[method])

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(method, res.shape, min_loc, max_loc)
    if method >= 4:
        loc = min_loc
    else:
        loc = max_loc
    cv2.rectangle(cop, loc, (loc[0] + templ_w, loc[1] + templ_h), (0, 255, 0), 10, )
    cv2.imshow(f'{method}', cop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()