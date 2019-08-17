import unittest
from src.PasswdParser import PasswdParser


class MyTestCase(unittest.TestCase):
    testFile = "test/test_passwd"
    def test_users(self):
        expected_value = '{“name”: “root”, “uid”: 0, “gid”: 0, “comment”: “root”, “home”: “/root”, “shell”: “/bin/bash”}, {“name”: “dwoodlins”, “uid”: 1001, “gid”: 1001, “comment”: “”, “home”: “/home/dwoodlins”, “shell”: “/bin/false”}'
        parser = PasswdParser(self.testFile)
        self.assertEqual(parser.users(), expected_value)

    def test_quary(self):
        expected_value = '{“name”: “dwoodlins”, “uid”: 1001, “gid”: 1001, “comment”: “”, “home”: “/home/dwoodlins”, “shell”: “/bin/false”}'
        parser = PasswdParser(self.testFile)
        self.assertEqual(parser.quary(shell="/bin/false"), expected_value)



if __name__ == '__main__':
    unittest.main()
