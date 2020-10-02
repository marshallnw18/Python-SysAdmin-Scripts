import time

from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Swiper():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tinder_login(self):
        self.driver.get('https://tinder.com/')
        loginbutton = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div"))
        )
        loginbutton.click()

        time.sleep(5)
        phonelogin = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[3]/button")
        phonelogin.click()
        time.sleep(5)
        phonenumber = self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div[2]/div/input")
        phonenumber.send_keys(input('Opened Tinder. Please enter your phone number: '))
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/button").click()

        time.sleep(5)
        verificationcode = input('Please enter the 6 digit authentication code sent to your phone number: ')
        verificationcode = list(verificationcode)
        #validate that the code is 6 digits before proceeding 

        #iterating through 6 digit verifcation code fields
        for number in verificationcode:
            time.sleep(2)
            # check xpaths if the sleep timer doesn't work 
            verificationfield = self.driver.find_element_by_xpath(f"/html/body/div[2]/div/div/div[1]/div[3]/input[{verificationcode.index(number) + 1}]")
            verificationfield.send_keys(f"{number}")

if __name__ == "__main__":
    swiper = Swiper()
    swiper.tinder_login()