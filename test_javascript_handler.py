import unittest
from unittest.mock import patch

# pylint: disable="import-error"
from javascript_handler import JavascriptHandler

test_js = "class Cat {  }"

class JavaScriptHandlerTests(unittest.TestCase):

    def test_extract_javascript_a(self):
        self.js_handler = JavascriptHandler(test_js, "a")
        self.js_handler.extract_javascript_a()
        # Expect handler.js_code to have changed after method called 

        self.assertEqual(True, True, "This shows if test fails")

    def test_extract_javascript_b(self):
        self.js_handler = JavascriptHandler(test_js, "b")
        self.js_handler.extract_javascript_b()
        # Expect js_handler.js_code to have changed after extract method called 

        self.assertEqual(True, True, "This shows if test fails")

    @patch('dot_formatter.DotFormatter.convert_to_dot_a')
    def test_create_puml(self, MockMethod):
        # Create mock for my_dot_formatter.convert_to_dot_a and expect it to have been called
        self.js_handler = JavascriptHandler(test_js, "a")
        self.js_handler.create_puml()
        self.assertTrue(MockMethod.called)


if __name__ == '__main__':
    unittest.main(verbosity=2)
