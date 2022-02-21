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


class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    @property
#相当于salary属性的getter方法
    def salary(self):
        print("月薪为{0},年薪为{1}".format(self.__salary,(12*self.__salary)))
        return  self.__salary
    @salary.setter
    def salary(self,salary):
#相当于salary属性的setter方法
        if (0<salary<1000000):
            self.__salary=salary
        else:
            print("薪水录入错误！只能在0-1000000之间")
emp1=Employee("高淇",100)
print(emp1.salary)
emp1.salary=-200