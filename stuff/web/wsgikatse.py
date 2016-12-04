from urllib.parse import parse_qs

def hello_world(environ, start_response):

    if environ["SCRIPT_NAME"] == "ilm":
        ...
    elif environ["SCRIPT_NAME"] == "horoskoop":
        parameetrid = parse_qs(environ["QUERY_STRING"])
        
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    yield b"<h1>OK</h1>\n"


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, hello_world)
    srv.serve_forever()    