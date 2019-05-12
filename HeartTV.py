from selenium import webdriver
import unittest
import time


class heartyTV(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        print(" Open Application")
        driver = webdriver.Chrome(executable_path='/Library/Python/2.7/site-packages/chromedriver')
        driver.get("https://heartynote.com/tv")

        time.sleep(5)

    # def test_AGooglePlay(self):
    #     GoolePlay = driver.find_element_by_xpath(
    #         "//a[@href='https://play.google.com/store/apps/details?id=com.heartynote.mobileapp.heartynote']")
    #     GoolePlay.click()
    #     time.sleep(4)
    #     cur = driver.current_url
    #     print(cur)
    #     assert cur in 'https://play.google.com/store/apps/details?id=com.heartynote.mobileapp.heartynote'
    #     driver.back()

    def test_BSearch_hubs(self):
        Search = driver.find_element_by_xpath("//div[@class='search-trigger dark']")
        Search.click()
        driver.find_element_by_xpath("//input[@id='search']").send_keys("Sri")

    def test_Grabdata(self):
        Hubs = driver.find_elements_by_xpath("//div[@class='search-results']/div[@class='results-content']")
        for i in Hubs:
            print(i.text)

        time.sleep(3)
        driver.find_element_by_xpath("//div[@class='search-trigger dark']").click()

    def test_Profile(self):
        ProfileClick = driver.find_element_by_xpath("//div[@class='profile-pic']")
        ProfileClick.click()

        data = driver.find_elements_by_xpath("//div[@class='stats']")

        for d in data:
            print(d.text)

        time.sleep(5)

    def test_Text(self):
        Name = driver.find_element_by_xpath("//h1[@class='fullname']")
        print(Name.text)

    def test_Waddress(self):
        Fullname = driver.find_element_by_xpath("//div[@class='location']")
        print(Fullname.text)

    def test_Sdcription(self):
        Description = driver.find_element_by_xpath("//p[@class='description']")
        print(Description.text)

    @classmethod
    def tearDownClass(self):
        driver.close()
        print("Close Application")


if __name__ == "__main__":
    unittest.main()
