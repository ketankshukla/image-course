from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body=json.dumps({"status":"ok","service":"container-lab"} if self.path=="/health" else {"error":"not_found"}).encode()
        self.send_response(200 if self.path=="/health" else 404)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length",str(len(body)))
        self.end_headers()
        self.wfile.write(body)
if __name__=="__main__": HTTPServer(("0.0.0.0",8080),Handler).serve_forever()
