#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/1/2020 4:01 PM
# software:         PyCharm
# project name:     学习pyecharts 
# file name:        01-地图
# description:      
# usage:            

from pyecharts import Map  # 地图主要用于地理区域数据的可视化。


def world_map():
    # maptype='world' 显示世界各个国家（英文名）
    # 世界地图数据
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ["China", "Canada", "Brazil", "Russia", "United States"]

    map0 = Map(title="世界地图示例", subtitle='world map', width=1200, height=600, page_title='wdf-map')
    map0.add("世界地图", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
    map0.render(path="./data/世界地图.html")


def china_map():
    # maptype='china' 只显示全国直辖市和省级
    # 省和直辖市
    province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16,
                             '湖南': 9, '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7,
                             '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1,
                             '西藏': 1, '天津': 1, '其他': 1}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())

    map = Map("中国地图", '中国地图', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 50], maptype='china', is_visualmap=True,
            visual_text_color='#000', is_label_show=True)
    # map.show_config()
    map.render(path="./data/中国地图.html")


def henan_map():
    # 城市 -- 指定省的城市 xx市
    city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市', '信阳市', '新乡市']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

    # 河南地图  数据必须是省内放入城市名
    map2 = Map("河南地图", '河南', width=1200, height=600)
    map2.add('河南', city, values2, visual_range=[1, 10], maptype='河南', is_visualmap=True, is_label_show=True,
             visual_text_color='#000')
    # map2.show_config()
    map2.render(path="./data/河南地图.html")


def shangqiu_map():
    # 区县 -- 具体城市内的区县  xx县
    quxian = ['夏邑县', '民权县', '梁园区', '睢阳区', '柘城县', '宁陵县']
    values3 = [3, 5, 7, 8, 2, 4]

    map3 = Map('商丘地图', '商丘', title_color="#fff", title_pos="center", width=1200, height=600,
               background_color='#404a59')
    map3.add('商丘', quxian, values3, visual_range=[1, 10], maptype='商丘', is_visualmap=True, is_label_show=True,
             visual_text_color='#000')
    map3.render(path='./data/商丘地图.html')


def main():
    world_map()
    china_map()

    henan_map()
    shangqiu_map()


if __name__ == '__main__':
    main()
