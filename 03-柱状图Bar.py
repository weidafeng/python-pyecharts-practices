#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/1/2020 5:08 PM
# software:         PyCharm
# project name:     学习pyecharts 
# file name:        03-柱状图Bar
# description:      
# usage:            

# 柱状图
# //导入柱状图-Bar
from pyecharts import Bar  # 柱状/条形图，通过柱形的高度/条形的宽度来表现数据的大小。

def bar_1():
    columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

    bar = Bar("柱状图", "一年的降水量与蒸发量")

    bar.add("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
    bar.add("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])
    # 生成本地文件（默认为'render.html'文件）
    bar.render('./data/柱状图.html')

def main():
    bar_1()


if __name__ == '__main__':
    main()
