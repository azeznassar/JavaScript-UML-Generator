import unittest
# pylint: disable="import-error"
from input_handler import InputHandler


class InputHandlerTests(unittest.TestCase):
    def setUp(self):
        self.input_handler = InputHandler()

    # def test_functionality(self):
    #     self.input_handler.cmd_looper(self.input_handler.cmd_a, "Running Azez's cmd", self.input_handler)

    def tearDown(self):
        print("This test case is done!")


if __name__ == '__main__':
    unittest.main(verbosity=2)
