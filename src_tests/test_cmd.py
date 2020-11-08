import unittest
from src.input_handler import InputHandler


class TestEthanCMD(unittest.TestCase):
    def setUp(self):
        self.client_code = InputHandler()

    def test_functionality(self):
        self.client_code.cmd_looper(self.client_code.cmd_b, "Running Ethan's cmd", self.client_code)

    def tearDown(self):
        print("This test case is done!")


class TestAzezCMD(unittest.TestCase):
    def setUp(self):
        self.client_code = InputHandler()
        self.current_cmd = "0"

    def test_functionality(self):
        self.client_code.cmd_looper(self.client_code.cmd_a, "Running Azez's cmd", self.client_code)

    def tearDown(self):
        print("This test case is done!")


if __name__ == '__main__':
    unittest.main()
