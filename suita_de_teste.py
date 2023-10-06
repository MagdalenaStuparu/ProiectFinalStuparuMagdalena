import unittest
import HTMLTestRunner

from proiect_final import Test2


class TestSuite(unittest.TestCase):
    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Test2))

        runner= HTMLTestRunner.HTMLTestRunner\
        (
            combine_reports=True,
        report_title='TestReport',
        report_name='Test Result'
        )
        runner.run(teste_de_rulat)
