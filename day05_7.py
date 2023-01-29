# import가 안되는 이유 : 설치가 안된 라이브러리(모듈) 또는 오타
# 외부 모듈 설치 : pip install 모듈명

# pip install python-opencv (아나콘다 파이썬)
# pip install opencv-python (아나콘다 파이썬)
import cv2


def cv_img(path):
    이미지 = cv2.imread(path)
    cv2.imshow('title', 이미지)
    cv2.waitKey(0)

cv_img('../wrx.jpg')