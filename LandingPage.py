from selenium import webdriver
import unittest
import time


class LoginORM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Open Application")
        cls.driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')

        cls.driver.get("https://heartynote.com/")

    def test_Homepage_Blog(self):
        self.driver.find_element_by_xpath("//a[text()='Blog']").click()
        time.sleep(5)
        cur = self.driver.current_url
        expt = 'http://blog.heartynote.com/'
        assert cur in "http://blog.heartynote.com/"
        self.driver.back()

    def test_Homepage_About(self):
        self.driver.find_element_by_xpath("//a[text()='About']").click()
        time.sleep(5)
        cur = self.driver.current_url
        expt = 'http://blog.heartynote.com/'
        assert cur in "http://blog.heartynote.com/"
        self.driver.back()

    def test_VerifyGoogleLink(self):
        self.driver.find_element_by_xpath("//img[@class='download']").click()
        time.sleep(4)
        cur = cur = self.driver.current_url
        assert cur in 'https://play.google.com/store/apps/details?id=com.heartynote.mobileapp.heartynote'
        self.driver.back()

    def test_verfiyStatus_text(self):
        statusText = self.driver.find_element_by_xpath(
            "//span[text()='Let hearty people know what you are feeling now or currently occupied with.']")
        WebStore = statusText.text
        assert WebStore in 'Let hearty people know what you are feeling now or currently occupied with.'

    def test_verifyHub_text(self):
        statusText = self.driver.find_element_by_xpath(
            "//span[text()='A place to store your notes. Save all your notes in different hubs according to your convenience.']")
        WebStore = statusText.text
        assert WebStore in 'A place to store your notes. Save all your notes in different hubs according to your convenience.'
        time.sleep(7)

    def test_verifyTV_text(self):
        statusText = self.driver.find_element_by_xpath(
            "//span[text()='A place to watch most interesting videos recommended especially for you.']")
        WebStore = statusText.text
        assert WebStore in 'A place to watch most interesting videos recommended especially for you.'
        time.sleep(4)

    def test_verify_FB(self):
        self.driver.find_element_by_xpath("//a[text()='Facebook']").click()
        cur = self.driver.current_url
        assert cur in 'https://www.facebook.com/heartynote'
        time.sleep(2)
        self.driver.back()

    def test_verifyTV_Instragram(self):
        self.driver.find_element_by_xpath("//a[text()='Instagram']").click()
        cur = self.driver.current_url
        assert cur in 'https://www.instagram.com/heartynote.official/'
        time.sleep(2)
        self.driver.back()

    def test_verifyTV_Privicy(self):
        self.driver.find_element_by_xpath("//a[text()='Privacy policy']").click()
        cur = self.driver.current_url
        assert cur in 'https://heartynote.com/privacy_policy.html'
        time.sleep(2)
        self.driver.back()

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        print("All tests passed & Close the applications")


if __name__ == "__main__":
    unittest.main()
