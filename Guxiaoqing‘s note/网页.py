from http.server import HTTPServer, BaseHTTPRequestHandler

data = {'result': 'this is a test'}
host = ('localhost', 8888)
class Resqult(BaseHTTPRequestHandler):
    timeout = 10
    server_version = "Apache"

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.send_header("test", "this is test")
        self.end_headers()
        buf = '''<!DOCTYPE HTML>
        <html>
            <head>
                <title>Get page</title>
            </head>
            <body>
                <form action="post_age" method="post">
                username:<input type="text" name="username” ><br>
                password:<input type="text" name="password" ><br>
                <input type ="submit" value ="submit">
                </form>
            </body>
        </html>
            '''
        self.wfile.write(buf.encode())  # 传入一进制致据

    def do_POST(self):
        path = self.path
        print(path)

        datas = self.rfile.read(int(self.headers['content-length']))

        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.send_header("test", "this is test")
        self.end_headers()

        buf = '''<!DOCTYPE HTML>
            <html>
                <head>
                    <title>Post page</title>
                </head>
                <body>
                    Post Data:%s <br>
                    Path:%s
                </body>
            </html>

        ''' % (datas, self.path)
        self.wfile.write(buf.encode())


if __name__ == '__main__':
    server = HTTPServer(host, Resqult)
    print("starting server,listen at:%s:%s" % host)
    server.serve_forever()
