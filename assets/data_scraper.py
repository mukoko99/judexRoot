from bs4 import BeautifulSoup
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

init = {'DIN':[],'Last Name': [], 'First Name': [], 'D.O.B': [], 'Age': [], 'Race': [],'County of Commitment': [], 'Status': [], 'Prison': [], 'Date of Incarceration': [], 'Date Sentence Starts': [], 'Release Date': [], 'Agg Min Sentence': [], 'Agg Max Sentence': [], 'Duration of Incarceration': []}
df = pd.DataFrame(data=init)
print(df)
url = 'https://nysdoccslookup.doccs.ny.gov/'
driver = webdriver.Chrome('/Users/macbook/Desktop/Stack/chromedriver')
driver.get(url)
WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="lst"]'))).send_keys('A')
driver.find_element(By.XPATH, "/html/body/app/div[1]/div/div[3]/div[3]/form/div[2]/div[2]/div/button[1]").click()
WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '/html/body/app/div[1]/div/div[3]/div[5]/table')))
n = 1
flag = True
while flag:
    # driver.find_element.get_attribute('innerHTML')
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '/html/body/app/div[1]/div/div[3]/div[5]/table/tbody/tr[{}]/td[1]/a'.format(n)))).click()
    crime = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[4]/div/table'))).get_attribute('outerHTML')
    # data1 = pd.read_html(data)
    # print(data1)
    crime = pd.read_html(crime)
    lastName = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[1]/div/h3').text.split(', ')[0]
    firstName = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[1]/div/h3').text.split(', ')[1]
    din = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[2]').text[5:]
    age = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[4]/div[3]').text.split(' ')[0]
    dob = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[4]/div[2]').text
    race = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[4]/div[1]').text
    status = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[5]/div[2]').text
    prison = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[6]/div[2]').text
    county = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[7]/div[2]').text
    incarcerationDate = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[8]/div[2]').text
    sentenceStart = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[1]/div[1]/div[9]/div[2]').text
    releaseDate = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[2]/div/span[2]').text
    aggMinSentence = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[7]/div[2]').text
    aggMaxSentence = driver.find_element(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[4]/div[2]/div[8]/div[2]').text
    if len(firstName.split(' ')) > 1:
        middleName = firstName.split(' ')[1]
    mockData = {'DIN': [din],'Last Name': [lastName], 'First Name': [firstName], 'D.O.B': [dob], 'Age': [age], 'Race': [race],'County of Commitment': [county], 'Status': [status], 'Prison': [prison], 'Date of Incarceration': [incarcerationDate], 'Date Sentence Starts': [sentenceStart], 'Release Date': [releaseDate], 'Agg Min Sentence': [aggMinSentence], 'Agg Max Sentence': [aggMaxSentence], 'Duration of Incarceration': []}
    mockDF = pd.DataFrame.from_dict(mockData, orient='index')
    mockDF = mockDF.transpose()
    init = pd.concat([df,mockDF])
    # print(init)
    # incarcerationDuration = 
    n += 1
    flag = False

# elements = driver.find_elements(By.XPATH, '/html/body/app/div[1]/div/div[3]/div[5]/table/tbody/tr/td/a')
# elements = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, '/html/body/app/div[1]/div/div[3]/div[5]/table/tbody/tr/td/a')))
# for element in elements:
    # element.click()
    # print(element.get_attribute('innerHTML'))
    
# print(len(elements))