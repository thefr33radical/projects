import urllib
import re
url = "http://www.gpeters.com/names/baby-names.php?name=adam&button=Go"
f = urllib.urlopen(url)
#print f.read()
f1=f.read()
f2=f.read()
get_page=re.findall("<b>It's a(.*)!</b>",f1)
print get_page[0]

url = "http://www.gpeters.com/names/baby-names.php?name=adam&button=Go"
f = urllib.urlopen(url)
prob=re.findall(' <b>(.+) times',f.read())
print float(prob[0])