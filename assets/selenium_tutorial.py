from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import openpyxl

driver = webdriver.Chrome('/Users/macbook/Desktop/Stack/chromedriver')
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = ['A']
for letter in letters:
    driver.get('https://nysdoccslookup.doccs.ny.gov')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lst"]'))).send_keys(str(letter))
    driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[3]/form/div[2]/div[2]/div/button[1]').click()
    data = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app/div[1]/div/div[3]/div[5]/table'))).get_attribute('outerHTML')
    # print(data)
    dfs = pd.read_html(data)
    df = dfs[0]
    # print(df)
    df[['Last_Name', 'First_Name']] = df.Name.str.split(', ', expand=True)
    print(df)
    with pd.ExcelWriter('new_data.xlsx', mode='a', engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Convictions', index=False)

    
# driver.implicitly_wait(20)
# driver.get('https://nysdoccslookup.doccs.ny.gov/')
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lst"]'))).send_keys('A')
# driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[3]/form/div[2]/div[2]/div/button[1]').click()
# print(WebDriverWait(driver, 20).until(EC.visibility_of_any_elements_located((By.XPATH, '/html/body/app/div[1]/div/div[3]/div[5]/table')))).get_attribute('innerHTML')
# e = driver.find_element(By.XPATH, '//*[@id="lst"]')
# e.send_keys('A')
# e.send_keys(Keys.ENTER)
# print(driver.page_source)
# print(dfs[0])
# dfs = pd.read_html(e.send_keys(Keys.ENTER))
# print(dfs[0])

# t = driver.find_element(By.TAG_NAME, 'table')

# df = pd.DataFrame(columns=['DIN', 'Name', 'Birth Date', 'Status', 'Facility', 'Race/Ethnicity'])

# print(t.text)

# driver.get("https://www.bol.com/nl/")
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lst"]'))).click()
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="lst"]'))).send_keys("A")
# driver.find_element(By.XPATH, "/html/body/app/div[1]/div/div[3]/div[3]/form/div[2]/div[2]/div/button[1]").click()
# print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app/div[1]/div/div[3]/div[5]/table')))).__getattribute__('innerHTML')
# print(driver.__getattribute__("innerHTML"))

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC

