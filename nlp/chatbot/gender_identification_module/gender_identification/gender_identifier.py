#!/usr/bin/python

import pandas as pd
import numpy as np
import os
import sys
import re
import urllib
import urllib2

class identify:

    # 4.1 FUNCTION TO WRITE TO CSV<< probabilty needs to be added>>
    def write_csv(self,value,identity):
        name=str(value[0])
        abspath=os.path.abspath(os.path.dirname(sys.argv[0]))
        path_male="/data/Indian-Male-Names.csv"
        path_female="/data/Indian-Female-Names.csv"
        #print name
        #print identity
        if(identity=='m'):
            m_name=pd.read_csv(abspath+path_male)
            
            dict1={'name':name,'gender':identity,'race':'indian'}
            #print m_name
            m_name=m_name.append(dict1,ignore_index=True)
            m_name.to_csv(abspath+path_male,mode='a+',index=False)
            
        else:
            f_name=pd.read_csv(abspath+path_female)
            dict1={'name':name,'gender':identity,'race':'indian'}
            f_name=f_name.append(dict1,ignore_index=True)
            f_name.to_csv(abspath+path_female,mode='a+',index=False)
        return

    # 4. FUNCTION TO CHECK FROM INTERNET
    def check_online(self,value):
        print "checking online"
        try:
            url = "http://www.gpeters.com/names/baby-names.php?name=adam&button=Go"
            f = urllib.urlopen(url)
            get_page=re.findall("<b>It's a(.*)!</b>",f.read())
            ident= get_page[0]

            url = "http://www.gpeters.com/names/baby-names.php?name=adam&button=Go"
            f = urllib.urlopen(url)
            prob_search=re.findall(' <b>(.+) times',f.read())
            prob=float(prob_search[0])
            #print prob
            if(ident.find('boy')is True):
                #print "boy"
                self.write_csv(value,"m")
                return
            else:
                #print "female"
                self.write_csv(value,"f")
                return
        except IOError:
             print "exception"
             return

    # 3.1. READ FROM CSV FILE
    def read_csv(self,value):
        abspath=os.path.abspath(os.path.dirname(sys.argv[0]))
        path_male="/data/Indian-Male-Names.csv"
        path_female="/data/Indian-Female-Names.csv"
        
        m_name=pd.read_csv(abspath+path_male)
        f_name=pd.read_csv(abspath+path_female)
        
        m_dct=m_name.set_index('name')[['gender','race']].T.apply(tuple).to_dict()
        f_dct=f_name.set_index('name')[['gender','race']].T.apply(tuple).to_dict()
        
        return m_dct,f_dct

    # 3. FUNCTION TO CHECK IF NAME IS PRESENT IN LOCAL DICTIONARY << need to be optimized>>
    def check_in_dict(self,value):
        m_dct,f_dct=self.read_csv(value)
        
        first_name=""
        if(len(value)>1):
            first_name=value[1]
        else:
            first_name=value[0]
       
        if(m_dct.get(first_name)!=None):
            print first_name,"Male"
            return
        if(f_dct.get(first_name)!=None):
            print first_name,"Female"
            return
        
        # Check online if not present in dictionary
        self.check_online(value)

    # 2. FUNCTION TO CHECK IF THE NAME CONTAINS HONOROFICS, IF SO RETURN GENDER
    def check_honorofics(self,value):
        value=value.split(" ")
         ## IF Honorofics are present return the Gender
        
        # Male & female Honorofics. Including common names.
        m_defnames=["sri","mr","mohammad","muhammad",'md','mister','master','lord','rev','revd']
        f_defnames=["smt","mrs","ms","kaur","begum","jahan","kumari","bai",'lady','maam']
                
        for i in value:
            for z in f_defnames:
                if(z==i):
                    print value,"Female","P:1"
                    print i,z
                    return
            for j in m_defnames:
                if(i==j):
                    print value,"Male","P:1"
                    print i,j
                    return
         
        # IF not able to determine name by honorofics, check the dictionary
        self.check_in_dict(value)

    # 1. FUNCTION TO PARSE NAME, DETECT ANY AMBUIGUITIES.   
    def compute(self):
        
        ## 1. Preprocessing
        #inp=raw_input()
        #value=str("gowtham")
        value=raw_input()
        value=value.lower()
        value=value.replace(".","")
        #print value
        
        x=re.findall('[^a-z\s]',value)
        #print x
        #Catch invalid charecters
        if(len(x)>0):
            print x
            return
        
        self.check_honorofics(value)

    # 0. CONSTRUCTOR
    def __init__(self):
        self.compute()

# MAIN FUNCTION
        
if __name__=="__main__":
    new_obj=identify()
else:
    obj=identify()


    
    
    
        
        


