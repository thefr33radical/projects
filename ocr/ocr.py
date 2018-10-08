import os
import pandas as pd
import pyocr
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import cv2
from PIL import Image
import sys

import pyocr
import pyocr.builders

# preprocess steps
# remove noise
# convert to grayscale
# dpi scale


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


    def remove_noise(self,img):
        pass

    def load_image(self):
        """

        :return:
        """


        tools = pyocr.get_available_tools()
        # The tools are returned in the recommended order of usage
        tool = tools[0]

        langs = tool.get_available_languages()
        lang = langs[0]
        # Note that languages are NOT sorted in any way. Please refer
        # to the system locale settings for the default language
        # to use.

        txt = tool.image_to_string(
            Image.open('/home/kuliza227/Downloads/demo300.jpg'),
            lang="eng",
            builder=pyocr.builders.TextBuilder()
        )
        # txt is a Python string
        print(txt)
        '''word_boxes = tool.image_to_string(
            Image.open('/home/kuliza227/Downloads/IMG_4056_sized.jpg'),
            lang="eng",
            builder=pyocr.builders.WordBoxBuilder()
        )
        # list of box objects. For each box object:
        #   box.content is the word in the box
        #   box.position is its position on the page (in pixels)
        #
        # Beware that some OCR tools (Tesseract for instance)
        # may return empty boxes
        '''
        line_and_word_boxes = tool.image_to_string(
            Image.open('/home/kuliza227/Downloads/IMG_4057_sized.jpg'), lang="eng",
            builder=pyocr.builders.LineBoxBuilder()
        )
        #print(line_and_word_boxes[0])
        # list of line objects. For each line object:
        #   line.word_boxes is a list of word boxes (the individual words in the line)
        #   line.content is the whole text of the line
        #   line.position is the position of the whole line on the page (in pixels)
        #
        # Beware that some OCR tools (Tesseract for instance)
        # may return empty boxes
        '''
        # Digits - Only Tesseract (not 'libtesseract' yet !)
        digits = tool.image_to_string(
            Image.open('test-digits.png'),
            lang=lang,
            builder=pyocr.tesseract.DigitBuilder()
        )
        # digits is a python string
        '''

if __name__=="__main__":
    obj=OCR()
    #obj.load_image()
    #img = cv2.imread('/home/kuliza227/Downloads/IMG_4056_sized.jpg', 0)
    #print((img))
    text = pytesseract.image_to_string(Image.open('/home/kuliza227/Downloads/demo2.jpg'),lang="eng")
    print(text)
    pass
