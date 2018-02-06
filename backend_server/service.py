import pyjsonrpc
import json
#import package from other directory
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), './', 'utils'))

from bson.json_util import dumps
import MongoDBclient

HOST = 'localhost'
PORT = 3002

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """ Test """
    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        print("add is called with %d with %d" % (a, b))
        return a + b

    @pyjsonrpc.rpcmethod
    def getNews(self):
        db = MongoDBclient.get_db()
        db.news.insert({"id":1,"name":"zha"})
        news = list(db['news'].find()) #return everything
        return json.loads(dumps(news))

http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (HOST, PORT),
    RequestHandlerClass = RequestHandler
)

print("Starting HTTP server on %s:%d" % (HOST, PORT))

http_server.serve_forever()
