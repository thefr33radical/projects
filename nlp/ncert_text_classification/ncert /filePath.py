# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 21:15:18 2016

@author: Kalyani
"""
mypath ="D:\NLP_SP\myPythonCode\NCRT"

#import os

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print onlyfiles
import codecs
from PyPDF2 import PdfFileWriter, PdfFileReader
pdfFileObj = PdfFileReader(open("gess310.pdf", "rb"))
f = open('gess310.txt','w')
j = 0
while j < pdfFileObj.numPages:
    pageObj = pdfFileObj.getPage(j)
    f.write((pageObj.extractText()).encode('utf-8'))
    f.write("  ")
    print pageObj.extractText()
    j+=1
f.close()

#
#
##dirs = os.listdir( mypath )
##print dirs
##import os, glob
#
##for infile in glob.glob( os.path.join(mypath, '*.*') ):
#for infile in onlyfiles:
#    print("current file is: " + infile)
#    #print name.strip()
#    pdfFileObj = PdfFileReader(open(infile, "r"))
#    i=1
#    filename= i+'.txt'
#    print filename
#    f = open(filename,'w')
#    j = 0
#    while j < pdfFileObj.numPages:
#        pageObj = pdfFileObj.getPage(j)
#        #f.write((pageObj.extractText()).encode('utf-8')+'\n')
#        f.write((pageObj.extractText()).encode('utf-8')+' ')
#        print pageObj.extractText()
#        j+=1
#    f.close()
#    i+=1
#
#
