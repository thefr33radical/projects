import requests
import json
import os
import glob
import pandas as pd
import base64

def get_method(data,payload):
    if payload is None:
        r = requests.get(url)
        return r.status_code
    r = requests.get(url, params=payload)
    return r.status_code

def post_method(url,payload):
    r = requests.post(url, data=json.dumps(payload))
    return r


    test_mails_non_phishing()

