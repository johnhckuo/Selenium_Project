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
import sys

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
	
	


	start = timeit.default_timer()
	
			
	jsfile= "window.onload = function () {var chart2 = new CanvasJS.Chart('second_chart',{title:{text: '阿里山每月氣溫'}, animationEnabled: true,   axisY :{maximum: 20,suffix: '℃',interval: 1,labelFontSize: 20},axisX: {title: '歷月氣溫',interval:1,labelAngle: -60},  data: [ {        type: 'splineArea',showInLegend: true,color: 'rgba(255,0,255,.7)',name: '阿里山氣溫',dataPoints: [";
      
	f = open('all.js','a')
	f.write(jsfile) # python will convert \n to os.linesep
	
	while year < 2010:
		month = 1;
	#    print "Value is: " + option.get_attribute("value")
		if year == 2006:
			cwd = os.getcwd() + '/'
			driver = webdriver.Chrome(cwd + 'chromedriver') # 啟動 chromedriver
			driver.get(url+str(year)+str(month)+'.htm'); 
		else:
			driver.get(url+str(year)+str(month)+'.htm')	
			body = driver.find_element_by_tag_name("body")		
			body.send_keys(Keys.CONTROL + 't')
	
		
		while month < 12:
			result = driver.find_elements_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]")
			str_result = result[0].get_attribute('innerHTML');
			
			
			f = open('all.js','a')
			f.write('{x:new Date('+str(year)+','+str(month-1)+',1),y:'+str(str_result)+'},') # python will convert \n to os.linesep
			 # you can omit in most cases as the destructor will call if
			
			month = month +1;
			driver.get(url+str(year)+str(month)+'.htm')	
			body = driver.find_element_by_tag_name("body")
			body.send_keys(Keys.CONTROL + 't')
			stop = timeit.default_timer()
			print "目前共費時"+str(stop - start)+"秒"; 
		year = year +1;
		
	
	f.write("]}]});chart2.render();}") # python will convert \n to os.linesep
	f.close()
	driver.get('D:/Open Data/file.html')	
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