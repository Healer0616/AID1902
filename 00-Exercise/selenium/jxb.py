from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://test.i31.com/jxb/index.html#/mobilePay")
time.sleep(2)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/input').send_keys('admin')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/input').send_keys('123456')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[5]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]/div').click()
time.sleep(1)
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
js = "var action=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(3)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]/ul/li[1]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]/ul/li[2]').click()
time.sleep(1)
browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div/label[2]/span[1]/span').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[2]/ul/li[2]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[3]/div').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[3]/ul/li[1]').click()
time.sleep(1)
browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div[1]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[7]/div/div/div[2]/div[2]/div[1]').click()
time.sleep(1)
browser.find_element_by_xpath(
    '//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[4]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[7]/div/div/div[2]/div[2]/div[1]').click()
time.sleep(3)
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div/ul/li[4]/div').click()
time.sleep(1)
browser.close()