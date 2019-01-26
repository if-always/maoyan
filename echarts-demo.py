import numpy as np
import pandas as pd
from pyecharts import Pie,Bar,Style
from collections import Counter


df = pd.read_excel('data2.xlsx',index_col='names')
file = df.copy()

file = file[~file['longt'].str.contains('None')]
file['longt'] = file['longt'].str.strip('分钟').astype('int64')
file['years'] = file['times'].str.split('-').str[0]
file['month'] = file['times'].str.split('-').str[1]
file['dayss'] = file['times'].str.split('-').str[2]
file['datas'] = file['month'] +'.'+ file['dayss'] 
Clean = file['areas'].fillna('未知')
file['areas'] = Clean



def Bars():

	def cut(value):

		values = value.split(',')
		if len(values) > 1:
			value = values[np.random.randint(1,len(values))]
			if '中国' in value:
				return '中国'
			else:
				return value
		else:
			if '中国' in values[0]:
				return '中国'
			else:
				return values[0]
	attr = file.areas.apply(cut).value_counts().index.tolist()[0:7]
	valu = file.areas.apply(cut).value_counts().tolist()[0:7]
	print(len(attr))
	print(len(valu))
	style = Style(
		title_pos = 'left',
		width = 900,
		height = 500,
		background_color = 'white',)
	bar_style = style.add(
		legend_pos = 'bottom',
		label_color = ['yellow'],
		label_text_color ='blue',
		is_label_show=None,#显示图例  数据
		mark_point=['max','min'],
		mark_line=['average'])
	bar = Bar("地区分布:","",**style.init_style)#标题和副标题
	bar.add("",attr,valu,**bar_style)
	#is_convert = True 换x y轴
	bar.render('./Echarts/bar.html')
#Bars()
#

def Pies_1():
	def cut(value):

		values = value.split(',')
		return values[0]

	datas = file['types'].apply(cut)
	attr = datas.value_counts().index.tolist()[0:9]
	valu = datas.value_counts().tolist()[0:9]
	style = Style(
		title_pos = 'center',
		title_top = 'bottom',
		width = 900,
		height = 500,
		background_color = 'white')
	pie_style = style.add(
		legend_pos = 'center',
		radius=[40, 75],
		label_color = [],
		label_text_color ='',
		#legend_orient="vertical",
		is_label_show=True,#显示图例  数据
		)

	pie = Pie("","",**style.init_style)
	pie.add("",attr,valu,**pie_style)
	pie.render('./Echarts/pie.html')


Pies_1()

def Pie_2():#环形
	
	def cut(value):

		values = value.split(',')
		return values[0]

	datas = file['types'].apply(cut)
	attr = datas.value_counts().index.tolist()[0:9]
	valu = datas.value_counts().tolist()[0:9]

	pie = Pie("", title_pos='center')
	pie.add(
	    "",
	    attr,
	    valu,
	    radius=[40, 75],
	    label_text_color='',
	    is_label_show=True,
	    legend_orient="vertical",  #图例的方向
	    legend_pos="left",         #图例的位置
	)
	pie.render('./Echarts/pie.html')