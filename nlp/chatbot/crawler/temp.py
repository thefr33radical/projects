from multiprocessing import Process
import os
import sent_analysis_m5 as sme
import os
obj=sme.sentiment_analyzer()

def info(title):
    print (title)
    print ('module name:', __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print ('parent process:', os.getppid())
    print ('process id:', os.getpid())

def f(name):
    info('function f')
    print ('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
