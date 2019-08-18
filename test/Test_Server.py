import unittest
import requests
import pandas as pd
from src.PasswdRequestHandler import PasswdRequestHandler
from http.server import HTTPServer
class PasswdRequestHandlerCase(unittest.TestCase):
    myurl = 'http://localhost:8000'
    passwdpath="test/test_passwd"
    # response = requests.get(myurl + "/users")
    # response = requests.get(myurl + "/users", {'name': "dasf"})
    # response = requests.get(myurl)
    # print(response)
    def test_read(self):
        response = self.handler.read(PasswdRequestHandler.Type.passwd)
        self.assertEqual(response, self.passwd_data)

    def test_read2(self):
        response = self.handler.read(PasswdRequestHandler.Type.passwd)
        self.assertEqual(response, self.group_data)


    def setUp(self) -> None:
        PasswdRequestHandler.setPasswdPath(self.passwdpath)
        PasswdRequestHandler.setGroupPath("test/test_group")
        self.handler = PasswdRequestHandler()

        self.group_data = pd.read_csv(PasswdRequestHandler.__group_path, sep=':', header=None, names=['name', 'gid', 'member'],
                           usecols=[0, 2, 3])
        self.group_data.fillna({'name': '', 'gid': 0, 'member': ''}, inplace=True)

        self.passwd_data = pd.read_csv(self.passwdpath, sep=':', header=None,
                           names=['name', 'uid', 'gid',
                                  'comment', 'homedir', 'shell'],
                           usecols=[0, 2, 3, 4, 5, 6])
        self.passwd_data.fillna({'name': '', 'uid': 0,
                     'gid': 0, 'comment': '', 'homedir': '', 'shell': ''}, inplace=True)

if __name__ == '__main__':


    unittest.main()
