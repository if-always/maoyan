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

def cut_1(value):

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
file['areas'] = file.areas.apply(cut_1)
def cut_2(value):

		values = value.split(',')
		return values[0]

file['types'] = file['types'].apply(cut_2)
def Bars():

	
	attr = file.areas.value_counts().index.tolist()[0:7]
	valu = file.areas.value_counts().tolist()[0:7]
	style = Style(
		title_pos = 'left',
		width = 1200,
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
Bars()


def Bar_x_y():

	attr_1 = file.areas.value_counts().index.tolist()[0:7]
	attr_2 = file.types.value_counts().index.tolist()[0:3]
	datas = file[(file.areas.isin(attr_1)) & (file.types.isin(attr_2))]
	data = datas.groupby(['areas','types']).agg({'score':'mean'})
	data.score = data.score.round(decimals=1)
	list_1 = []
	list_2 = []
	list_3 = []
	attr = attr_1
	#print(city)

	#print(data.score.tolist())
	for i in range(0,7):
		list_1.append(data.score.tolist()[0+3*i])
		list_2.append(data.score.tolist()[1+3*i])
		list_3.append(data.score.tolist()[2+3*i])
	style = Style(
		title_pos='center',
		width=800,
		height=500,
		background_color='white',
		)
	bar_style=style.add(
		legend_top='bottom',
		yaxis_rotate=45,
		is_label_show=None,
		label_color=['#FFB90F','#FFF68F','#1E90FF'],
		)
	#print(city)
	print(list_1)
	bar=Bar('',**style.init_style)
	bar.add('剧情',attr,list_1,is_stack=True,**bar_style)#is_stack=True堆叠
	bar.add('喜剧',attr,list_2,is_stack=True,**bar_style)
	bar.add('动作',attr,list_3,is_stack=True,**bar_style)
	bar.render('Echarts/bar_x_y.html')
	
#Bar_x_y()

def Pies_1():
	

	attr = file.types.value_counts().index.tolist()[0:9]
	valu = file.types.value_counts().tolist()[0:9]
	style = Style(
		title_pos = 'center',
		title_top = 'bottom',
		width = 900,
		height = 500,
		background_color = 'white')
	pie_style = style.add(
		legend_pos = 'center',
		#radius=[40, 75],  #饼图还是环形兔
		label_color = [],
		label_text_color ='',
		#legend_orient="vertical",
		is_label_show=True,#显示图例  数据
		)

	pie = Pie("","",**style.init_style)
	pie.add("",attr,valu,**pie_style)
	pie.render('./Echarts/pie.html')


#Pies_1()

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
	    radius=[30, 75],
	    label_text_color='',
	    is_label_show=True,
	    legend_orient="",  #图例的方向  vertical  垂直
	    legend_pos="",         #图例的位置
	    rosetype='area',
	)
	pie.render('./Echarts/pie.html')
#Pie_2()


def Rose():

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
	    radius=[30, 75],
	    label_text_color='',
	    is_label_show=True,
	    legend_orient="",  #图例的方向  vertical  垂直
	    legend_pos="",         #图例的位置
	    rosetype='area',
	)
	pie.render('./Echarts/rose.html')
#Rose()


def Line():
	datas = file['years']
	print(datas)


	pass
Line()