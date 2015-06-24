#!/usr/bin/python
# -*- coding: utf-8 -*-
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
	
	

	search = sys.argv[1]  #因為Python編碼問題，這邊中文輸入可能會有問題，必要時請註解此行並用下一行的code
	#search = u'高雄'
	start = timeit.default_timer()
	print search
			
	jsfile= "window.onload = function () {var chart2 = new CanvasJS.Chart('second_chart',{title:{text: 'Kaohsiung Monthly Temperature'}, animationEnabled: true,   axisY :{minimum :15, maximum: 40,suffix: 'C',interval: 1,labelFontSize: 20},axisX: {title: 'Monthly Temperature',interval:1,labelAngle: -60},  data: [ {        type: 'splineArea',showInLegend: true,color: 'rgba(255,0,255,.7)',name: 'Kaohsiung',dataPoints: [";
      
	f = open('all3.js','a')
	f.write(jsfile) # python will convert \n to os.linesep
	i = 0;
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
			result = driver.find_elements_by_tag_name("td")
			#result = str(result[6].text)
			print len(result)
			while i<len(result):
				print result[i].text
				if result[i].text == search :
					
					break;
				i=i+1
			str_result = result[i+1].get_attribute('innerHTML');

			
			f = open('all3.js','a')
			f.write('{x:new Date('+str(year)+','+str(month-1)+',1),y:'+str(str_result)+'},') # python will convert \n to os.linesep
			 # you can omit in most cases as the destructor will call if
			
			month = month +1;
			driver.get(url+str(year)+str(month)+'.htm')	
			body = driver.find_element_by_tag_name("body")
			body.send_keys(Keys.CONTROL + 't')
			stop = timeit.default_timer()
			print "Total Time Spent"+str(stop - start)+"second"; 
		year = year +1;
		
	
	f.write("]}]});chart2.render();}") # python will convert \n to os.linesep
	f.close()
	driver.get('D:/Open Data/file3.html')	
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