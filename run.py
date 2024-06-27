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





email_id = "identifierId"
#pass_class = "whsOnd zHQkBf"





class Gmail:

    
  
  @staticmethod
  def Locate():
        
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "gb_I")))
        input_element = driver.find_element(By.CLASS_NAME, "gb_I")
        input_element.send_keys(Keys.ENTER)
        
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Sign in")))
        
        Button = driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        Button.click()
        
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, email_id)))
        
  @staticmethod      
  def USERID():
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, email_id)))
        input_element = driver.find_element(By.ID, email_id)
        input_element.send_keys("dump1234.mail@gmail.com" + Keys.ENTER)
    
  @staticmethod 
  def PASS():
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Enter your password')]")))
        input_element = driver.find_element(By.NAME, "Passwd")
        input_element.send_keys("dump@1234mail" + Keys.ENTER)

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://google.com")
run = Gmail()
run.Locate()
run.USERID()
run.PASS()

time.sleep(15)
