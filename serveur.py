from http.server import HTTPServer, BaseHTTPRequestHandler

class MonHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Une nouvelle requête !")
        reponse = """HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 12
Connection: close

Hello World!"""
        self.wfile.write(reponse.encode())  
        '''
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            message = "Bonjour depuis BaseHTTPRequestHandler !"
            self.send_header("Content-Length", str(len(message)))
            self.end_headers()
            self.wfile.write(message.encode())
        else:
            self.send_error(404, "Ressource non trouvée")
        '''

# Lancement du serveur sur le port 8000
server = HTTPServer(("0.0.0.0", 8080), MonHandler)
print("Serveur HTTP actif sur le port 8080")
server.serve_forever()
