import unittest

from src.current_cmd_a import CurrentCMD_A


class CmdATests(unittest.TestCase):
    def setUp(self):
        self.foo = CurrentCMD_A()   

    # def test_three(self):
    #     self.assertEqual(True)

    def tearDown(self):
        print("This CmdATests test case is done!")


if __name__ == '__main__':
    unittest.main(verbosity=2)
