import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# 批量注册子域名
# 初始化
chrome = webdriver.Chrome("chromedriver")
chrome.get("https://clients.hostwinds.com/cloud/dns-manager.php")
chrome.implicitly_wait(20)
selector1 = '#dns_manager-43576 > td:nth-child(5) > div.dropdown.open > ul > li:nth-child(1)'  # 点击跳转子路由新增页面

# 用户密码登录
chrome.find_element(By.ID, 'inputEmail').send_keys("jlacoin@protonmail.com")
chrome.find_element(By.ID, 'inputPassword').send_keys("Qaz123123123..")
chrome.find_element(By.ID, 'login').click()
# 域名注册界面跳转
chrome.implicitly_wait(20)
chrome.find_element(By.ID, 'dropdown-43576').click()
chrome.find_element(By.CSS_SELECTOR, selector1).click()
chrome.implicitly_wait(10)
# 获取 NFT Project 文件夹下所有项目文件夹名称，用于注册二级域名
with os.scandir('./NFT Project') as projects:
    for project in projects:
        chrome.implicitly_wait(20)
        chrome.find_element(By.ID, 'dns-name').clear()  # 清空输入框,追加域名名称
        chrome.find_element(By.ID, 'dns-name').send_keys(project.name.lower())
        chrome.find_element(By.ID, 'dns-value').clear()  # 清空输入框,追加域名IP
        chrome.find_element(By.ID, 'dns-value').send_keys('104.168.170.89')
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

# 开始登录宝塔上传文件
chrome.execute_script("window.open('http://104.168.170.89:8888/adcd0b00')")
chrome.implicitly_wait(20)
# 遍历标签页 -> 进入标签页 -> 如果符合查找条件则停留在该页面
for tab in chrome.window_handles:
    chrome.switch_to.window(tab)
    if 'Com面板' in chrome.title:
        break
# 用户密码登录
chrome.find_element(By.CSS_SELECTOR, 'body > div > div > div.account > form > div:nth-child(2) > input').send_keys(
    "b4vhmxao")
chrome.find_element(By.CSS_SELECTOR, 'body > div > div > div.account > form > div:nth-child(3) > input').send_keys(
    "109b2446")
chrome.find_element(By.ID, 'login-button').click()
chrome.implicitly_wait(40)

# 跳转宝塔网站域名绑定界面
chrome.find_element(By.CSS_SELECTOR, '#memuAsite > a').click()
chrome.implicitly_wait(40)
time.sleep(2)
with os.scandir('./NFT Project') as srcs:
    for project in srcs:
        # 点击添加站点
        hostName = project.name + '.solmintnft.com'
        hostName = hostName.lower()
        time.sleep(0.8)
        chrome.find_element(By.XPATH, "//button[@title='添加站点']").click()
        time.sleep(2)
        chrome.find_element(By.CLASS_NAME, 'inlineBlock').click()  # 获取焦点
        time.sleep(0.5)
        chrome.find_element(By.NAME, 'webname').send_keys(hostName)  # 输入域名
        chrome.find_element(By.CLASS_NAME, 'layui-layer-btn').click()  # 失去焦点
        chrome.find_element(By.CLASS_NAME, 'layui-layer-btn0').click()  # 确认添加
        chrome.implicitly_wait(5)
        time.sleep(3)
        # 设置 https
        chrome.find_element(By.XPATH, f"//a[@title='{hostName}']").click()
        time.sleep(0.8)
        chrome.find_element(By.XPATH, "//p[contains(text(),'SSL')]").click()
        chrome.implicitly_wait(10)
        time.sleep(2)
        chrome.find_element(By.CSS_SELECTOR, '#ssl_tabs > span:nth-child(3)').click()
        chrome.implicitly_wait(10)
        time.sleep(2)
        chrome.find_element(By.CSS_SELECTOR, '#ymlist > li > input').click()
        time.sleep(0.3)
        chrome.find_element(By.XPATH, "//button[@name='letsApply']").click()  # 确认申请
        # 持续检测是否申请成功
        # chrome.implicitly_wait(20)
        time.sleep(1)
        WebDriverWait(chrome, 120).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'关闭SSL')]")))
        time.sleep(2)
        chrome.find_element(By.CLASS_NAME, 'btswitch-btn').click()
        chrome.implicitly_wait(50)
        time.sleep(3)
        chrome.find_element(By.CLASS_NAME, 'layui-layer-close').click()

# 上传文件
chrome.find_element(By.XPATH, '//*[@id="memuAfiles"]/a').click()
chrome.implicitly_wait(40)
with os.scandir('./dist') as projects:
    for project in projects:
        hostName = project.name + '.solmintnft.com'
        hostName = hostName.lower()
        chrome.find_element(By.XPATH, f"//i[contains(text(),'{hostName}')]").click()
        chrome.implicitly_wait(5)
        time.sleep(1.5)
        chrome.find_element(By.XPATH, "//*[@id='container']/div[2]/div[2]/div[2]/div[1]/div/span").click()
        time.sleep(2)
        # chrome.find_element(By.CLASS_NAME, "upload_file_btn").click()
        chrome.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        time.sleep(0.5)
        chrome.find_element(By.XPATH, "//a[contains(text(),'上传目录')]").click()
        command = "autoSelect.exe" + " " f"{os.path.abspath(project.path)}"
        os.system(command)
        time.sleep(4.5)
        chrome.find_element(By.XPATH, "//a[contains(text(),'开始上传')]").click()
        WebDriverWait(chrome, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "ico-tips-close")))
        # chrome.find_element(By.CLASS_NAME, "layui-layer-min").click() # 最小化上传弹窗
        chrome.find_element(By.CLASS_NAME, "layui-layer-close").click()  # 关闭上传弹窗
        time.sleep(1)
        chrome.find_element(By.CLASS_NAME, "file_path_upper").click()
        time.sleep(1)
