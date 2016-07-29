#!/usr/bin/env python
"""
Description

    Uses the Tornado framework to display a website frontend and
    websocket communications for the Fogponics project.

"""


import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
from tornado.options import define, options

# Web Server Paths
WORKING_DIR = os.path.dirname(__file__)
STATIC_PATH = os.path.join(WORKING_DIR, 'static')
TEMPLATE_PATH = os.path.join(WORKING_DIR, 'templates')

# WebSocket
define("ws_port", default=9998, help="run on the given port", type=int)
define("ws_host", default='127.0.0.1', help="run on the given ip", type=str)

# HTTP Server
define("http_port", default=8080, help="run on the given port", type=int)
define("http_host", default='127.0.0.1', help="run on the given ip", type=str)

CLIENTS = []


class WebServer(tornado.web.Application):
    """Defines the Web Server """
    def __init__(self):

        handlers = [
            (r"/", MainHandler)
        ]

        settings = {
            "template_path": TEMPLATE_PATH,
            "static_path": STATIC_PATH,
            "debug": False,  # Change to True for live updates to the site
        }

        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    """Main Handler renders the webpage """
    def get(self):
        self.render("index.html")


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    """Defines the WebSocket Server """

    def open(self):
        """When a client connects add it to the list """
        CLIENTS.append(self)

    def on_message(self, message):
        """Pass of all messages to all connected clients """
        for client in CLIENTS:
            client.write_message(message)

    def on_close(self):
        """When clients disconnect remove them from the list """
        CLIENTS.remove(self)

    def check_origin(self, origin):
        return True


def main():
    """Main function - starts the webserver and websocket server
    """
    # Define the websocket connection
    wsocket = tornado.web.Application([(r'/', WebSocketHandler)])
    wsocket.listen(options.ws_port, options.ws_host)

    # Define the Web Server
    web_server = WebServer()
    http_server = tornado.httpserver.HTTPServer(web_server)
    http_server.listen(options.http_port, options.http_host)

    # Define the main Tornado IO loop
    main_loop = tornado.ioloop.IOLoop.instance()
    # Start the program
    main_loop.start()


if __name__ == '__main__':

    main()
