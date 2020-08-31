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

# Print webpage title
print(driver.title)

# Interact with page elements
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

# webdriver will wait 10 seconds to see if the presence of the ID main is located
# otherwise it will exit
try:
    main = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # find all elements inside "main" with the article tag
    articles = main.find_elements_by_tag_name("article")
    # loop through those articles and print out the article summaries
    for article in articles:
        summary = article.find_element_by_class_name("entry-summary")
        print(summary.text)
finally:
    # Close all chrome windows
    driver.quit()