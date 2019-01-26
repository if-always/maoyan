import re
import requests
import pandas as pd
from lxml import etree




headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}



movie_list = []
def maoyan_url(url):

    html = requests.get(url,headers=headers).text
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?href="(.*?)".*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        movie_dict = {}
        movie_dict['index'] = item[0]
        movie_dict['image'] = item[1]
        movie_dict['title'] = item[3]
        movie_dict['actor'] = item[4].strip()[3:]
        movie_dict['times'] = item[5].strip()[5:].split('(')[0]
        movie_dict['score'] = item[6] + item[7]
        movie_dict['url_i'] = "https://maoyan.com" + str(item[2])
        info = get_info(movie_dict['url_i'])
        movie_dict['style'] = info[0]
        movie_dict['areas'] = info[1]
        movie_dict['longt']   = info[2]
        movie_list.append(movie_dict)
        print(movie_dict)


def get_info(url):
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    style = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/text()')[0]
    area = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()')[0].split('/')[0].strip()
    longt = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()')[0].split('/')[1].strip()
    #times = html,xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')[0][0:9]
    return style,area,long_time


if __name__ == '__main__':

    urls = ['http://maoyan.com/board/4?offset={}'.format(str(i)) for i in range(0, 100, 10)]
    for url in urls:
        maoyan_url(url)

    

    index = [info['index'] for info in movie_list]
    title = [info['title'] for info in movie_list]
    image = [info['image'] for info in movie_list]
    url_i = [info['url_i'] for info in movie_list]
    score = [info['score'] for info in movie_list]
    style = [info['style'] for info in movie_list]
    times = [info['times'] for info in movie_list]
    longt = [info['longt'] for info in movie_list]
    areas = [info['areas'] for info in movie_list]
    actor = [info['actor'] for info in movie_list]


    df = pd.DataFrame({'index':index,'title':title,'image':image,'url_i':url_i,'score':score,'style':style,'times':times,'longt':longt,'areas':areas,'actor':actor})
    df = df.set_index('index')
    df.to_excel('datas.xlsx')

    for url,name in zip(image,title):

        pic = requests.get(url,headers=headers)
        f= open('picture/'+str(name)+".jpg", 'wb')#以二进制模式打开文件夹
        f.write(pic.content)
        f.close()
