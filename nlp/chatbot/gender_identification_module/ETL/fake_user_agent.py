# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:04:36 2017

@author: gowtham
"""

from fake_useragent import UserAgent
import requests

ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
print(header)
