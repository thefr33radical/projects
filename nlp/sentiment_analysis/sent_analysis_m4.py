# 1.corenlp module needs to be installed
# 2. working directory need to be set to corenlp module
# 3. time stamp is marked for all three modules


from textblob import TextBlob
import time
from subprocess import call
import os 
import json
from pycorenlp import StanfordCoreNLP
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

 
class sentiment_analyzer:
    #TEXTBLOB
    def text_blob(self,string):
          #  x=time.time()
            l=[]
            l.append(string)
            for i in l:             
               text=i
               if(text ==""):
                   print("Exiting")
                   return 0
               blob=TextBlob(text)
           # print(time.time()-x)
            return(blob.sentiment.polarity)
    #VADER        
    def vader(self,paragraph):
          #  x=time.time()
            sentences = [""]
            lines_list = tokenize.sent_tokenize(paragraph)
            sentences.extend(lines_list)
            sid = SentimentIntensityAnalyzer()
            for sentence in sentences:
                if sentence != "":
                    ss = sid.polarity_scores(sentence)
                    #print (ss,max(ss['pos'],ss['neg'],ss['neu']))
                    #print(time.time()-x)
                    if((ss['pos']>=ss['neg']) and (ss['pos']>=ss['neu'])):
                        return 1.0-((ss['neu']*33.3)+(ss['neg']*33.3))/100
                    if((ss['neg']>=ss['pos']) and (ss['neg']>=ss['neu'])):
                        return 0.0+((ss['pos']*33.3)+(ss['neu']*33.3))/100
                    if((ss['neu']>=ss['neg']) and (ss['neu']>=ss['pos'])):
                        return 0.5+((ss['pos']*33.3)-(ss['neg']*33.3))/100
                        
    #CORENLP            
    def corenlp_starter(self):
        os.chdir("/home/gowtham/Documents/stanford-corenlp-full-2017-06-09/")
        os.system('java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9011 -timeout 15000')

    def corenlp(self,text):
        #x=time.time()        
        nlp = StanfordCoreNLP('http://localhost:9011')
        
        output = nlp.annotate(text, properties={  'annotators': 'sentiment',  'outputFormat': 'json'        })
        score=0.0
        sentiment=(output['sentences'][0]['sentiment'])
      #  print("senti_corenlp",sentiment)
        if(sentiment=='Positive' or sentiment=='Verypositive'):
            score=0.75
        if(sentiment=='Verypositive'):
            score=1.0
        if(sentiment=='Negative'):
            score=0.25
        if(sentiment=='Verynegative'):
             score=0.0
        if(sentiment=='Neutral'):
            score=0.5
        #print(time.time()-x)
        return score   
        
    #COMPUTATION_AVERAGE                 
    def module3(self,text_sentiment,vader_sentiment,corenlp_sentiment):
        #x=time.time()
        std_text=float(((1+text_sentiment)/2)) 
        #std_vader=float(((1-vader_sentiment)/1)*100) 
       # print(std_text,vader_sentiment,corenlp_sentiment)
        if(vader_sentiment<=0.5 and corenlp_sentiment<= 0.5):
           # print(time.time()-x)
            return (vader_sentiment+corenlp_sentiment)/2
        
        avg=(std_text+vader_sentiment+corenlp_sentiment)/3
       # print(time.time()-x)
        return avg
        
      #STARTER MODULE
    def initialize(self,string2):
             s.corenlp_starter()
                 # Input to be given
             string2='its a very open matter'
             string3=string2.split(".")
    
             for string in string3:
                 if(string !=""):
                     core_nlp=s.corenlp(string)
                     text_sentiment=s.text_blob(string)
                     vader_sentiment=s.vader(string)
        
                     print(text_sentiment,vader_sentiment,core_nlp)
                
                     avg=s.module3(text_sentiment,vader_sentiment,core_nlp)
                     print(avg)
           
if __name__=="__main__":
    s=sentiment_analyzer()
    s.initialize('its a very open matter')
   