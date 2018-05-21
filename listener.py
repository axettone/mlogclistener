#!/usr/bin/env python

import BaseHTTPServer, SimpleHTTPServer
import database
import mlogchandler
import sqlite3
import ssl
import yaml

config = yaml.safe_load(open("config.yml"))
HOST = config['server']['address']
PORT = config['server']['port']
CERT = config['server']['cert']

conn = sqlite3.connect('websites.db')
database.init_db(conn)

httpd = BaseHTTPServer.HTTPServer((HOST, PORT), mlogchandler.MLogCHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile=CERT, server_side=True)
httpd.serve_forever()
