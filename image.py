import numpy as np
from matplotlib import pyplot as plt

from math import sqrt
from copy import deepcopy
import cv2
print('loading image...')
L = cv2.imread('amumu.jpg', cv2.IMREAD_GRAYSCALE)
# print(L)
cv2.imwrite('origin_gray.jpg', L)
# print(L.shape)
# print(type(L))
# print(L.shape)
print('calculating HOG algorithm...')
ans = deepcopy(L)
height, width = L.shape
for i in range(len(L)):
    for j in range(len(L[i])):
        if i == 0:
            gy = int(L[i + 1][j])
        elif i == height - 1:
            gy = int(L[i - 1][j])
        else:
            gy = int(L[i + 1][j]) - int(L[i - 1][j])

        if j == 0:
            gx = int(L[i][j + 1])
        elif j == width - 1:
            gx = int(L[i][j - 1])
        else:
            gx = int(L[i][j + 1]) - int(L[i][j - 1])
        ans[i][j] = sqrt(gx ** 2 + gy ** 2)

cv2.imwrite('output.jpg', ans)
ans2 = deepcopy(ans)
for i in range(len(ans)):
    for j in range(len(ans[i])):
        if ans[i][j] > 20:
            ans2[i][j] = 0
        else:
            ans2[i][j] = 255
cv2.imwrite('edge.jpg', ans2)
print('finish')
# cv2.imshow('edge result', ans2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(ans2, cmap = 'gray')
plt.show()