import unittest

# pylint: disable="import-error"
from current_cmd_a import CurrentCMD_A


class CmdATests(unittest.TestCase):
    def setUp(self):
        self.cmd_a = CurrentCMD_A()   

    def test_one(self):
        self.assertEqual(True, True, "This shows if test fails")

    def tearDown(self):
        print("This CmdATests test case is done!")


if __name__ == '__main__':
    unittest.main(verbosity=2)
