import numpy as np
import argparse
import sys
import cv2
import os

from func.facenet import FaceDet

if __name__ == '__main__':

    det = FaceDet()

    while True:

        pt = input('输入图片路径（输入\'exit\'退出）：')
        print(pt)
        if pt == 'exit':
            break
        if not os.path.exists(pt):
            print('路径不存在，请重新输入！')
            continue
        frame = cv2.imread(pt)
        frame = det.detect_and_recognition(frame)
        cv2.imshow('a', frame)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
