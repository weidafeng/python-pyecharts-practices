# pyecharts学习笔记

pyecharts是个很强大的可视化库，相比于matplotlib来说，具有强大的可交互功能，除了可以生成静态图像，还可以生成html格式图像。就像pyecharts官方文档说的，matplotlib有的，pyecharts都会有！
官方文档有中文版，十分友好，我照着运行了一遍，语法很同意、简洁、规范，效果很不错！

-  官方文档：https://05x-docs.pyecharts.org
-  官方仓库：https://github.com/pyecharts/pyecharts

## 支持图表形式
```
基本图表类
Bar（柱状图/条形图）
Bar3D（3D 柱状图）
Boxplot（箱形图）
EffectScatter（带有涟漪特效动画的散点图）
Funnel（漏斗图）
Gauge（仪表盘）
Geo（地理坐标系）
GeoLines（地理坐标系线图）
Graph（关系图）
HeatMap（热力图）
Kline/Candlestick（K线图）
Line（折线/面积图）
Line3D（3D 折线图）
Liquid（水球图）
Map（地图）
Parallel（平行坐标系）
Pie（饼图）
Polar（极坐标系）
Radar（雷达图）
Sankey（桑基图）
Scatter（散点图）
Scatter3D（3D 散点图）
Surface3D（3D 曲面图）
ThemeRiver（主题河流图）
Tree（树图）
TreeMap（矩形树图）
WordCloud（词云图）
```



```bash
安装地图

$ pip install echarts-countries-pypkg
$ pip install echarts-china-provinces-pypkg
$ pip install echarts-china-cities-pypkg
$ pip install echarts-china-counties-pypkg
$ pip install echarts-china-misc-pypkg
$ pip install echarts-united-kingdom-pypkg

全球国家地图: echarts-countries-pypkg (1.9MB): 世界地图和 213 个国家，包括中国地图
中国省级地图: echarts-china-provinces-pypkg (730KB)：23 个省，5 个自治区
中国市级地图: echarts-china-cities-pypkg (3.8MB)：370 个中国城市

```

## 绘制地图
0. 初始化地图
```python
    map0 = Map(title="世界地图示例", subtitle='world map', width=1200, height=600)
```

1. data（数据），attr（地名）
```python
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ["China", "Canada", "Brazil", "Russia", "United States"]
```
2. 地图添加属性add
```python
    map0.add("世界地图", attr, value, maptype="world", is_visualmap=True, visual_text_color='#000')
```
3. 渲染/生成地图
```python
    map0.render(path="世界地图.html")
```

```python
# add 方法参数详解
    def __add(
        self,
        name,
        attr,
        value,
        maptype="china",
        is_roam=True,
        is_map_symbol_show=True,
        name_map=None,
        **kwargs
    ):
        '''
        :param name:
            系列名称，用于 tooltip 的显示，legend 的图例筛选。
        :param attr:
            属性名称。
        :param value:
            属性所对应的值。
        :param maptype:
            地图类型。 支持 china、world、安徽、澳门、北京、重庆、福建、福建、甘肃、广东，
            广西、广州、海南、河北、黑龙江、河南、湖北、湖南、江苏、江西、吉林、辽宁、
            内蒙古、宁夏、青海、山东、上海、陕西、山西、四川、台湾、天津、香港、新疆、
            西藏、云南、浙江，以及 [363个二线城市地图](https://github.com/chfw/echarts-china-cities-js#featuring-citiesor-for-single-download)。
            提醒：
                在画市级地图的时候，城市名字后面的‘市’要省去了，比如，石家庄市的‘市’不要提，
                即‘石家庄’就可以了。地图提供了自定义模式 [用户如何自定义地图](https://github.com/chenjiandongx/pyecharts/blob/master/docs/zh-cn/user-customize-map.md)
        :param is_roam:
            是否开启鼠标缩放和平移漫游。默认为 True
            如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启。
        :param is_map_symbol_show:
            是否显示地图标记红点，默认为 True。
        :param name_map:
            用自定义的地图名称。默认为 None，也就是用地图自带地名。
        :param kwargs:
        '''
```

```
# 支持的市级地图
Cities:

安徽: 安庆, 蚌埠, 亳州, 池州, 滁州, 阜阳, 合肥, 淮北, 淮南, 黄山, 六安, 马鞍山, 宿州, 铜陵, 芜湖, 宣城
福建: 福州, 龙岩, 南平, 宁德, 莆田, 泉州, 三明, 厦门, 漳州
甘肃: 白银, 定西, 甘南藏族自治州, 嘉峪关, 金昌, 酒泉, 兰州, 临夏回族自治州, 陇南, 平凉, 庆阳, 天水, 武威, 张掖
广东: 潮州, 东莞, 东沙群岛, 佛山, 广州, 河源, 惠州, 江门, 揭阳, 茂名, 梅州, 清远, 汕头, 汕尾, 韶关, 深圳, 阳江, 云浮, 湛江, 肇庆, 中山, 珠海
广西: 百色, 北海, 崇左, 防城港, 贵港, 桂林, 河池, 贺州, 来宾, 柳州, 南宁, 钦州, 梧州, 玉林
贵州: 安顺, 毕节, 贵阳, 六盘水, 黔东南苗族侗族自治州, 黔南布依族苗族自治州, 黔西南布依族苗族自治州, 铜仁, 遵义
海南: 白沙黎族自治县, 保亭黎族苗族自治县, 昌江黎族自治县, 澄迈县, 儋州, 定安县, 东方, 海口, 乐东黎族自治县, 临高县, 陵水黎族自治县, 琼海, 琼中黎族苗族自治县, 三沙, 三亚, 屯昌县, 万宁, 文昌, 五指山
河北: 保定, 承德, 邯郸, 衡水, 廊坊, 秦皇岛, 石家庄, 唐山, 邢台, 张家口
河南: 安阳, 沧州, 鹤壁, 济源, 焦作, 开封, 洛阳, 南阳, 平顶山, 濮阳, 三门峡, 商丘, 漯河, 新乡, 信阳, 许昌, 郑州, 周口, 驻马店
黑龙江: 大庆, 大兴安岭地区, 哈尔滨, 鹤岗, 黑河, 鸡西, 佳木斯, 牡丹江, 七台河, 齐齐哈尔, 双鸭山, 绥化, 伊春
湖北: 鄂州, 恩施土家族苗族自治州, 黄冈, 黄石, 荆门, 荆州, 潜江, 神农架林区, 十堰, 随州, 天门, 武汉, 仙桃, 咸宁, 襄阳, 孝感, 宜昌
湖南: 常德, 长沙, 郴州, 衡阳, 怀化, 娄底, 邵阳, 湘潭, 湘西土家族苗族自治州, 益阳, 永州, 岳阳, 张家界, 株洲
吉林: 白城, 白山, 长春, 吉林, 辽源, 四平, 松原, 通化, 延边朝鲜族自治州
江苏: 常州, 淮安, 连云港, 南京, 南通, 苏州, 宿迁, 泰州, 无锡, 徐州, 盐城, 扬州, 镇江
江西: 抚州, 赣州, 吉安, 景德镇, 九江, 南昌, 萍乡, 上饶, 新余, 宜春, 鹰潭
辽宁: 鞍山, 本溪, 大连, 丹东, 抚顺, 阜新, 葫芦岛, 锦州, 辽阳, 盘锦, 沈阳, 铁岭, 营口, 朝阳
内蒙古: 阿拉善盟, 巴彦淖尔, 包头, 赤峰, 鄂尔多斯, 呼和浩特, 呼伦贝尔, 通辽, 乌海, 乌兰察布, 锡林郭勒盟, 兴安盟
宁夏: 固原, 石嘴山, 吴忠, 银川, 中卫
青海: 果洛藏族自治州, 海北藏族自治州, 海东, 海南藏族自治州, 海西蒙古族藏族自治州, 黄南藏族自治州, 西宁, 玉树藏族自治州
山东: 滨州, 德州, 东营, 菏泽, 济南, 济宁, 莱芜, 聊城, 临沂, 青岛, 日照, 泰安, 威海, 潍坊, 烟台, 枣庄, 淄博
山西: 长治, 大同, 晋城, 晋中, 临汾, 吕梁, 朔州, 太原, 忻州, 阳泉, 运城
陕西: 安康, 宝鸡, 汉中, 商洛, 铜川, 渭南, 西安, 咸阳, 延安, 榆林
四川: 阿坝藏族羌族自治州, 巴中, 成都, 达州, 德阳, 甘孜藏族自治州, 广安, 广元, 乐山, 凉山彝族自治州, 泸州, 眉山, 绵阳, 南充, 内江, 攀枝花, 遂宁, 雅安, 宜宾, 资阳, 自贡
西藏: 阿里地区, 昌都, 拉萨, 林芝, 那曲地区, 日喀则, 山南
新疆: 阿克苏地区, 阿拉尔, 阿勒泰地区, 巴音郭楞蒙古自治州, 北屯, 博尔塔拉蒙古自治州, 昌吉回族自治州, 哈密, 和田地区, 喀什地区, 可克达拉, 克拉玛依, 克孜勒苏柯尔克孜自治州, 昆玉, 石河子, 双河, 塔城地区, 铁门关, 图木舒克, 吐鲁番, 乌鲁木齐, 五家渠, 伊犁哈萨克自治州
云南: 保山, 楚雄彝族自治州, 大理白族自治州, 德宏傣族景颇族自治州, 迪庆藏族自治州, 红河哈尼族彝族自治州, 昆明, 丽江, 临沧, 怒江傈僳族自治州, 普洱, 曲靖, 文山壮族苗族自治州, 西双版纳傣族自治州, 玉溪, 昭通
浙江: 杭州, 湖州, 嘉兴, 金华, 丽水, 宁波, 衢州, 绍兴, 台州, 温州, 舟山
直辖市: 澳门, 北京, 重庆, 上海, 天津, 香港
```

## 使用 pyecharts-snapshot 插件
如果想直接将图片保存为 png, pdf, gif 格式的文件，可以使用 pyecharts-snapshot。使用该插件请确保你的系统上已经安装了 Nodejs 环境。

- 安装 phantomjs $ npm install -g phantomjs-prebuilt
- 安装 pyecharts-snapshot $ pip install pyecharts-snapshot
- 调用 render 方法 bar.render(path='snapshot.png') 文件结尾可以为 svg/jpeg/png/pdf/gif。请注意，svg 文件需要你在初始化 bar 的时候设置 renderer='svg'。

## 图形初始化常用配置
```
图形初始化
图表类初始化所接受的参数（所有类型的图表都一样）。

title -> str
默认 -> ""
主标题文本，支持 \n 换行。

subtitle -> str
默认 -> ""
副标题文本，支持 \n 换行。

width -> int
默认 -> 800（px）
画布宽度。

height -> int
默认 -> 400（px）
画布高度。

page_title -> str
默认 -> 'Echarts'
指定生成的 html 文件中 <title> 标签的值。

renderer -> str
默认 -> 'canvas'
指定使用渲染方式，有 'svg' 和 'canvas' 可选。3D 图仅能使用 'canvas'。

title_pos -> str/int
默认 -> 'left'
标题距离左侧距离，有'auto', 'left', 'right', 'center'可选，也可为百分比或整数

background_color -> str
默认 -> '#fff'
画布背景颜色。
```


## add 方法常用配置
地址：https://05x-docs.pyecharts.org/#/zh-cn/charts_configure

```
is_more_utils=True 指定是否提供更多的实用工具按钮。默认只提供『数据视图』和『下载』按钮
```


