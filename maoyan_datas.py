import numpy as np
import pandas as pd
from collections import Counter
from pyecharts.engine import create_default_environment
png = create_default_environment("png")

df = pd.read_excel('datas.xlsx',index_col='index')
file = df.copy()

file['longt'] = file['longt'].str.strip('分钟').astype('int64')   #.str  因为类型是seris  所以要转为str
file['years'] = file['times'].str.split('-').str[0]
file['month'] = file['times'].str.split('-').str[1]
file['month'] = file['month'].fillna("07")       #设置缺省值
#file['actor'] = file['actor'].str.split(',')
#print(file.columns)

str = ''

for x in range(100):
	str = str + ',' + file.iloc[x]['style']
types = str.split(',')


types = Counter(types)
most_types = types.most_common(10)

print(most_types)

attr = [ x[0] for x in most_types]
value = [ x[1] for x in most_types]

from pyecharts import Pie

pie = Pie("电影类型", title_pos='right')
pie.add(
    "",
    attr,
    value,
    radius=[40, 75],
    label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",
)

png.render_chart_to_file(pie,path = 'result/picture/type.png')

#@@@@@@@@@@@@@@@@@@@@@@@@@@
# str_1 = ''
# for i in range(100):
#     str_1 = str_1 + ',' + file.iloc[i]['actor']

# actor_name = str_1.split(',')
# name = Counter(actor_name)
# most_name = name.most_common(20)


# from pyecharts import WordCloud

# attr = [ x[0] for x in most_name]
# value = [ x[1] for x in most_name]
# wordcloud = WordCloud(width=1300, height=620)
# wordcloud.add("", attr, value, word_size_range=[20, 100])

# png.render_chart_to_file(wordcloud,path='result/picture/name.png')
# print(attr,value)
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# year_count = file.groupby('years')['month'].count()
# print(year_count)


# from pyecharts import Bar,Line,Overlap

# attr = list(year_count.index)
# v1 = list(year_count)
# bar = Bar("电影年份分布")
# bar.add("", attr, v1,mark_line=["average"],mark_point=['max','min'])

# line = Line()
# line.add("",attr,v1)

# overlap = Overlap()
# overlap.add(bar)
# overlap.add(line)

# png.render_chart_to_file(overlap,path='result/picture/years.png')
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def get_country(data):
   
# 	datas_2 = []
# 	datas_1 = data.split(',')
# 	for x in datas_1:
# 		if '中国香港' in x:
# 			x = '中国'
# 			datas_2.append(x)
# 		elif '中国台湾' in x:
# 			x = '中国'
# 			datas_2.append(x)
# 		elif '中国大陆' in x:
# 			x = '中国'
# 			datas_2.append(x)
# 		else:
# 			datas_2.append(x)

# 	datas_country.extend(datas_2)


# datas_country = []
# file['areas'].map(get_country)
# c = Counter(datas_country)
# countrys = c.most_common(7)
# v = []
# attr = []
# for i in countrys:
#     v.append(i[1])
#     attr.append(i[0])
# print(v,attr)


# from pyecharts import Pie
# pie = Pie("电影产地统计", title_pos='left', width=900)
# pie.add(
#     "",
#     attr,
#     v,
#     is_label_show=True
# )
# png.render_chart_to_file(pie, path='result/picture/areas.png')
# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@