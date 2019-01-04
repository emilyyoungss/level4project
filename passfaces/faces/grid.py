import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in colour
img = cv2.imread('old_man.jpg',1)

cv2.imshow('old-man',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


