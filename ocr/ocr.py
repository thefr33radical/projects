import os
import pandas as pd
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import cv2

class OCR(object):
    def __init__(self):
        pass

    def preprocess_image(self):
        image = cv2.imread()

        # --- dilation on the green channel ---
        dilated_img = cv2.dilate(image[:, :, 1], np.ones((7, 7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)

        # --- finding absolute difference to preserve edges ---
        diff_img = 255 - cv2.absdiff(image[:, :, 1], bg_img)

        # --- normalizing between 0 to 255 ---
        norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        cv2.imshow('norm_img', cv2.resize(norm_img, (0, 0), fx=0.5, fy=0.5))
        pass

if __name__=="__main__":
    img = cv2.imread('/home/kuliza227/Downloads/IMG_4057.jpg', 0)
    print((img))
    #text = pytesseract.image_to_string(Image.open('/home/kuliza227/Downloads/IMG_4057.jpg'),lang="eng")
    #print(text)
    pass
