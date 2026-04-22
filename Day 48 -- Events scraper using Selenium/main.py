from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.python.org/")

events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li')

event_dict = {}
event_number = 1

for item in events:
    time_element = item.find_element(By.TAG_NAME, "time")
    link_element = item.find_element(By.TAG_NAME, "a")

    time_text = time_element.text
    link_text = link_element.text

    event_dict[f"Event {event_number}"] = {
        "Date":time_text,
        "Event":link_text
    }
    event_number += 1
driver.quit()

print(event_dict)
