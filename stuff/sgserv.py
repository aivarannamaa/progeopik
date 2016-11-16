from wsgiref.simple_server import make_server
from veebiprogramm import application

server = make_server('localhost', 8080, application)
server.serve_forever()