#!/usr/bin/python

import pandas as pd
#import numpy as np
import os
import sys
import re
import urllib
#import urllib2
abs_path=os.path.abspath(os.path.dirname(sys.argv[0]))
     
class GenderIdentify:
    maleNames = set()
    femaleNames = set()

    # 4.1 FUNCTION TO WRITE TO CSV<< probabilty needs to be added>>
    @staticmethod
    def __write_csv(value,identity):
        name=value
        path_male="/data/new_male_names2.csv"
        path_female="/data/new_female_names2.csv"
        #print name
        #print identity
        if(identity=='m'):
            with open(abs_path+path_male, 'a+') as fp:
                fp.write(name+','+identity+',indian\n')
            return

        else:
            with open(path_female, 'a+') as fp:
                fp.write(name+','+identity+',indian\n')
            return

        return
    
    # 4. FUNCTION TO CHECK FROM INTERNET
    @staticmethod
    def __check_online(value):
        print("checking online")
        try:
            url = "http://www.gpeters.com/names/baby-names.php?name=" + value + "&button=Go"
            f = urllib.request.urlopen(url)
            #f = urllib.urlopen(url)
            downloaded = f.read().decode('ascii')
            get_page=re.findall("<b>It's a(.*)!</b>",downloaded)
            #get_page=re.findall("<b>It's a(.*)!</b>",f.read().decode('ascii'))
            ident= get_page[0].strip()
            print(ident)

            #url = "http://www.gpeters.com/names/baby-names.php?name=" + value + "adam&button=Go"
            #f = urllib.request.urlopen(url)
            #f = urllib.urlopen(url)
            prob_search=re.findall(' <b>(.+) times',downloaded)
            #prob_search=re.findall(' <b>(.+) times',f.read().decode('ascii'))
            prob=float(prob_search[0])
            #print prob
            if ident == 'boy':
                #print("boy")
                __write_csv(value,"m")
                return ['male', 0.9]
            else:
                #print("female")
                __write_csv(value,"f")
                return ['female', 0.9]
        except Exception:
             #print("exception")
             return ['unknown', 1]
            
    # 3.1. READ FROM CSV FILE
    @staticmethod
    def __read_csv(value):
        abspath=os.path.abspath(os.path.dirname(sys.argv[0]))
        path_male="/new_male_names.csv"
        path_female="/new_female_names.csv"
        
        m_name=pd.read_csv(abspath+path_male)
        f_name=pd.read_csv(abspath+path_female)
        
        m_dct=m_name.set_index('name')[['gender','race']].T.apply(tuple).to_dict()
        f_dct=f_name.set_index('name')[['gender','race']].T.apply(tuple).to_dict()
        print(m_dct,f_dct)
        return m_dct,f_dct
    
    # 3. FUNCTION TO CHECK IF NAME IS PRESENT IN LOCAL DICTIONARY << need to be optimized>>
    @staticmethod
    def __check_in_dict(value):
        if len(GenderIdentify.maleNames) == 0:
            with open(abs_path+"/data/new_male_names.txt", 'r') as fp:
                GenderIdentify.maleNames = set([e for e in fp.read().split('\n') if len(e) > 1])
        if len(GenderIdentify.femaleNames) == 0:
            with open(abs_path+"/data/new_female_names.txt", 'r') as fp:
                GenderIdentify.femaleNames = set([e for e in fp.read().split('\n') if len(e) > 1])
        print(value)
        if ((value in GenderIdentify.maleNames) and (value not in GenderIdentify.femaleNames)):
            return ['male', 1]
        if ((value in GenderIdentify.femaleNames) and (value not in GenderIdentify.maleNames)):
            return ['female', 1]

        ml2 = [' '.join(e.split()[:2]) for e in GenderIdentify.maleNames]
        fl2 = [' '.join(e.split()[:2]) for e in GenderIdentify.femaleNames]
        v = value.split()
        if len(v) >= 2:
            nm = v[0] + ' ' + v[1]
            if ((nm in ml2) and (nm not in fl2)):
                return ['male', 0.9]
            if ((nm in fl2) and (nm not in ml2)):
                return ['female', 0.9]

        ml1 = [e.split()[0] for e in ml2]
        fl1 = [e.split()[0] for e in fl2]
        nm = v[0]
        if ((nm in ml1) and (nm not in fl1)):
            return ['male', 0.9]
        if ((nm in fl1) and (nm not in ml1)):
            return ['female', 0.9]

        return ['unknown', 1]

    # 2. FUNCTION TO CHECK IF THE NAME CONTAINS HONOROFICS, IF SO RETURN GENDER
    @staticmethod
    def __check_honorofics(value):
        value=value.split(" ")
         ## IF Honorofics are present return the Gender
        
        # Male & female Honorofics. Including common names.
        m_defnames=["sri","mr","mohammad","muhammad",'md','mister','master','lord','rev','revd']
        f_defnames=["smt","mrs","ms","kaur","begum","jahan","kumari","bai",'lady','maam', 'miss']
                
        for i in value:
            for z in f_defnames:
                if(z==i):
                    #print(value,"Female","P:1")
                    #print(i,z)
                    return ['female', 1]
            for j in m_defnames:
                if(i==j):
                    #print(value,"Male","P:1")
                    #print(i,j)
                    return ['male', 1]
            print("something")
            return ['unknown', 1]
           
    # 1. FUNCTION TO PARSE NAME, DETECT ANY AMBUIGUITIES.   
   # @staticmethod
    def identify(name):
        
        ## 1. Preprocessing
        #inp=raw_input()
        #value=str("gowtham")
        value = name
        #value=raw_input()
        value=value.lower()
        value=value.replace(".","")
        print (value,"value")
        
        x=re.findall('[^a-z\s]',value)
        #(print x#
        #Catch invalid charecters
        if(len(x)>0):
            print(x)
            return
        
        gender = GenderIdentify.__check_honorofics(value)

        # IF not able to determine name by honorofics, check the dictionary
        if gender[0] == 'unknown':
            gender = GenderIdentify.__check_in_dict(value)

        # Check online if not present in dictionary
        if gender[0] == 'unknown':
            gender = GenderIdentify.__check_online(value)

        return gender


if __name__=='__main__':
    GenderIdentify.identify(" i am blue clown")
    
    
        
        

#with open('Indian-Male-Names.csv', 'r') as fp:
#	mnames = [e for e in fp.read().split('\n')]
#
#
#mnames1 = [e.split(',')[0] for e in mnames]
#fnames2 = [(e.split('d/0')[0]).strip() for e in fnames1]
#fnames2 = [(e.split('d/o')[0]).strip() for e in fnames2]
#fnames2 = [(e.split('w/o')[0]).strip() for e in fnames2]
#fnames2 = [(e.split('w/0')[0]).strip() for e in fnames2]
#
#mnames5 = []
#for e1 in fnames2:
#	mnames5.append(e1.split('@')[0].strip())
#
#fnames6 = [(e.split('(')[0]).strip() for e in fnames5]
#fnames6 = [re.sub('^smt[.]?', '', e).strip() for e in fnames6]
#fnames6 = [re.sub('^kumari[.]?', '', e).strip() for e in fnames6]
#fnames6 = [re.sub('^ku[.]', '', e).strip() for e in fnames6]
#fnames6 = [re.sub('^km ', '', e).strip() for e in fnames6]

