#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         2/1/2020 4:36 PM
# software:         PyCharm
# project name:     学习pyecharts 
# file name:        02-地图Geo
# description:      
# usage:            

from pyecharts import Geo  # 地理坐标系组件用于地图的绘制，支持在地理坐标系上绘制散点图，线集。


def heat_map():
    data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15),
            ("赤峰", 16), ("青岛", 18), ("乳山", 18), ("金昌", 19), ("泉州", 21), ("莱西", 21),
            ("日照", 21), ("胶南", 22), ("南通", 23), ("拉萨", 24), ("云浮", 24), ("梅州", 25), ("乌鲁木齐", 40)]

    geo = Geo("全国主要城市空气质量热力图", "data from pm2.5", title_color="#fff", title_pos="center",
              width=1200, height=600, background_color='#404a59')
    attr, value = geo.cast(data)

    geo.add("空气质量热力图", attr, value, visual_range=[0, max(value)], type='heatmap',
            visual_text_color="#fff", symbol_size=15, is_label_show=True, is_visualmap=True)
    # geo.show_config()

    geo.render(path="./data/空气质量热力图.html")


def heat_map_with_effects():
    # 空气质量评分（带水波特效）
    indexs = ['上海', '北京', '合肥', '哈尔滨', '广州', '成都', '无锡', '杭州', '武汉', '深圳', '西安', '郑州', '重庆', '长沙']
    values = [4.07, 1.85, 4.38, 2.21, 3.53, 4.37, 1.38, 4.29, 4.1, 1.31, 3.92, 4.47, 2.40, 3.60]

    geo = Geo("全国主要城市空气质量评分", "data from pm2.5", title_color="#fff", title_pos="center",
              width=1200, height=600, background_color='#404a59')
    # 图例类型，有'scatter', 'effectscatter', 'heatmap'可选。
    # type="effectScatter", is_random=True, effect_scale=5  随机排列颜色列表，使点具有发散性
    geo.add("空气质量评分", indexs, values, type="effectScatter", is_random=True, effect_scale=5, visual_range=[0, 5],
            visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
    # geo.show_config()
    geo.render(path="./data/空气质量评分.html")

def heat_map_with_scatter():
    # 空气质量评分
    indexs = ['上海', '北京', '合肥', '哈尔滨', '广州', '成都', '无锡', '杭州', '武汉', '深圳', '西安', '郑州', '重庆', '长沙']
    values = [4.07, 1.85, 4.38, 2.21, 3.53, 4.37, 1.38, 4.29, 4.1, 1.31, 3.92, 4.47, 2.40, 3.60]

    geo = Geo("全国主要城市空气质量评分", "data from pm2.5", title_color="#fff", title_pos="center",
              width=1200, height=600, background_color='#404a59')
    # 图例类型，有'scatter', 'effectscatter', 'heatmap'可选。
    # type="effectScatter", is_random=True, effect_scale=5  使点具有发散性
    geo.add("空气质量评分", indexs, values, type="scatter", is_random=True, effect_scale=5, visual_range=[0, 5],
            visual_text_color="#fff", symbol_size=15, is_visualmap=True, is_roam=False)
    # geo.show_config()
    geo.render(path="./data/空气质量评分-scatter.html")



def main():
    heat_map()
    heat_map_with_effects()
    heat_map_with_scatter()


if __name__ == '__main__':
    main()
