import os
import pytesseract
import cv2
import numpy as np
from PIL import Image

import pyocr
import pyocr.builders

# preprocess steps
# remove noise
# convert to grayscale
# dpi scale


class OCR(object):
    def __init__(self):
        pass

    def increase_dpi(self,path):
        """

        :param path:
        :return:
        """

    def recursive_scanner(self,path):
        """

        :param path:
        :return:
        """
        foldername, filename = os.path.split(path)
        img = Image.open(path, 'r')


        
        for i in range(0,12):
            area = (100, 200+115*i, 1550,(200+115*(i+1)))
            cropped_img = img.crop(area)
            cropped_img.show()
            cropped_img.save(foldername+"/test.jpg")
            self.convert_grayscale(foldername+"/test.jpg")
            self.remove_noise(foldername+"/output.jpg")
            text = pytesseract.image_to_string(Image.open('/home/kuliza227/Downloads/result_.png'), lang="eng")
            print(text)

    def preprocess_image(self):
        """

        :return:
        """
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

    def remove_noise(self,path):
        """
        :param path:
        :return:
        """

        foldername, filename = os.path.split(path)
        img = cv2.imread(path, 0)
        _, blackAndWhite = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

        nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(blackAndWhite, None, None, None, 8,
                                                                             cv2.CV_32S)
        sizes = stats[1:, -1]  # get CC_STAT_AREA component
        img2 = np.zeros((labels.shape), np.uint8)

        for i in range(0, nlabels - 1):
            if sizes[i] >= 10:  # filter small dotted regions
                img2[labels == i + 1] = 255

        res = cv2.bitwise_not(img2)
        cv2.imwrite(foldername+'/result_.png', res)

    def convert_grayscale(self,path):
        """

        :param path:
        :return:
        """

        foldername,filename = os.path.split(path)

        x = Image.open(path, 'r')
        x = x.convert('L')  # makes it greyscale
        y = np.asarray(x.getdata(), dtype=np.float64).reshape((x.size[1], x.size[0]))
        y = np.asarray(y, dtype=np.uint8)  # if values still in range 0-255!
        w = Image.fromarray(y, mode='L')
        w.save(foldername+'/output.jpg')

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
            Image.open('/home/kuliza227/Downloads/demo3.jpg'),
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
    obj.recursive_scanner("/home/kuliza227/Downloads/demo4.jpg")
    ##obj.convert_grayscale('/home/kuliza227/Downloads/demo4.jpg')
    #obj.remove_noise('/home/kuliza227/Downloads/output.jpg')

    #text = pytesseract.image_to_string(Image.open('/home/kuliza227/Downloads/result.png'),lang="eng")
    #print(text)
