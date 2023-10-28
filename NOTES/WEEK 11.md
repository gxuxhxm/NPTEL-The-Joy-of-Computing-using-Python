## Browser Automation
---
### Explaination
**Step 1: Import Required Libraries**
- Import necessary libraries such as Selenium, WebDriverWait, expected_conditions, keys, by, and time. These libraries enable you to automate interactions with web pages.
**Step 2: Initialize the Web Driver**
- Initialize a web driver (in this case, Chrome) by providing the path to the ChromeDriver executable. The web driver is essential for controlling and interacting with web browsers.
**Step 3: Open WhatsApp Web**
- Use the web driver to navigate to the WhatsApp Web URL (https://web.whatsapp.com/), which opens the WhatsApp Web page in a web browser.
**Step 4: Scan QR Code**
- Manually scan the QR code displayed on the web page using the WhatsApp mobile app. This step is necessary to link the web application with your WhatsApp account.
**Step 5: Define Recipient and Message**
- Define the recipient's name (in this example, "Ravi Kiran") and the message you want to send (e.g., "Message sent using Python"). These will be used in the automation script.
**Step 6: Locate the Recipient's Chat**
- Use the Selenium library to locate the chat of the recipient by their name. WhatsApp Web typically uses a span element with a title attribute to identify chats. The `find_element_by_xpath` method is used for this purpose.
**Step 7: Locate the Text Input Box**
- Find the input box (text field) where you can send your message. This text input box can be located using a class name. The `find_element_by_class_name` method is employed to find this element.
**Step 8: Send Multiple Messages**
- Utilize a loop to send multiple messages to the recipient. In this example, 50 messages are sent. Inside the loop, the message text is entered into the input box, and the Enter (RETURN) key is simulated to send the message. A `time.sleep()` pause is added to prevent sending messages too quickly.
**Step 9: Close the Browser**
- Once you've sent the desired number of messages, you can close the web browser. The `driver.quit()` method is used to close the browser window.
- 
Please note that you need to replace `'path_to_chromedriver.exe'` with the actual path to the ChromeDriver executable on your system for this script to work correctly.

### To automate WhatsApp using Python and Selenium, you'll need to follow these steps and explanations:

**Step 1: Import Libraries**
- Import the required libraries, including Selenium, WebDriverWait, expected_conditions, keys, by, and time.

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
```

**Step 2: Initialize the Web Driver**
- Initialize the web driver (in this example, Chrome) and provide the path to the ChromeDriver executable.

```python
driver = webdriver.Chrome('path_to_chromedriver.exe')
```

**Step 3: Open WhatsApp Web**
- Open WhatsApp Web by navigating to the WhatsApp Web URL.

```python
driver.get("https://web.whatsapp.com/")
```

**Step 4: Scan QR Code**
- Manually scan the QR code using your WhatsApp mobile app to link the web application with your WhatsApp account.

**Step 5: Define Recipient and Message**
- Define the recipient's name and the message you want to send.

```python
recipient_name = "Ravi Kiran"
message_text = "Message sent using Python"
```

**Step 6: Locate the Recipient's Chat**
- Use Selenium to locate the chat of the recipient by their name. WhatsApp web typically uses a span element with the title attribute to identify chats.

```python
xpath = f"//span[contains(@title, '{recipient_name}')]"
target = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath)))
target.click()
```

**Step 7: Locate the Text Input Box**
- Find the input box (text field) where you can send your message. It's usually located using a class name.

```python
input_box = driver.find_element(By.CLASS_NAME, "_1Plpp")
```

**Step 8: Send Multiple Messages**
- Use a loop to send multiple messages to the recipient.

```python
for i in range(50):  # Sending 50 messages
    input_box.send_keys(message_text)
    input_box.send_keys(Keys.RETURN)
    time.sleep(1)  # Add a pause to avoid sending messages too quickly
```

**Step 9: Close the Browser**
- After you've sent your messages, you can close the browser.

```python
driver.quit()
```

Here's the full code block with sample output:

```python
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
```

Please note that you need to replace `'path_to_chromedriver.exe'` with the actual path to the ChromeDriver executable on your system. Additionally, this script sends 50 messages as an example, but you can adjust the loop count as needed.

## Fun with Calendar
---
**FUN WITH CALENDAR: 01**

- Introduction to the series, highlighting the exploration of calendar-related tasks and functions in Python.

**FUN WITH CALENDAR: 02**

- Discusses the importance of calendars in daily life, not just for dates but for organizing time and events.
- Emphasizes the relevance of understanding calendar systems.

**FUN WITH CALENDAR: 03**

- Highlights the use of calendars in various domains, including programming, events, scheduling, and more.
- Understanding the use cases of calendars is crucial for Python programming.

**FUN WITH CALENDAR: 04**

- Discusses key calendar concepts such as days of the week, months, and years.
- Explains the concept of leap years and how they impact calendar systems.

**FUN WITH CALENDAR: 05**

- Introduction to Python's `datetime` module, which provides tools for working with dates and times.
- Covers various functions within the module and how they can be used for calendar-related tasks.

```python
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()
print(current_datetime)
```

**Sample Output:**
```
2023-10-15 15:30:00.123456
```

**FUN WITH CALENDAR: 06**

- Overview of Python's `calendar` module, used for working with calendars and date-related functions.
- Demonstrates how to create and display calendars.

```python
import calendar

# Create a text calendar for a specific year and month
cal = calendar.TextCalendar(calendar.SUNDAY)
cal_str = cal.formatmonth(2023, 10)
print(cal_str)
```

**Sample Output:**
```
    October 2023
Su Mo Tu We Th Fr Sa
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
```

**FUN WITH CALENDAR: 07**

- Explores creating a simple calendar and customizing its appearance using the `calendar` module.
- Demonstrates creating a text-based calendar and manipulating its layout.

```python
import calendar

# Create a text calendar for a specific year and month
cal = calendar.TextCalendar(calendar.SUNDAY)
cal_str = cal.formatmonth(2023, 10)

# Customize the calendar by replacing characters
customized_cal = cal_str.replace("1", "X")
print(customized_cal)
```

**Sample Output:**
```
    October 2023
Su Mo Tu We Th Fr Sa
 X  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
```

**FUN WITH CALENDAR: 08**

- Explores more advanced operations with the `calendar` module, including calculating the number of days in a month and determining the day of the week for a given date.

```python
import calendar

# Calculate the number of days in a specific month
days_in_october = calendar.monthrange(2023, 10)[1]
print(f"October 2023 has {days_in_october} days.")

# Determine the day of the week for a specific date
day_of_week = calendar.weekday(2023, 10, 15)
print(f"October 15, 2023 is a {calendar.day_name[day_of_week]}.")
```

**Sample Output:**
```
October 2023 has 31 days.
October 15, 2023 is a Sunday.
```

**FUN WITH CALENDAR: 09**

- Explains how to check if a given date is valid by considering leap years, months, and their respective days.
- Provides code to validate a date and determine if it's a valid calendar date.

```python
def check_valid_date(year, month, date):
    # Check if it's a leap year
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if month == 2:  # February
        if is_leap and date <= 29:
            return True
        if not is_leap and date <= 28:
            return True
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return date <= 30
    elif month in [1, 3, 5, 7, 8, 10, 12]:  # January, March, May, July, August, October, December
        return date <= 31

    return False

# Example usage
year = 2023
month = 10
date = 15
is_valid = check_valid_date(year, month, date)
print(f"Is {month}/{date}/{year} a valid date? {is_valid}")
```

**Sample Output:**
```
Is 10/15/2023 a valid date? True
```

**FUN WITH CALENDAR: 10**

- Demonstrates how to determine which day of the week a given date falls on using Python's `calendar` module.
- A custom function is used to convert the weekday index into a human-readable day name.

```python
import calendar

def get_day_from_weekday_index(weekday_index):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[weekday_index]

# Get the day of the week for a specific date
day_of_week_index = calendar.weekday(2023, 10, 15)
day_name = get_day_from_weekday_index(day_of_week_index)
print(f"October 15, 2023 falls on a {day_name}.")
```

**Sample Output:**
```
October 15, 2023 falls on a Sunday.
```

**FUN WITH CALENDAR: 11**

- This part focuses on a task where you need to fetch the current time in different time zones.
- It utilizes the `datetime` and `pytz` libraries to achieve this.

```python
import datetime
import pytz

# Get a list of all available time zones
time_zones = pytz.all_timezones

# Iterate through each time zone and print the current time
for zone in time_zones:
    tz = pytz.timezone(zone)
    current_time = datetime.datetime.now(tz)
    print(f"Current time in {zone}: {current_time}")
```

**Sample Output:**
```
Current time in Africa/Abidjan: 2023-10-15 20:30:00
Current time in Africa/Accra: 2023-10-15 20:30:00
Current time in Africa/Addis_Ababa: 2023-10-16 00:30:00
...
Current time in Pacific/Wallis: 2023-10-16 06:30:00
Current time in US/Alaska: 2023-10-15 12:30:00
Current time in US/Arizona: 2023-10-15 13:30:00
...
```

**FUN WITH CALENDAR: 12**

- In this part, you wrap up the series and explain the significance of the task of fetching the current time in different time zones.
- It showcases the power of Python in easily accomplishing such tasks and emphasizes the speed and versatility of Python programming.

**Summary of the Series:**

1. Introduction to the series and the exploration of calendar-related tasks in Python.
2. The importance of calendars in daily life and various domains.
3. The use cases of calendar systems in Python programming.
4. Key calendar concepts, including days of the week, months, and leap years.
5. Introduction to Python's `datetime` module for working with dates and times.
6. Using the `calendar` module to create and customize calendars.
7. Advanced operations with the `calendar` module, such as calculating days in a month and determining the day of the week.
8. Checking for valid dates by considering leap years and months.
9. Determining the day of the week for a given date using Python's `calendar` module.
10. Fetching the current time in various time zones using the `datetime` and `pytz` libraries.
11. An overview of the entire series, summarizing the key topics and tasks explored.
12. Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)

