
import os
    

          
def corenlp_starter():
        os.chdir("/home/****/Documents/stanford-corenlp-full-2017-06-09/")
        os.system('java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9011 -timeout 15000&')
       # os.system("killall -9 $(lsof -t -i:9011)")
corenlp_starter()
