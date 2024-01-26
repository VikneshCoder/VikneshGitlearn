import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class MyBot():
    def viky(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")

        # Wait for the element to become clickable
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Yatra for Business")))

        # Click the element
        element.click()

        time.sleep(5)
        driver.quit()


bot = MyBot()
bot.viky()
