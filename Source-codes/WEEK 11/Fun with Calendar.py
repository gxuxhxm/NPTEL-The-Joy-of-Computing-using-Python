import datetime
import calendar

# Get the current date and time
current_datetime = datetime.datetime.now()
print(current_datetime)

# Create a text calendar for a specific year and month
cal = calendar.TextCalendar(calendar.SUNDAY)
cal_str = cal.formatmonth(2023, 10)
print(cal_str)

# Create a text calendar for a specific year and month
cal = calendar.TextCalendar(calendar.SUNDAY)
cal_str = cal.formatmonth(2023, 10)

# Customize the calendar by replacing characters
customized_cal = cal_str.replace("1", "X")
print(customized_cal)

# Calculate the number of days in a specific month
days_in_october = calendar.monthrange(2023, 10)[1]
print(f"October 2023 has {days_in_october} days.")

# Determine the day of the week for a specific date
day_of_week = calendar.weekday(2023, 10, 15)
print(f"October 15, 2023 is a {calendar.day_name[day_of_week]}.")

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


#Demonstrates how to determine which day of the week a given date falls on using Python's calendar module.
def get_day_from_weekday_index(weekday_index):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[weekday_index]

# Get the day of the week for a specific date
day_of_week_index = calendar.weekday(2023, 10, 15)
day_name = get_day_from_weekday_index(day_of_week_index)
print(f"October 15, 2023 falls on a {day_name}.")

#This part focuses on a task where you need to fetch the current time in different time zones.
#It utilizes the datetime and pytz libraries to achieve this.

import datetime
import pytz

# Get a list of all available time zones
time_zones = pytz.all_timezones

# Iterate through each time zone and print the current time
for zone in time_zones:
    tz = pytz.timezone(zone)
    current_time = datetime.datetime.now(tz)
    print(f"Current time in {zone}: {current_time}")