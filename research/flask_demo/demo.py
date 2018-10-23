from flask import jsonify,Flask


class Demo(object):
    """
        Flask Demo Server

    """
    def names(self):
        """

        :return:
        """
        data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
        return jsonify(data)

    def welcome(self):
        return "<H1> Welcome!!!!!!!!!!!!! </H1>"


obj = Demo()
app = Flask(__name__)
app.add_url_rule("/names","names",obj.names,methods=["GET"])
app.add_url_rule("/","/",obj.welcome,methods=["GET"])
app.run(debug=True,host='0.0.0.0')


if __name__ == '__main__':
    obj = Demo()
