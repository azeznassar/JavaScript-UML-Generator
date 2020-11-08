"""
Unit Testing with Python
http://www.drdobbs.com/testing/unit-testing-with-python/240165163?pgno=1

https://docs.python.org/3/library/unittest.html
"""

from tests.test_current_cmd_a import CmdATests
from tests.test_input_handler import InputHandlerTests

import unittest


def suite():
    the_suite = unittest.TestSuite()
    '''
    suite1.addTest(FooTests1("test_one"))
    suite1.addTest(FooTests1("test_two"))
    suite1.addTest(FooTests1("test_hello_world"))
    suite1.addTest(FooTests2("test_three"))
    '''
    the_suite.addTest(unittest.makeSuite(CmdATests))
    the_suite.addTest(unittest.makeSuite(InputHandlerTests))
    return the_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    # runner = unittest.TextTestRunner(descriptions=True, verbosity=2)
    test_suite = suite()
    runner.run(test_suite)
