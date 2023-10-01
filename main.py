from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

driver = webdriver.Firefox()  # initialize a firefox browser
try:
    driver.get("https://www.wikipedia.org")
    key_input = driver.find_element(By.NAME, 'search')  # look for element by 'name' property
    key_input.send_keys("Automation")  # simulate typing to the above element in the session
    time.sleep(2)  # wait 2 seconds
    submit_button = driver.find_element(By.TAG_NAME, 'button')  # look for element by <tag>
    submit_button.click()  # Simulate pressing a button specified above in session
    time.sleep(2)
#    Below tells the session to wait until it finds object in DOM or for a certain amount of time if not defined
#    wait = WebDriverWait(driver, 10).until()
#    Below tells the session to poll DOM for a certain amount of time (DO NOT USE LINES 16 or 18 TOGETHER in one file)
#    driver.implicitly_wait(10)
finally:
    driver.close()  # close the window keeps session active
# --------------------------------------------------------------------
try:
    firefox = Options()  # define firefox options
    firefox.headless = True  # Enable headless mode (not visible on screen) this method is deprecated
    driver = webdriver.Firefox(options=firefox)  # Start firefox in headless mode
    driver.get("https://www.google.com")  # Load web URL
    cookies = driver.get_cookies()  # grab cookies
    for cookie in cookies:  # loop through grabbed cookies and display in console
        print(cookie)
    driver.delete_all_cookies()  # delete all cookies
    time.sleep(1)
finally:
    driver.close()
    driver.quit() # ends session
    
# --------------------------------------------------------------------

# Pulling and displaying the events off the event page of the official python website
firefox_opt = Options()
firefox_opt.add_argument("--headless") # The current process for running headless mode(for firefox) in selenium
driver = webdriver.Firefox(options=firefox_opt)
try:
    driver.get("https://www.python.org/events/")
    header = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div/div/h2')
    dates = driver.find_elements(By.TAG_NAME, 'time')
    date_list = [date.text for date in dates]
    events = driver.find_elements(By.CLASS_NAME, 'event-title')
    event_list = [event.text for event in events]
    locations = driver.find_elements(By.CLASS_NAME, 'event-location')
    location_list = [location.text for location in locations]
    # print(header.text)

    print(f"{header.text}\n")
    for index, event in enumerate(event_list):
        print(f"{event}:{date_list[index]}\n{location_list[index]}\n")

finally:
    driver.close()
    driver.quit()


