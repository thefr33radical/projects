from flask import jsonify,Flask

app = Flask(__name__)

def names():
        """

        :return:
        """
        data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
        return jsonify(data)

def welcome():
        return "<H1> Welcome!!!!!!!!!!!!! </H1>"


if __name__ =="__main__":
	
	
	app.run(debug=True)
	app.add_url_rule("/names","names",names,methods=["GET"])
	app.add_url_rule("/","/",welcome,methods=["GET"])


from flask import Flask, Response


app = Flask(__name__)

@app.route("/")
def index():
    return Response("It works!"), 200

if __name__ == "__main__":
    app.run(debug=True)
	


