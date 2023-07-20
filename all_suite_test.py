import unittest

from unittest.loader import makeSuite

from test_cases.Fill_addplayer_form import TestFillAddPLayer
from test_cases.login_with_no_credentials import TestLoginNoCreds
from test_cases.Login_incorrect_password import TestLoginIncorrect
from test_cases.login_to_the_system import TestLoginPage
from test_cases.Remind_password import TestRemindPassword
from test_cases.Addplayer import TestAddPLayer
from test_cases.sign_out import TestSignOut
from test_cases.framework import Test


def full_suite():
    # test_suite = unittest.TestLoader()
    # test_suite.loadTestsFromTestCase(TestLoginIncorrectPW)
    # test_suite.loadTestsFromTestCase(TestLoginNoCreds)
    # test_suite.loadTestsFromTestCase(TestLoginPage)
    # test_suite.loadTestsFromTestCase(TestRemindPassword)
    # test_suite.loadTestsFromTestCase(TestFillAddPLayer)
    # test_suite.loadTestsFromTestCase(TestSignOut)
    # test_suite.loadTestsFromTestCase(TestAddPLayer)
    # test_suite.loadTestsFromTestCase(Test)
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginIncorrect))
    test_suite.addTest(makeSuite(TestLoginNoCreds))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestRemindPassword))
    test_suite.addTest(makeSuite(TestFillAddPLayer))
    test_suite.addTest(makeSuite(TestSignOut))
    test_suite.addTest(makeSuite(TestAddPLayer))
    test_suite.addTest(makeSuite(Test))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
