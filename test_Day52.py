
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

similar_account = "dinesh.etah457@gmail.com"
username = "dinesh.etah457@gmail.com"
PASSWORD = "Chandra@123"

class InstaFollower:
    def __init__(self):
        # Initialize WebDriver
        self.driver = webdriver.Chrome()
        
    def login(self, url):  # Accept URL as argument
        self.driver.get(url)  # Navigate to the provided URL
        time.sleep(1.2)

        username_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="dinesh.etah457@gmail.com"]')
        username_input.send_keys("dinesh.etah457@gmail.com")

   
        # Check if the cookie warning is present on the page 
        decline_cookies_xpath = "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"
        cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
        if cookie_warning:
            # Dismiss the cookie warning by clicking an element or button 
            cookie_warning[0].click()

        username = self.driver.find_element(by=By.NAME, value="dinesh.etah457@gmail.com")
        password = self.driver.find_element(by=By.NAME, value="Chandra@123")

        username.send_keys(username)
        password.send_keys(password)

        time.sleep(2.1)
        password.send_keys("dinesh.enter")

        time.sleep(4.3)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()
        
        time.sleep(3.7)
        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()


    def find_followers(self):
        pass

    def follow(self):
        pass

bot = InstaFollower()
url = "https://www.instagram.com/accounts/login/"
bot.login(url)  # Pass URL when calling login()
bot.find_followers()
bot.follow()
