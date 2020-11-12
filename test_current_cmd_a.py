import unittest
import sys
from io import StringIO

# pylint: disable="import-error"
from current_cmd_a import CurrentCMD_A


class CmdATests(unittest.TestCase):
    def setUp(self):
        self.cmd_a = CurrentCMD_A()   

    # DELETE THIS METHOD
    def test_example(self):
        self.assertEqual(True, True, "This shows if test fails")

    def test_cmd_a_help(self):
        out = StringIO()
        sys.stdout = out
        self.cmd_a.do_help(None)

        output = out.getvalue().strip()
        assert 'Exits from the program' in output

    def test_cmd_a_create_uml(self):
        self.cmd_a.do_create_uml(None)
        self.assertEqual(self.cmd_a.current_command, "do_create_uml", "create_uml test failed")
        self.assertTrue(self.cmd_a.do_create_uml(None), "create_uml test failed")

    def test_cmd_a_deserialize(self):
        self.cmd_a.do_deserialize(None)
        self.assertEqual(self.cmd_a.current_command, "do_deserialize", "deserialize test failed")
        self.assertTrue(self.cmd_a.do_create_uml(None), "deserialize test failed")

    def test_cmd_a_info(self):
        out = StringIO()
        sys.stdout = out
        self.cmd_a.do_info(None)

        output = out.getvalue().strip()
        assert 'JS2UML: Generate UML 2 Class Diagrams from JavaScript file(s)' in output

    def test_cmd_a_switch_cmd(self):
        out = StringIO()
        sys.stdout = out
        self.cmd_a.do_switch_cmd(None)

        output = out.getvalue().strip()
        assert "Swapping to Ethan's Command Line" in output
        self.cmd_a.do_switch_cmd(None)
        self.assertEqual(self.cmd_a.current_command, "do_switch_cmd", "switch_cmd test failed")
        self.assertTrue(self.cmd_a.do_switch_cmd(None), "switch_cmd test failed")

    def test_cmd_a_quit(self):
        out = StringIO()
        sys.stdout = out
        self.cmd_a.do_quit(None)

        output = out.getvalue().strip()
        assert "Thank you for using JS2UML" in output
        self.cmd_a.do_quit(None)
        self.assertEqual(self.cmd_a.current_command, "do_quit", "quit test failed")
        self.assertTrue(self.cmd_a.do_quit(None), "quit test failed")

    def test_cmd_a_help_create_uml(self):
        out = StringIO()
        sys.stdout = out
        self.cmd_a.help_create_uml()

        output = out.getvalue().strip()
        assert "Generate UML 2 Class Diagrams from JavaScript file" in output


if __name__ == '__main__':
    unittest.main(verbosity=2)
