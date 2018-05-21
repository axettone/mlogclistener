from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class MLogCHandler(BaseHTTPRequestHandler):
	def do_PUT(self):
		print self.rfile.read(int(self.headers.getheader('Content-Length')))
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		# Send the html message
		self.wfile.write('''{"response":"ok"}''')
		return