# -*- coding: UTF-8 -*-

# Python 程序用于检测用户输入的数字是否为质数

# 用户输入数字
number = int(input('请输入一个数字：'))

# 质数大于 1
if number > 1:
    #查看因子
    for i in  range(2, number):
        if number % i == 0:
            print(number, '不是质数')
            print(i,'乘于', number / i,'是', number)
            break
    else:
        print(number, '是质数')
# 如果输入的数字小于等于1，不是质数
else:
    print(number, '不是质数')


