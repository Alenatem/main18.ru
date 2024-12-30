from selenium import webdriver
#from selenium.webdriver import Keys
#from time import sleep
#import datetime
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains


file = open("log.txt", "w")
#driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option(name='detach', value=True)
#options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get('http://demoqa.com/radio-button')
driver.maximize_window()

Impressive_radio = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/label')
Impressive_radio.click()

correct_text = "Impressive"
current_text = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p/span')
assert correct_text == current_text.text, 'text not matches'
file.write('text matches')
