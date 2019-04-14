import glob
import os
import email
import pandas as pd
import json


def convert():
    for file in glob.glob(os.path.join("", "*.txt")):
        foldername, filename = os.path.split(file)
        print(filename)
        f2 = open("" + str(filename), "r")
        data = f2.read()
        # print(data)

        b = email.message_from_string(data)
        if b.is_multipart():
            for part in b.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                # skip any text/plain (txt) attachments
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    body = part.get_payload(decode=True)  # decode
                    break
        # not multipart - i.e. plain text, no attachments, keeping fingers crossed
        else:
            body = b.get_payload(decode=True)

        obj = dict()
        obj["sender"] = b["from"]
        obj["recipients"] = b["to"]
        obj["subject"] = b["subject"]
        obj["emailSentOn"]=""
        obj["body"] = body.encode('base64')
        f3 =open(os.getcwd()+"/csv_files/"+filename+".json","w+")
        json.dump(obj, f3, sort_keys=True, indent=4)
        f3.close()
        f2.close()
    return obj


if __name__=="__main__":
    #data = convert()
    #data = pd.DataFrame.from_dict(data)
    #data.to_csv("training_data.csv")
    f2 = open("", "r")
    data = f2.read()
    d= json.loads(data)
