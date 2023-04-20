from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

def automate():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://computer-database.gatling.io/computers")
    time.sleep(5)
    add_computer = driver.find_element(by=By.ID, value="add")

    add_computer.click()
    time.sleep(5)

    name = driver.find_element(by=By.ID, value="name")
    name.send_keys('ASUS')

    introduced = driver.find_element(by=By.ID, value="introduced")
    introduced.send_keys('2015-02-03')

    discontinued = driver.find_element(by=By.ID, value="discontinued")
    discontinued.send_keys('2017-02-03')

    company = driver.find_element(by=By.ID, value="company")
    select = Select(company)
    select.select_by_visible_text("ASUS")

    button = driver.find_element(by=By.CSS_SELECTOR, value="input[type='submit'][value='Create this computer']")
    button.click()

    time.sleep(5)




    # title = driver.title
    # assert title == "Web form"
    #
    # driver.implicitly_wait(0.5)
    #
    # text_box = driver.find_element(by=By.NAME, value="my-text")
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    #
    # text_box.send_keys("Selenium")
    # driver.implicitly_wait(5000)
    # submit_button.click()
    #
    # message = driver.find_element(by=By.ID, value="message")
    # value = message.text
    # assert value == "Received!"

    # driver.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    automate()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
