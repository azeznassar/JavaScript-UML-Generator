import unittest
from unittest.mock import patch

# pylint: disable="import-error"
from javascript_handler import JavascriptHandler

test_js = ""

class JavaScriptHandlerTests(unittest.TestCase):
    def setUp(self):
        global test_js
        with open('test.js') as js_file:
                js = js_file.read()
                test_js += js + ' \n' 

    def test_extract_javascript_a(self):
        self.js_handler = JavascriptHandler(test_js, "a")
        current_value = self.js_handler.js_code
        self.js_handler.extract_javascript_a()
        new_value = self.js_handler.js_code
        # Expect handler.js_code to have changed after method called 
        self.assertNotEqual(current_value, new_value, "extract javascript a test failed")

    def test_extract_javascript_b(self):
        self.js_handler = JavascriptHandler(test_js, "b")
        current_value = self.js_handler.js_code
        self.js_handler.extract_javascript_b()
        new_value = self.js_handler.js_code
        # Expect js_handler.js_code to have changed after extract method called 
        self.assertNotEqual(current_value, new_value, "extract javascript a test failed")

    @patch('dot_formatter.DotFormatter.convert_to_dot_a')
    def test_create_puml_a(self, MockMethod):
        # Create mock for my_dot_formatter.convert_to_dot_a and expect it to have been called
        self.js_handler = JavascriptHandler(test_js, "a")
        self.js_handler.create_puml()
        self.assertTrue(MockMethod.called)

    @patch('dot_formatter.DotFormatter.convert_to_dot_b')
    def test_create_puml_b(self, MockMethod):
        # Create mock for my_dot_formatter.convert_to_dot_b and expect it to have been called
        self.js_handler = JavascriptHandler(test_js, "b")
        self.js_handler.create_puml()
        self.assertTrue(MockMethod.called)


if __name__ == '__main__':
    unittest.main(verbosity=2)
