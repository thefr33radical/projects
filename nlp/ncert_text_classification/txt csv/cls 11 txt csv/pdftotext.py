# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 14:53:17 2016

@author: Kalyani
"""

mypath ="D:\\NLP_SP\\myPythonCode\\books\\class11"
import os

filelist=[]
txtfile=[]
from PyPDF2 import PdfFileWriter, PdfFileReader
for file in os.listdir(mypath):
    if file.endswith(".pdf"):
        filelist.append(file)
        writefile= file.replace(".pdf",".txt")
        txtfile.append(writefile)


for i in xrange(0, len(txtfile)) :
    pdfFileObj = PdfFileReader(open(filelist[i], "rb"))
    f = open(txtfile[i],'w')
    try :
        j = 0
        while j < pdfFileObj.numPages:
            pageObj = pdfFileObj.getPage(j)
            f.write((pageObj.extractText()).encode('utf-8')+'\n')
            print pageObj.extractText()
            j+=1
    except:
        print ""
    f.close()
        
    
   

