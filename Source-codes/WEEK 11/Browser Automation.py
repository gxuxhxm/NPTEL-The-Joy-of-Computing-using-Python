from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the web driver
driver = webdriver.Chrome('path_to_chromedriver.exe')

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Scan the QR code manually with your WhatsApp mobile app

# Define recipient and message
recipient_name = "Ravi Kiran"
message_text = "Message sent using Python"

# Locate the recipient's chat
xpath = f"//span[contains(@title, '{recipient_name}')]"
target = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath)))
target.click()

# Locate the text input box
input_box = driver.find_element(By.CLASS_NAME, "_1Plpp")

# Send multiple messages
for i in range(50):  # Sending 50 messages
    input_box.send_keys(message_text)
    input_box.send_keys(Keys.RETURN)
    time.sleep(1)  # Add a pause to avoid sending messages too quickly

# Close the browser
driver.quit()