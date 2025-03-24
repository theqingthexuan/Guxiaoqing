
from pyecharts import options as opts
from pyecharts.charts import Bar
# 内置主题
from pyecharts.globals import ThemeType

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10, 20, 15, 25, 30]

# 创建柱状图
bar_chart = Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))  # 切换到暗色系主题
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxis("销售额", y_data)

# 配置图表
bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title='月度销售额柱状图'),
    xaxis_opts=opts.AxisOpts(name='月份'),
    yaxis_opts=opts.AxisOpts(name='销售额（万元）'),
)

# 渲染图表
bar_chart.render("bar_chart.html")

# 配置全局属性
bar_chart.set_global_opts(
    title_opts=opts.TitleOpts(title='月度销售额柱状图', subtitle='副标题'),
    xaxis_opts=opts.AxisOpts(name='月份'),
    yaxis_opts=opts.AxisOpts(name='销售额（万元）'),
    legend_opts=opts.LegendOpts(pos_left='center', pos_top='top'),
    toolbox_opts=opts.ToolboxOpts(),
    tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type="cross"),
)

bar_chart.render("bar_chart.html")
"""
可以设置的主题
class _ThemeType:
    BUILIN_THEME = ["light", "dark", "white"]
    LIGHT = "light"
    DARK = "dark"
    WHITE = "white"
    CHALK: str = "chalk"
    ESSOS: str = "essos"
    INFOGRAPHIC: str = "infographic"
    MACARONS: str = "macarons"
    PURPLE_PASSED: str = "purple_passed"
    ROMAN: str = "roma"
    BOMANTIC: str = "bomantic"
    SHINE: str = "shine"
    VINTAGE: str = "vintage"
    WALDEN: str = "walden"
    WESTEROS: str = "westeros"
    WONDERLAND: str = "wonderland"
    HALLOWEEN: str = "halloween"
"""

from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.faker import Faker

attr = Faker.choose()
tl = Timeline()
for i in range(2010, 2024):
    pie = (
        Pie()
        .add(
            "商家A",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
    )
    tl.add(pie, "{}年".format(i))
tl.render("timeline_pie.html")

from pyecharts.charts import Geo
import os

data = [
    ("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15),
    ("赤峰", 16), ("青岛", 18), ("乳山", 18), ("金昌", 19), ("泉州", 21), ("莱西", 21),
    ("日照", 21), ("胶南", 22), ("南通", 23), ("拉萨", 24), ("云浮", 24), ("梅州", 25),
    ("文登", 25), ("上海", 25), ("攀枝花", 25), ("威海", 25), ("承德", 25), ("厦门", 26),
    ("汕尾", 26), ("潮州", 26), ("丹东", 27), ("太仓", 27), ("曲靖", 27), ("烟台", 28),
    ("福州", 29), ("瓦房店", 30), ("即墨", 30), ("抚顺", 31), ("玉溪", 31), ("张家口", 31),
    ("阳泉", 31), ("莱州", 32), ("湖州", 32), ("汕头", 32), ("昆山", 33), ("宁波", 33),
    ("湛江", 33), ("揭阳", 34), ("荣成", 34), ("连云港", 35), ("葫芦岛", 35), ("常熟", 36),
    ("东莞", 36), ("河源", 36), ("淮安", 36), ("泰州", 36), ("南宁", 37), ("营口", 37),
    ("惠州", 37), ("江阴", 37), ("蓬莱", 37), ("韶关", 38), ("嘉峪关", 38), ("广州", 38),
    ("延安", 38), ("太原", 39), ("清远", 39), ("中山", 39), ("昆明", 39), ("寿光", 40),
    ("盘锦", 40), ("长治", 41), ("深圳", 41), ("珠海", 42), ("宿迁", 43), ("咸阳", 43),
    ("铜川", 44), ("平度", 44), ("佛山", 44), ("海口", 44), ("江门", 45), ("章丘", 45),
    ("肇庆", 46), ("大连", 47), ("临汾", 47), ("吴江", 47), ("石嘴山", 49), ("沈阳", 50),
    ("苏州", 50), ("茂名", 50), ("嘉兴", 51), ("长春", 51), ("胶州", 52), ("银川", 52),
    ("张家港", 52), ("三门峡", 53), ("锦州", 54), ("南昌", 54), ("柳州", 54), ("三亚", 54),
    ("自贡", 56), ("吉林", 56), ("阳江", 57), ("泸州", 57), ("西宁", 57), ("宜宾", 58),
    ("呼和浩特", 58), ("成都", 58), ("大同", 58), ("镇江", 59), ("桂林", 59), ("张家界", 59),
    ("宜兴", 59), ("北海", 60), ("西安", 61), ("金坛", 62), ("东营", 62), ("牡丹江", 63),
    ("遵义", 63), ("绍兴", 63), ("扬州", 64), ("常州", 64), ("潍坊", 65), ("重庆", 66),
    ("台州", 67), ("南京", 67), ("滨州", 70), ("贵阳", 71), ("无锡", 71), ("本溪", 71),
    ("克拉玛依", 72), ("渭南", 72), ("马鞍山", 72), ("宝鸡", 72), ("焦作", 75), ("句容", 75),
    ("北京", 79), ("徐州", 79), ("衡水", 80), ("包头", 80), ("绵阳", 80), ("乌鲁木齐", 84),
    ("枣庄", 84), ("杭州", 84), ("淄博", 85), ("鞍山", 86), ("溧阳", 86), ("库尔勒", 86),
    ("安阳", 90), ("开封", 90), ("济南", 92), ("德阳", 93), ("温州", 95), ("九江", 96),
    ("邯郸", 98), ("临安", 99), ("兰州", 99), ("沧州", 100), ("临沂", 103), ("南充", 104),
    ("天津", 105), ("富阳", 106), ("泰安", 112), ("诸暨", 112), ("郑州", 113), ("哈尔滨", 114),
    ("聊城", 116), ("芜湖", 117), ("唐山", 119), ("平顶山", 119), ("邢台", 119), ("德州", 120),
    ("济宁", 120), ("荆州", 127), ("宜昌", 130), ("义乌", 132), ("丽水", 133), ("洛阳", 134),
    ("秦皇岛", 136), ("株洲", 143), ("石家庄", 147), ("莱芜", 148), ("常德", 152), ("保定", 153),
    ("湘潭", 154), ("金华", 157), ("岳阳", 169), ("长沙", 175), ("衢州", 177), ("廊坊", 193),
    ("菏泽", 194), ("合肥", 229), ("武汉", 273), ("大庆", 279)]

geo = Geo(init_opts=opts.InitOpts(width='1200px', height='600px', bg_color='#404a59'))
geo.add_schema(maptype='china',
               itemstyle_opts=opts.ItemStyleOpts(color="#28527a",  # 背景颜色
                                                 border_color="#9ba4b4"))
geo.add("", data, symbol_size=15, label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(
    title_opts=opts.TitleOpts(pos_left='center', title="全国主要城市空气质量", subtitle="data from pm2.5",
                              title_textstyle_opts=opts.TextStyleOpts(color='#fff')),
    visualmap_opts=opts.VisualMapOpts(range_size=[0, 200],
                                      textstyle_opts=opts.TextStyleOpts(color='#fff')))
geo.render()
os.system("render.html")

from pyecharts.charts import Geo
import os

geo = Geo(init_opts=opts.InitOpts(width='1200px', height='600px', bg_color='#404a59'))
geo.add_schema(maptype='china',
               itemstyle_opts=opts.ItemStyleOpts(color="#28527a",  # 背景颜色
                                                 border_color="#9ba4b4"))
geo.add("", data, symbol_size=15, label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(title_opts=opts.TitleOpts(pos_left='center', title="全国主要空气质量", subtitle="data from pm2.5",
                                              title_textstyle_opts=opts.TextStyleOpts(color='#fff')),
                    visualmap_opts=opts.VisualMapOpts(range_size=[0, 200],
                                                      textstyle_opts=opts.TextStyleOpts(color='#fff')))
geo.render()
os.system("空气质量图.html")

