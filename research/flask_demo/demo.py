from flask import jsonify,Flask


class demo(object):
    """
        Flask Demo Server

    """

    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule("/names","names",self.names,methods=["GET"])
        self.app.add_url_rule("/","/",self.welcome,methods=["GET"])
        self.app.run(debug=True,host='0.0.0.0')


    def names(self):
        """
        
        :return:
        """
        data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
        return jsonify(data)

    def welcome(self):
        return "<H1> Welcome </H1>"


if __name__ == '__main__':
    obj = demo()
