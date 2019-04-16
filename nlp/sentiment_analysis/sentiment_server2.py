#when to join the process needs to be seen.


from multiprocessing import Process
import sent_analysis_m5 as sme
import os

if __name__ == '__main__':
    obj=sme.sentiment_analyzer()
    l=["how are you","awesome","very bad","how are you","awesome","very bad","how are you","awesome","very bad"]
    for i in l:#inp="This is  a new way"
        p = Process(target=obj.initialize, args=(i,))
        p.start()
        p.join()
    
