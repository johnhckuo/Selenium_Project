#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timeit

def find(driver):
    element = driver.find_element_by_id("cphMain_btnQuery")
    if element:
		print element.id
		return element
    else:
        return False

def main():
	url = 'http://www.cwb.gov.tw/V7/climate/monthlyData/Data/mD'
	year = 2006;
	month = 1;
	
	#time.sleep(3) # 等待5秒

	start = timeit.default_timer()
	
	while year < 2010:
	#    print "Value is: " + option.get_attribute("value")
		
	
		if year == 2006:
			cwd = os.getcwd() + '/'
			driver = webdriver.Chrome(cwd + 'chromedriver') # 啟動 chromedriver
			
			str_tear = str(year)
			str_month = str(month)
			driver.get(url+str_tear+str_month+'.htm'); 
			
		
		
		
		while month < 12:
			month = month +1;
				
			result = driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]")

			str_result = result[0].get_attribute('innerHTML');
			f = open('file2.html','a')
			f.write('<div>'+str_result+'</div>') # python will convert \n to os.linesep
			 # you can omit in most cases as the destructor will call if
			driver.get(url+str(year)+str(month)+'.htm')	
			body = driver.find_element_by_tag_name("body")
			
			body.send_keys(Keys.CONTROL + 't')
			stop = timeit.default_timer()
			print "目前共費時"+str(stop - start)+"秒"; 
		
		month = 1;
		year = year +1;
		driver.get(url+str(year)+str(month)+'.htm')	
		body = driver.find_element_by_tag_name("body")
			
		body.send_keys(Keys.CONTROL + 't')
	

	driver.get('D:/Open Data/file2.html')	
	body = driver.find_element_by_tag_name("body")	
	body.send_keys(Keys.CONTROL + 't')
#############################################################################
 
if __name__ == "__main__":
    main()


#cheese = driver.find_element_by_link_text("Hung-Chung Kuo");
#cheese.click();

#
#search_box3 = driver.find_elements_by_class_name("uiTextareaAutogrow _552m");
#search_box3.send_keys('哈囉');
#search_box3.submit();
#http://chimerhapsody.blogspot.tw/2013/06/python-selenium-chrome.html
#http://docs.seleniumhq.org/docs/03_webdriver.jsp#introducing-the-selenium-webdriver-api-by-example