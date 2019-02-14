from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.get('https://mail.yahoo.com/d/folders/2')
# print(browser.page_source)
# browser.close()
input = browser.find_element_by_id('login-username')#找到搜索框
input.send_keys('ketterere76@yahoo.com')
button = browser.find_element_by_id('login-signin')#找到搜索按钮
button.click()
# print(browser.page_source)
browser.implicitly_wait(10)
browser.switch_to_window(browser.window_handles[-1])
input = browser.find_element_by_id('login-passwd')#找到搜索框
input.send_keys('ssj9564**')
button = browser.find_element_by_id('login-signin')#找到搜索按钮
button.click()
browser.implicitly_wait(10)
browser.switch_to_window(browser.window_handles[-1])
# a = input('里面有几封已发邮件：')
# if not isinstance(a,int):
#     a = int()

n = 0
while True:
    try:
        if n > 0:
            browser.refresh()
        # time_0 = browser.find_element_by_xpath("//div[@draggable='true'][%s]//span[@role='gridcell'][%s]/span" %(int(a)+2,int(a)))
        # time_1 = time_0.text
        while True:
            elements = browser.find_elements_by_xpath("//ul[@aria-readonly='true']/li")
            a = len(elements)
            # print(a - 1)
            while True:
                # print(browser.current_url)
                if browser.current_url.split('/')[5][0] == '2':
                    elements = browser.find_elements_by_xpath("//ul[@aria-readonly='true']/li")
                    b = len(elements)
                    # print(b - 1)
                    if a == b:
                        browser.refresh()
                        continue
                    elif a > b:
                        a = b
                        browser.refresh()
                        continue
                    else:
                        break
                else:
                    button = browser.find_element_by_xpath("//div[@data-test-folder-container='Sent']/a")
                    button.click()
                    continue
            break

        # input = WebDriverWait(browser, 24*60*60, 0.5).until(EC.presence_of_element_located((By.XPATH, "//ul[@aria-readonly='true']/li[%s]" %(a+1))))

        # elements = browser.find_elements_by_xpath("//ul[@aria-readonly='true']/li")
        # b = len(elements)
        # print(b - 1)

        button = browser.find_element_by_xpath("//ul[@aria-readonly='true']/li[2]//a[@role='row']")
        button.click()
        # link_0 = button.get_attribute('href')
        # link_1 = 'https://mail.yahoo.com' + link_0
        content = browser.find_element_by_xpath("//div[@data-test-id='message-view-body']")
        print(content.text)
        with open('content.txt','a+',encoding='utf8') as f:
            f.write(content.text)
            f.write('\n\n')
        browser.back()
        n += 1
    except Exception as e:
        pass




