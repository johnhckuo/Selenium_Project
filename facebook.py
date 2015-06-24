#!/usr/bin/python
# -*- coding: big5 -*-
import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
cwd = os.getcwd() + '/'
driver = webdriver.Chrome(cwd + 'chromedriver') # 啟動 chromedriver
driver.get('http://www.google.com'); # 前往 google 首頁
#time.sleep(3) # 等待5秒
search_box = driver.find_element_by_name('q') # 取得搜尋框
search_box.send_keys(u'高大資管營') # 在搜尋框內輸入 'ChromeDriver'
search_box.submit() # 令 chrome driver 按下 submit
time.sleep(1)
#driver.quit() # 關閉 chromedriver
cheese = driver.find_element_by_partial_link_text("Facebook");
cheese.click();
search_box2 = driver.find_element_by_name('email');
search_box2.send_keys('~~~~~~~~~EMAIL HERE~~~~~~~~~~~');
search_box2 = driver.find_element_by_name('pass');
search_box2.send_keys('~~~~~~~~~PASSWORD HERE~~~~~~~~~~~');
search_box2.submit();
print driver.title
cheese = driver.find_element_by_id("pagesHeaderLikeButton");
cheese.click();
cheese = driver.find_element_by_id("fbDockChatBuddylistNub");
cheese.click();

driver.get("https://www.facebook.com/johnhckuo")
body = driver.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')


cheese = driver.find_element_by_id("u_0_t");
if cheese[0] == null:
	cheese = driver.find_element_by_id("u_0_u");
cheese.click();
#driver.findElement(By.cssSelector("a[href*='messages/johnhckuo']")).click();
#cheeses = driver.find_elements_by_class_name("uiTextareaAutogrow _552m")
cheese = driver.find_elements_by_xpath("//*[@id='js_4']/div[4]/div[1]/textarea");
cheese[0].send_keys(u'哈囉你好');
cheese[0].send_keys(Keys.ENTER)
#cheese = driver.find_element_by_link_text("Hung-Chung Kuo");
#cheese.click();

#
#search_box3 = driver.find_elements_by_class_name("uiTextareaAutogrow _552m");
#search_box3.send_keys('哈囉');
#search_box3.submit();
#http://chimerhapsody.blogspot.tw/2013/06/python-selenium-chrome.html
#http://docs.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example