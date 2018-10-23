import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        return json.dumps({"msg":"hello!!!!!!!"})

def make_app():
    return tornado.web.Application([
        (r"/hello", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()