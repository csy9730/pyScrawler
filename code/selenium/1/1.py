from selenium import webdriver
import os,sys
os.environ['PATH'] +=';../;'
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')


