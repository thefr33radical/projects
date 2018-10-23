import falcon
import json

class HelloResource:
    def on_get(self, request, response):
        """Handles GET requests"""
        data = {'message': 'Hello world!'}

        response.body = json.dumps(data)

api = falcon.API()
api.add_route('/hello', HelloResource())


""""
standalone falcon + waitress
 waitress-serve --port=8080 demo:api





"""