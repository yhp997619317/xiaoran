import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 批量注册子域名
# 初始化
chrome = webdriver.Chrome("chromedriver")
chrome.get("https://clients.hostwinds.com/cloud/dns-manager.php")
chrome.implicitly_wait(20)
selector1 = '#dns_manager-43463 > td:nth-child(5) > div.dropdown.open > ul > li:nth-child(1)'  # 点击跳转子路由新增页面

# 用户密码登录
chrome.find_element(By.ID, 'inputEmail').send_keys("daobiyouxiang@protonmail.com")
chrome.find_element(By.ID, 'inputPassword').send_keys("Qaz123123123..")
chrome.find_element(By.ID, 'login').click()
# 域名注册界面跳转
chrome.implicitly_wait(20)
chrome.find_element(By.ID, 'dropdown-43463').click()
chrome.find_element(By.CSS_SELECTOR, selector1).click()
# 获取 NFT Project 文件夹下所有项目文件夹名称，用于注册二级域名
with os.scandir('./NFT Project') as projects:
    for project in projects:
        chrome.implicitly_wait(20)
        chrome.find_element(By.ID, 'dns-name').clear()  # 清空输入框,追加域名名称
        chrome.find_element(By.ID, 'dns-name').send_keys(project.name)
        chrome.find_element(By.ID, 'dns-value').clear()  # 清空输入框,追加域名IP
        chrome.find_element(By.ID, 'dns-value').send_keys('104.168.142.223')
        chrome.find_element(By.ID, 'dns-ttl').clear()  # 清空输入框,TTL 时间
        chrome.find_element(By.ID, 'dns-ttl').send_keys('60')
        chrome.find_element(By.ID, 'dns-add').click()

# 批量生成站点文件站点文件
filterText = 'Wobblebug'  # 需要替换的关键字
# 初始化删除
try:
    shutil.rmtree('./dist')
except OSError as e:
    print(f'Error: ./dist : {e}')
# 复制模板文件到输出文件夹
with os.scandir('./NFT Project') as srcs:
    for project in srcs:
        shutil.copytree('./Wobblebug', 'dist/' + project.name)
# 替换关键字
with os.scandir('./dist') as dists:
    for distFile in dists:
        # 只读形式打开文件
        with open(distFile.path + '/settings.js', 'r', encoding='UTF-8') as settingJS:
            # 文件内容赋值变量存储
            settingJSStr = settingJS.read()
            # 单词替换
            settingJSStr = settingJSStr.replace(filterText, distFile.name)
        # 覆盖写入替换后的内容
        with open(distFile.path + '/settings.js', 'w', encoding='UTF-8') as settingJS:
            settingJS.write(settingJSStr)
# 复制图片到输出文件下对应的项目中
with os.scandir('./NFT Project') as NFTProject:
    for project in NFTProject:
        with os.scandir(project.path + '/images') as imgs:
            for img in imgs:
                if os.path.isfile(img):
                    shutil.copy(img, 'dist/' + project.name + '/images')
                else:
                    with os.scandir(img.path) as svgs:
                        for svg in svgs:
                            shutil.copy(svg, 'dist/' + project.name + '/images/svg')
print('操作已完成，请查看 dist 文件夹下生成的站点项目')
