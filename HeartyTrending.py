from selenium import webdriver
import unittest
import time


class heartyTV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" Open Application")
        cls.driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')

        cls.driver.get("https://heartynote.com/")


def test_verifyTV_z(self):
    self.driver.find_element_by_xpath("//a[@href='/trending']").click()
    VideosList = self.driver.find_elements_by_xpath("//div[@id='trending-body']/a")
    time.sleep(7)
    for video in VideosList:
        video.click()
        time.sleep(7)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        print("Close Application")


if __name__ == "__main__":
    unittest.main()
