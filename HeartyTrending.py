from selenium import webdriver
import unittest
import time


class heartyTV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(" Open Application")
        cls.driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')
        cls.driver.get("https://heartynote.com")

        time.sleep(5)

    def test_PlayAllVideos(self):
        VideoViews = self.driver.find_elements_by_xpath("//div[@class='trending-content']/a")
        for videos in VideoViews:
            videos.click()
            time.sleep(8)
            self.driver.back()

    @classmethod
    def tearDownClass(self):
        # self.driver.close()
        print("Close Application")


if __name__ == "__main__":
    unittest.main()
