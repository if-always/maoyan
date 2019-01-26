#https://maoyan.com/films?showType=3&sortId=3&offset=30
#
import re
import requests
import pandas as pd
from lxml import etree




headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}



movie_list = [[],[],[],[],[],[],[]]
def maoyan_url(url):

    html = requests.get(url,headers=headers).text
    infos = etree.HTML(html).xpath('//div[@class="movies-list"]/dl/dd')

    for info in infos:
    	
    	href = info.xpath('.//div[@class="movie-item"]/a/@href')
    	hrefs = ["https://maoyan.com" + url for url in href]
    	names = info.xpath('.//div[@class="channel-detail movie-item-title"]/a/text()')
    	picus = info.xpath('.//div[@class="movie-item"]/a/div[@class="movie-poster"]/img[2]/@data-src')
    	scor1 = info.xpath('.//div[@class="channel-detail channel-detail-orange"]/i[1]/text()')
    	scor2 = info.xpath('.//div[@class="channel-detail channel-detail-orange"]/i[2]/text()')
    	score = [i + j for i,j in zip(scor1,scor2)]
    	longt = []
    	types = []
    	areas = []
    	times = []
    	for href in hrefs:
    		#print(href)
    		datas = get_info(href)
    		print(datas)
    		types.append(datas[0])
    		areas.append(datas[1])
    		longt.append(datas[2])
    		times.append(datas[3])
    	#df = pd.DataFrame({'names':names,'image':hrefs,'score':score,'areas':areas,'longt':longt,'types':types,'times':times})
    	#df = df.set_index('names')
    	#df.to_excel('data2.xlsx')
    	movie_list[0].extend(names)
    	movie_list[1].extend(hrefs)
    	movie_list[2].extend(score)
    	movie_list[3].extend(longt)
    	movie_list[4].extend(times)
    	movie_list[5].extend(areas)
    	movie_list[6].extend(types)

def get_info(url):
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    try:
	    style = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/text()')[0]
	    area = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()')[0].split('/')[0].strip()
	    long_time = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()')[0].split('/')[1].strip()
	    times = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')[0][0:10]
	    return style,area,long_time,times
    except:
    	style = 'None',
    	area  = 'None',
    	long_time = 'None',
    	times = 'None'
    	return style,area,long_time,times
#maoyan_url("https://maoyan.com/films?showType=3&sortId=3&offset=0")
#
if __name__ == '__main__':

    urls = ['https://maoyan.com/films?showType=3&sortId=3&offset={}'.format(str(i)) for i in range(0,1500, 30)]
    #print(len(urls))
    num = 0
    for url in urls:
    	print('******page:{}'.format(num))
    	num = num + 1 
    	maoyan_url(url)
    df = pd.DataFrame({'names':movie_list[0],'image':movie_list[1],'score':movie_list[2],'areas':movie_list[5],'longt':movie_list[3],'types':movie_list[6],'times':movie_list[4]})
    df = df.set_index('names')
    df.to_excel('data2.xlsx')