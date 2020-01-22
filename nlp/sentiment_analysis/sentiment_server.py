import sent_analysis_m5 as sme
from flask import Flask,request,jsonify

obj=sme.sentiment_analyzer()
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])

def func():
    if request.method=="POST":
        x=request.json
        text=x['text']
        print(text)
              
        output=obj.initialize(text)
        #print (output)
        #print (x)
        return jsonify({"sentiment":output})
       # return "true"
    
if __name__=="__main__":
    app.run(threaded=True)
    