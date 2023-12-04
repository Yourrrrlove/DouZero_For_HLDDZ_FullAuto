import GameHelper as gh
from GameHelper import GameHelper
import cv2
import numpy as np

GameHelper = GameHelper()
GameHelper.ScreenZoomRate = 1.0
img, _ = GameHelper.Screenshot()
# img = cv2.imread("15.png")
img = cv2.cvtColor(np.asarray(img), cv2.COLOR_BGR2RGB)

# img, _ = GameHelper.Screenshot()
img = gh.DrawRectWithText(img, (192, 725, 1448, 200), "test")
# cv2.imwrite("111.png", img)
gh.ShowImg(img)
