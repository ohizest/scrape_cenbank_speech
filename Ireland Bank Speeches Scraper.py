import time
import csv
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to validate date format
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False


# This function is relevant in line 71 to help convert and print the dates in separate lines for year, month, and day
def format_date(date_str):
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    return date_obj.strftime('%Y'), date_obj.strftime('%B'), date_obj.strftime('%d')


# Prompt the user for a start date
while True:
    start_date_str = input("Enter the start date (dd/mm/yyyy): ")
    if is_valid_date(start_date_str):
        break
    else:
        print("Invalid date format. Please enter the date in dd/mm/yyyy format.")

# Prompt the user for an end date
while True:
    end_date_str = input("Enter the end date (dd/mm/yyyy): ")
    if is_valid_date(end_date_str):
        break
    else:
        print("Invalid date format. Please enter the date in dd/mm/yyyy format.")

print('Accessing website.....')
time.sleep(0.2)
driver = webdriver.Firefox()
driver.get("https://www.centralbank.ie/news-media/speeches")
driver.maximize_window()
time.sleep(1)

# Line 48 to 55 is code to force the dates to have leading zeros in the format to be used in XPATH
# Split the input into day, month, and year components
day, month, year = start_date_str.split('/')
# Format the date with leading zeros
formatted_start_date = f"{month.zfill(2)}/{day.zfill(2)}/{year}"
# Split the input into day, month, and year components
day, month, year = end_date_str.split('/')
# Format the date with leading zeros
formatted_end_date = f"{month.zfill(2)}/{day.zfill(2)}/{year}"

# Check if the "Accept all cookies" popup is present and click if it is
try:
    accept_all_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler'] "))
    )
    accept_all_button.click()
except:
    pass

calendar_drop_down = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='fa fa-caret-down']"))
            )
time.sleep(5)
calendar_drop_down.click()
time.sleep(2)

# Convert and print the dates in separate lines for year, month, and day
start_year, start_month, start_day = format_date(start_date_str)
end_year, end_month, end_day = format_date(end_date_str)
target_month_year_start = start_month + ' ' + start_year
target_month_year_end = end_month + ' ' + end_year

# Concatenate selected start month and year strings
selected_month_year = driver.find_element(By.XPATH, "//th[@title='Select Month']").get_attribute("innerHTML")
selected_start_year = (selected_month_year.split())[-1]
selected_month = (selected_month_year.split())[0]

# Navigate through the calendar to go to the required start year
# and then the required start month

while selected_month_year != target_month_year_start:
    if (int(start_year)) < int(selected_start_year):
        # Click the next button
        previous_click = driver.find_element(By.XPATH, "//span[@title='Previous Month']")
        previous_click.click()
        time.sleep(1)
        selected_month_year = driver.find_element(By.XPATH, "//th[@title='Select Month']").get_attribute("innerHTML")
        target_month_year_start = start_month + ' ' + start_year

    elif (int(start_year)) == int(selected_start_year):
        while start_month != selected_month:
            previous_click = driver.find_element(By.XPATH, "//span[@title='Previous Month']")
            previous_click.click()
            time.sleep(1)
            selected_month_year = driver.find_element(By.XPATH, "//th[@title='Select Month']").get_attribute(
                "innerHTML")
            selected_month = (selected_month_year.split())[0]

    else:
        next_click = driver.find_element(By.XPATH, "//span[@title='Next Month']")
        next_click.click()
        time.sleep(1)
        selected_month_year = driver.find_element(By.XPATH, "//th[@title='Select Month']").get_attribute("innerHTML")
        target_month_year_start = start_month + ' ' + start_year

# After selecting the correct year and month, click on the specific day
day_xpath = f"//td[@data-day='{formatted_start_date}']"
target_start_day = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, day_xpath))
            )
target_start_day.click()
time.sleep(1)

calendar_drop_down2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='datetimepickerToNews']//span[@class='fa fa-caret-down']"))
            )
calendar_drop_down2.click()
time.sleep(2)

# Navigate through the calendar to go to the required end_year
# and then the required end_month
while selected_month_year != target_month_year_end:
    if (int(end_year)) < int(selected_start_year):
        # Click the next button
        previous_click = driver.find_element(By.XPATH, "//span[@title='Previous Month']")
        previous_click.click()
        time.sleep(1)
        selected_month_year = driver.find_element(By.XPATH, "//th[@title='Select Month']").get_attribute("innerHTML")
        target_month_year_end = end_month + ' ' + end_year

    elif (int(end_year)) == int(selected_start_year):
        while end_month != selected_month:
            previous_click = driver.find_element(By.XPATH, "//span[@title='Previous Month']")
            previous_click.click()
            time.sleep(1)
            selected_month_year = driver.find_element(By.XPATH, "//th[@title='Select Month']").get_attribute(
                "innerHTML")
            selected_month = (selected_month_year.split())[0]

    else:
        next_click = driver.find_element(By.XPATH, "//span[@title='Next Month']")
        next_click.click()
        time.sleep(1)
        selected_month_year = driver.find_element(By.XPATH, "//th[@title='Select Month']").get_attribute("innerHTML")
        target_month_year_end = end_month + ' ' + end_year

# After selecting the correct year and month, click on the specific day
day_xpath = f"//td[@data-day='{formatted_end_date}']"
target_end_day = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, day_xpath))
            )
target_end_day.click()
time.sleep(1)
# This code selects the speech category
select_category = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Choose a category']")))
select_category.click()
time.sleep(1)
speech = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='text'][normalize-space()='Speech']")))
speech.click()
time.sleep(1)


# Click on filter after selecting start and end date
filter_search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='col-sm-2']/a")))
filter_search.click()
time.sleep(2)

# Create a list of dictionaries to store the data
output_columns = []

while True:
    speaker_names = driver.find_elements(By.XPATH, "//div[@class='spotlight fixed-lines spotlight-wide new-story']//img")
    speech_dates = driver.find_elements(By.XPATH, "//div[@class='spotlight-content ']//descendant::span[1]")
    speech_titles = driver.find_elements(By.XPATH, "//div[@class='spotlight-content ']//a/h4")
    speech_urls = driver.find_elements(By.XPATH, "//div[@class='spotlight-content ']//a")

    # Extract and store the data in dictionaries
    for speaker_name, speech_date, speech_title, speech_url in zip(speaker_names, speech_dates, speech_titles, speech_urls):
        output = {
            "speaker_name": speaker_name.get_attribute("title"),
            "speech_date": speech_date.get_attribute("innerHTML"),
            "speech_title": speech_title.get_attribute("innerHTML"),
            "speech_url": speech_url.get_attribute("href")
        }
        output_columns.append(output)
        time.sleep(1)

    try:
        next_page1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[@class='next-page']//a")))
        next_page = next_page1.get_attribute("href")
        print('Scraping:', next_page)
        if next_page != '#':
            next_page1.click()
            time.sleep(2)  # Added a sleep to give the page time to load
        else:
            break
    except TimeoutException:
        print("Reached the end of pagination.")
        break

# Define the CSV file name
csv_file = "Ireland_Bank_speech1.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["speaker_name", "speech_date", "speech_title", "speech_url"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the book data
    for book in output_columns:
        writer.writerow(book)

print(f"Data has been exported to {csv_file}")
# Close the driver when you are done
# driver.quit()
