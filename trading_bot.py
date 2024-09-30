from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # Import the Service class
import time

class OlympTradeBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        service = Service(r"C:\chromedriver\chromedriver.exe")  # Update with the correct path to your ChromeDriver
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://olymptrade.com")
        time.sleep(2)  # Allow time for the page to load
        self.driver.find_element(By.NAME, "email").send_keys(self.email)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]").click()
        time.sleep(5)  # Wait for login to complete

        # Check if login was successful
        try:
            # Change this selector to something that indicates a successful login
            self.driver.find_element(By.XPATH, "//div[@class='profile-icon']")  # Example selector
            print("Connected successfully.")
        except:
            print("Failed to connect.")

    def fetch_trade_history(self):
        self.driver.get("YOUR_TRADE_HISTORY_URL")  # Replace with the actual trade history URL
        time.sleep(5)  # Allow time for the page to load
        # Extract trade results using BeautifulSoup or directly with Selenium
        # For example, to print the page source:
        print(self.driver.page_source)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = OlympTradeBot("vaultguard41@gmail.com", "King@2005")
    bot.login()
    bot.fetch_trade_history()
    bot.close()
