import time

def application(environ, start_response):
    vastuse_shabloon = """
        <html>
            <head>
                <title>Tere!</title>
            </head>
            <body>
                <h1>Tere, kallis klient!</h1>
                <p>{}</p>
            </body>
        </html>"""

    if environ["QUERY_STRING"] == "kellaaeg":
        vastuse_keha = vastuse_shabloon.format(time.strftime("%H:%M:%S"))
    elif environ["QUERY_STRING"] == "kuupaev":
        vastuse_keha = vastuse_shabloon.format(time.strftime("%Y-%m-%d"))
    else:
        vastuse_keha = vastuse_shabloon.format("Kuidas, palun?")

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [vastuse_keha.encode("UTF-8")]
import sys
print(sys.argv)