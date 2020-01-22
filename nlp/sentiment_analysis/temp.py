import os
os.chdir("/home/gowtham/Documents/stanford-corenlp-full-2017-06-09/")
#call(["java","-mx4g","-cp",'"*"'," edu.stanford.nlp.pipeline.StanfordCoreNLPServer","-port","9009","-timeout","15000"])
os.system('java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9011 -timeout 15000')
import json

from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9011')

l=[]

text = (
  'Pusheen and Smitha walked along the beach. ')
  
  
l=text.split(".")

print(l)
output = nlp.annotate(l[0], properties={
  'annotators': 'sentiment',
  'outputFormat': 'json'
  })

print(output['sentences'][0]['sentiment'])
with open("output.json","w+") as f:
         f.write(json.dumps(output,indent=4,sort_keys=True,ensure_ascii=False))
         
