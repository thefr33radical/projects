import sent_analysis_m5 as sme
from flask import Flask,request,jsonify


app=Flask(__name__)
@app.route("/",methods=['GET','POST'])


def func():
    if request.method=="POST":
        x=request.json
        text=x['text']
        print(text)
        
        obj=sme.sentiment_analyzer()
        output=obj.initialize(text)
        #print (output)
        #print (x)
        return jsonify({"sentiment":output})
       # return "true"
    return "were"


if __name__=="__main__":
    app.run(threaded=True)