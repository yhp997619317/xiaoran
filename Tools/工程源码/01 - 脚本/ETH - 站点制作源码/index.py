from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time

# 初始化
chrome = webdriver.Chrome("chromedriver")
chrome.implicitly_wait(10)
chrome.get("https://app.bitlaunch.io/login?r=m")
selector1 = 'body > app-root > div > div > div.col-lg-6.col-md-12.pl-lg-0.mt-2.mt-lg-0 > ul > li:nth-child(2) > a' # 选择服务器
selector2 = 'body > app-root > div > app-dashboard > div > div:nth-child(4) > div > div > div > table > tbody > tr:nth-child(3) > td.cursor-pointer'  # 选择服务器 -> 域名注册
selector3 = 'body > app-root > div > app-dns-records > div > app-new-record > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input' # 域名输入框
selector4 = 'body > app-root > div > app-dns-records > div > app-new-record > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > input' # 服务器IP下拉框
selector5 = 'body > app-root > div > app-dns-records > div > app-new-record > div:nth-child(2) > div:nth-child(2) > div.col-xs-2.col-md-2.col-lg-2 > div > ul > li:nth-child(1) > a' # 64.190.113.80
selector6 = 'body > app-root > div > app-dns-records > div > app-new-record > div:nth-child(2) > div:nth-child(2) > div.col-xs-2.col-md-2.col-lg-2 > div > button' # TTL（seconds）
selector7 = 'body > app-root > div > app-dns-records > div > app-new-record > div:nth-child(2) > div:nth-child(2) > div.col-xs-2.col-md-2.col-lg-2 > div > ul > li:nth-child(1) > a' # 60
# 用户密码登录
chrome.find_element(By.ID, 'email').send_keys("daobixitong4@protonmail.com")
chrome.find_element(By.ID, 'password').send_keys("qaz123123123")
chrome.find_element(By.CLASS_NAME, 'btn-lg').click()
# 域名注册界面跳转
chrome.find_element(By.CSS_SELECTOR, selector1).click()
chrome.find_element(By.CSS_SELECTOR, selector2).click()
# 获取 NFT Project 文件夹下所有项目文件夹名称，用于注册二级域名
files = os.listdir('./NFT Project')
    # print(files);
for file in files:
    chrome.find_element(By.CSS_SELECTOR, selector3).clear() # 清空输入框
    chrome.find_element(By.CSS_SELECTOR, selector3).send_keys(file) # 追加域名名称
    chrome.find_element(By.CSS_SELECTOR, selector4).click() # 关联服务器IP
    time.sleep(1)
    chrome.find_element(By.CSS_SELECTOR, selector5).click()
    time.sleep(1)
    chrome.find_element(By.CSS_SELECTOR, selector6).click() # 选择 TTL(seconds)
    time.sleep(1)
    chrome.find_element(By.CSS_SELECTOR, selector7).click()
    time.sleep(1)
