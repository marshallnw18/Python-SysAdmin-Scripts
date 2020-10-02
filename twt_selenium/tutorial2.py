from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Pull correct version of the chrome webdriver and install it rather than manually specifying the local filepath
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open a webpage in Chrome
driver.get("https://techwithtim.net/")

link = driver.find_element_by_link_text("Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, "sow-button-19310003"))
    )
    element.click()
except:
    driver.quit()