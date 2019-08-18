from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
# from urllib import request
import pandas as pd
from enum import Enum
import json
USERS = '/users'
QUERY = '/query'
GROUPS = '/groups'

class PasswdRequestHandler(BaseHTTPRequestHandler):
    __passwd_path = "/etc/passwd"
    __group_path = "/etc/group"
    @staticmethod
    def setGroupPath(path):
        PasswdRequestHandler.__group_path=path
        print(PasswdRequestHandler.__passwd_path)
        print("asfs")
    @staticmethod
    def setPasswdPath(path):
        PasswdRequestHandler.__passwd_path = path
        print(PasswdRequestHandler.__passwd_path)

    class Type(Enum):
        passwd = 0
        group = 1

    def do_GET(self):
        print(self.__passwd_path)
        print(self.path)
        if (self.path.startswith(USERS)):
            args = self.path[len(USERS):]
            self.parseRequest(args, self.Type.passwd)
        elif (self.path.startswith(GROUPS)):
            args = self.path[len(GROUPS):]
            self.parseRequest(args, self.Type.group)
        else:
            self.send_error(404)

    def parseRequest(self, args, type):
        file = self.read(type)
        print(args)
        if (args.startswith(QUERY)):
            print(QUERY)
            result = self.query(file)
            self.send(result)
        else:
            print(file.to_json())
            self.send(file)

    def send(self, data):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data.to_json(orient='records').encode(encoding='utf_8'))

    def read(self, type):
        if (type == self.Type.passwd):
            data = pd.read_csv(self.__passwd_path, sep=':', header=None,
                               names=['name', 'uid', 'gid',
                                      'comment', 'homedir', 'shell'],
                               usecols=[0, 2, 3, 4, 5, 6])
            data.fillna({'name': '', 'uid': 0,
                         'gid': 0, 'comment': '', 'homedir': '', 'shell': ''}, inplace=True)
            return data
        elif (type == self.Type.group):

            data = pd.read_csv(PasswdRequestHandler.__group_path, sep=':', header=None, names=['name', 'gid', 'member'],
                               usecols=[0, 2, 3])
            data.fillna({'name': '', 'gid': 0, 'member': ''}, inplace=True)
            return data

    def query(self, data):
        parsed_path = urlparse(self.path)
        print(parse_qs(parsed_path.query))
        query = parse_qs(parsed_path.query)
        for key, value in query.items():
            print(key,value)
            for v in value:
                print(data[key])
                print(data[key].str.contains(v))
                data = data[data[key].str.contains(v)]
                print(data)
        return data



# httpd = HTTPServer(('localhost', 8000), PasswdRequestHandler)
# httpd.serve_forever()
# print(request.urlopen("localhost:8000").read())