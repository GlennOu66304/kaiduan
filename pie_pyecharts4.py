from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType

# 上面的包自己安装，不会的就百度

f = open('content.txt', 'r', encoding='utf-8')  # 这是数据源，也就是想生成词云的数据
words = f.read()  # 读取文件
f.close()  # 关闭文件，其实用with就好，但是懒得改了

name=["白敬亭","赵今麦","刘奕君","刘涛","黄觉","刘丹"]

print(name)
count=[float(words.count("白敬亭")),
      float(words.count("赵今麦")),
      float(words.count("刘奕君")),
    float(words.count("刘涛")),
    float(words.count("黄觉")),
    float(words.count("刘丹"))]
print(count)

num = count
lab = name
(
    Pie(init_opts=opts.InitOpts(width='1650px',height='450px',theme=ThemeType.LIGHT))#默认900，600
    .set_global_opts(
        title_opts=opts.TitleOpts(title="开端主演提及占比",
                                               title_textstyle_opts=opts.TextStyleOpts(font_size=27)),legend_opts=opts.LegendOpts(

            pos_top="3%", pos_left="33%",# 图例位置调整
            ),)
    .add(series_name='',center=[280, 270], data_pair=[(j, i) for i, j in zip(num, lab)])#饼图
   .add(series_name='',center=[800, 270],data_pair=[(j,i) for i,j in zip(num,lab)],radius=['40%','75%'])#环图
    .add(series_name='', center=[1300, 270],data_pair=[(j, i) for i, j in zip(num, lab)], rosetype='radius')#南丁格尔图
).render('pie_pyecharts4.html')