import pandas as pd
import urllib.parse as urlparse
from http.server import HTTPServer
from src.PasswdRequestHandler import PasswdRequestHandler
import sys
if __name__ == '__main__':
    # global PASSWD_PATH
    print("here")
    if len(sys.args) == 3:
        PasswdRequestHandler.setPasswdPath(sys.argv[1])
        PasswdRequestHandler.setGroupPath(sys.argv[2])

    httpd = HTTPServer(('localhost', 8000), PasswdRequestHandler)
    httpd.serve_forever()