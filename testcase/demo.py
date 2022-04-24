#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
# @Author: will.tan
# @time: 2022/2/9 10:22

# i=int(input("请输入一个数字："))
# def func(n):
#     if(n<=1):
#         return n
#     else:
#         return func(n-1)*n
# print(func(1))
# print(type(func(1)))
# print('-'.join(str(func(i))))


# class Employee():
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#     @property
# #相当于salary属性的getter方法
#     def salary(self):
#         print("月薪为{0},年薪为{1}".format(self.__salary,(12*self.__salary)))
#         return  self.__salary
#     @salary.setter
#     def salary(self,salary):
# #相当于salary属性的setter方法
#         if (0<salary<1000000):
#             self.__salary=salary
#         else:
#             print("薪水录入错误！只能在0-1000000之间")
# emp1=Employee("高淇",100)
# print(emp1.salary)
# emp1.salary=-200
from time import sleep

from selenium.webdriver.common.by import By


class data:
    pass

da = data()

from public.models.getdriver import browser
from public.models import logger
from page.basepage import DataAssociation
from selenium.webdriver.common.keys import Keys
log = logger.Logs()
driver = browser()

def send_key(loc, vaule, clear_first=True, click_first=True):
        try:
            # loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            element = driver.find_element(*loc)
            if click_first:
                element.click()
            if clear_first:
                element.clear()
                element.send_keys(vaule)
        except AttributeError:
            log.error("%s 页面中未能找到 %s 元素" % ('-----', loc))

def scroll(driver):
    driver.execute_script(""" 
        (function () { 
            var y = document.body.scrollTop; 
            var step = 100; 
            window.scroll(0, y); 
            function f() { 
                if (y < document.body.scrollHeight) { 
                    y += step; 
                    window.scroll(0, y); 
                    setTimeout(f, 50); 
                }
                else { 
                    window.scroll(0, y); 
                    document.title += "scroll-done"; 
                } 
            } 
            setTimeout(f, 1000); 
        })(); 
        """)

driver.get("https://www.baidu.com/")
loc = (By.ID, 'kw')
send_key(loc, 'selenium')
driver.find_element(By.ID, 'su').click()
sleep(2)
# js = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# driver.execute_script("window.scrollBy(0, 500)")
# tar = driver.find_element(By.CSS_SELECTOR, 'div[id="page"] > div > a.n')
# driver.execute_script('arguments[0].scrollIntoView();', tar)
target = driver.find_element(By.XPATH, "//*[@id='2']/div/div[1]/h3/a")

driver.execute_script("arguments[0].scrollIntoView();", target)
sleep(3)

# element = driver.find_element(By.ID, 'kw')
# element.send_keys('hhhahahah')
# sleep(3)
# element.send_keys(Keys.CONTROL, 'a')
# element.send_keys(Keys.DELETE)
# element.send_keys('selenium')