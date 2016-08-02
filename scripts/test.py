#!/usr/bin/env python

import cv2

SERTAC_IMG = cv2.resize(cv2.imread('sertac.png',0), (100,100), interpolation = cv2.INTER_AREA)

cv2.imshow("Sertac",SERTAC_IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()