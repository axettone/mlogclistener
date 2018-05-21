from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sqlite3

class MLogCHandler(BaseHTTPRequestHandler):
	def do_PUT(self):
		data = self.rfile.read(int(self.headers.getheader('Content-Length')))
		conn = sqlite3.connect('websites.db')
		conn.execute('''INSERT INTO audits 
			(code, src_ip,src_port,dst_ip,dst_port,status,section_b,section_f)
			VALUES (?,?,?,?,?,?,?,?)''', ())
		conn.commit()
		conn.close()
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		# Send the html message
		self.wfile.write('''{"response":"ok"}''')
		return