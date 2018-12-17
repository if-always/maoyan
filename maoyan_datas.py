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


def get_country(data):
   
	datas_2 = []
	datas_1 = data.split(',')
	for x in datas_1:
		if '中国香港' in x:
			x = '中国'
			datas_2.append(x)
		elif '中国台湾' in x:
			x = '中国'
			datas_2.append(x)
		elif '中国大陆' in x:
			x = '中国'
			datas_2.append(x)
		else:
			datas_2.append(x)

	datas_country.extend(datas_2)


datas_country = []
file['areas'].map(get_country)
c = Counter(datas_country)
countrys = c.most_common(7)
v = []
attr = []
for i in countrys:
    v.append(i[1])
    attr.append(i[0])
print(v,attr)


from pyecharts import Pie
pie = Pie("国家统计", title_pos='left', width=900)
pie.add(
    "",
    attr,
    v,
    is_label_show=True
)
png.render_chart_to_file(pie, path='421.png')