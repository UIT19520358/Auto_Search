import unittest

# import HTMLTestRunner
from reports.Runner import HTMLTestRunner
from steps.Step_search import stepSearch
from utils.CustomChromeDriver import customChrome


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("====== [Begin test] ======")
        self.browser = customChrome()
        self.browser.get("https://www.google.com/")

    def tearDown(self):
        self.browser.quit()
        print("========== [ End Test ] ========== \n")

    def test_search(self):
        keyword = "Xe hơi"
        stepSearch(self.browser).search(keyword)


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner())
