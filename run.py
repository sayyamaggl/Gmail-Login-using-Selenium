from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


#id dump1234.mail@gmail.com
#pass - dump@1234mail

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AS5LTATnlulK_d303IiO-IgZ9BghzxHQrqA03rPWxyKTjEOcbO78OxOimOj1KCxdz9WOz4AT6lQn&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S487321577%3A1719413009042632&ddm=0")

email_id = "identifierId"
#pass_class = "whsOnd zHQkBf"

driver.get("https://google.com")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gb_I"))
)

input_element = driver.find_element(By.CLASS_NAME, "gb_I")
input_element.send_keys(Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Sign in"))
)

Button = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
Button.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, email_id))
)

input_element = driver.find_element(By.ID, email_id)
input_element.send_keys("dump1234.mail@gmail.com" + Keys.ENTER)

#try:
 # element = WebDriverWait(driver,5).until(
    #EC.presence_of_element_located((By.CLASS_NAME, "whsOnd zHQkBf")))
 #Perform actions on the element
#except TimeoutException:


#driver.implicitly_wait(7)
WebDriverWait(driver, 5).until(
   EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Enter your password')]"))
)


input_element = driver.find_element(By.NAME, "Passwd")
input_element.send_keys("dump@1234mail" + Keys.ENTER)

#Button = driver.find_element(By.CLASS_NAME, "VfPpkd-RLmnJb")
#Button.click()

time.sleep(15)

driver.quit()
