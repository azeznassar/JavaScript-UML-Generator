import unittest
import sys
from io import StringIO
# pylint: disable="import-error"
from current_cmd_b import CurrentCMD_B


class CmdBTests(unittest.TestCase):
    def setUp(self):
        self.cmd_b = CurrentCMD_B()   

    def test_cmd_b_help(self):
        import sys
        from io import StringIO

        out = StringIO()
        sys.stdout = out
        self.cmd_b.do_help(None)

        output = out.getvalue().strip()
        assert 'Deletes the serialized file(s) after printing data' in output
    
    def test_cmd_b_create_uml(self):
        self.cmd_b.do_create_uml(None)
        self.assertEqual(self.cmd_b.current_command, "do_create_uml", "create_uml test failed")
        self.assertTrue(self.cmd_b.do_create_uml(None), "create_uml test failed")


    def test_cmd_b_deserialize(self):
        self.cmd_b.do_deserialize(None)
        self.assertEqual(self.cmd_b.current_command, "do_deserialize", "deserialize test failed")
        self.assertTrue(self.cmd_b.do_create_uml(None), "deserialize test failed")

    def test_cmd_b_info(self):
        out = StringIO()
        sys.stdout = out
        self.cmd_b.do_info(None)

        output = out.getvalue().strip()
        assert 'The software was developed by Azez Nassar & Ethan Bray in Python3' in output

    def test_cmd_b_switch_cmd(self):
        out = StringIO()
        sys.stdout = out
        self.cmd_b.do_switch_cmd(None)

        output = out.getvalue().strip()
        assert "Swapping to Azez's Command Line" in output
        self.cmd_b.do_switch_cmd(None)
        self.assertEqual(self.cmd_b.current_command, "do_switch_cmd", "switch_cmd test failed")
        self.assertTrue(self.cmd_b.do_switch_cmd(None), "switch_cmd test failed")

    def test_cmd_b_quit(self):
        out = StringIO()
        sys.stdout = out
        self.cmd_b.do_quit(None)

        output = out.getvalue().strip()
        assert "Leaving System" in output
        self.cmd_b.do_quit(None)
        self.assertEqual(self.cmd_b.current_command, "do_quit", "quit test failed")
        self.assertTrue(self.cmd_b.do_quit(None), "quit test failed")

    def test_cmd_b_default(self):
        out = StringIO()
        sys.stdout = out
        self.cmd_b.default(None)

        output = out.getvalue().strip()
        assert "Sorry, the command:" in output




if __name__ == '__main__':
    unittest.main(verbosity=2)
