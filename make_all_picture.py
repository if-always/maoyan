import os
from PIL import Image

width_i = 300
height_i = 300

#每行每列显示图片数量
line_max = 10
row_max = 10

#参数初始化
all_path = []
num = 0
pic_max=line_max*row_max
dirName = os.getcwd()


for root, dirs, files in os.walk(dirName):
        for file in files:
            if "jpg" in file:
                    all_path.append(os.path.join(root,file))


toImage = Image.new('RGBA',(width_i*line_max,height_i*row_max))


for i in range(0,row_max): 

    for j in range(0,line_max):

        pic_fole_head =  Image.open(all_path[num])
        width,height =  pic_fole_head.size
    
        tmppic = pic_fole_head.resize((width_i,height_i))
    
        loc = (int(i%line_max*width_i),int(j%line_max*height_i))
    
        #print("第" + str(num) + "存放位置" + str(loc))
        toImage.paste(tmppic,loc)
        num = num+1
        if num >= len(all_path):
                print("Done")
                break

    if num >= pic_max:
        break


print(toImage.size)
toImage.save('result/picture/all.png')