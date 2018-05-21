from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import re
import sqlite3

class MLogCHandler(BaseHTTPRequestHandler):
	def do_PUT(self):
		data = self.rfile.read(int(self.headers.getheader('Content-Length')))
		conn = sqlite3.connect('websites.db')
		sections = re.split(r"--\d{8}-[A-Z]--", data)
		sectionA = sections[1]
		sectionB = sections[2]
		sectionF = sections[3]
		print sectionB
		# ...
		m = re.search(r"\[(.*)\]\s(\S*)\s(\S*)\s(\S*)\s(\S*)\s(\S*)", sectionA)
		timestamp = m.group(1)
		code = m.group(2)
		src_ip = m.group(3)
		src_port = m.group(4)
		dst_ip = m.group(5)
		dst_port = m.group(6)
		
		m = re.search(r"(GET|POST|PUT|DELETE|PATCH)\s(\S*).*", sectionB, re.MULTILINE)
		method = m.group(1)
		url = m.group(2)
		#protocol = m.group(3)

		m = re.search(r"Host:\s([a-z|.]*)", sectionB, re.MULTILINE)
		host = m.group(1)
		
		m = re.search(r"HTTP/(?:1.1|1.0|2.0)\s([0-9]*)", sectionF, re.MULTILINE)
		status = m.group(1)
		# m = re.search(r"Content-Length:\s([0-9]*)", sectionF, re.MULTILINE)



		conn.execute('''INSERT INTO audits 
			(code, src_ip,src_port,dst_ip,dst_port,status,section_b,section_f)
			VALUES (?,?,?,?,?,?,?,?)''', (code, src_ip,src_port,dst_ip,dst_port,status,sectionB,sectionF))
		conn.commit()
		conn.close()
		self.send_response(200)
		self.send_header('Content-type','text/json')
		self.end_headers()
		# Send the html message
		self.wfile.write('''{"response":"ok"}''')
		return