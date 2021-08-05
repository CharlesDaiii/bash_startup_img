import sys
import cv2
import matplotlib.pyplot as plt
import numpy as np
import base64
import os


def img_base64(img_path):
    with open(img_path,"rb") as f:
        base64_str = base64.b64encode(f.read())
    return base64_str

def cv2_base64(image):
    base64_str = cv2.imencode('.jpg',image)[1].tostring()
    base64_str = base64.b64encode(base64_str)
    return base64_str

def base64_cv2(base64_str):
    imgString = base64.b64decode(base64_str)
    nparr = np.fromstring(imgString,np.uint8)
    image = cv2.imdecode(nparr,cv2.IMREAD_COLOR)
    return image



def img_RGBcolor_ascii(img,r=2.4):
    #img: input img img here is 3channel!
    #r:  raito params #由于不同控制台的字符长宽比不同，所以比例需要适当调整。
    #window cmd：r=3/linux console r=
    
    grays = "@%#*+=-:. "   #由于控制台是白色背景，所以先密后疏/黑色背景要转置一下
    gs = 10                #10级灰度
    #grays2 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^.` "
    #gs2 = 67              #67级灰度

    #宽（列）和高（行数）
    w = img.shape[1]
    h = img.shape[0]
    ratio = r*float(w)/h  #调整长宽比-根据终端改变r

    scale = w // 50   #缩放尺度/取值步长，向下取整，每100/50个像素取一个 值越小图越小(scale 越大)

    for y in range(0, h, int(scale*ratio)):  #根据缩放长度 遍历高度 y对于h，x对应w
        strline=''
        for x in range(0, w, scale):  #根据缩放长度 遍历宽度
            idx=int(img[100][100].mean()) * gs // 255  #获取每个点的灰度  根据不同的灰度填写相应的 替换字符
            if idx==gs:
                idx=gs-1  #防止溢出
			######改变这里，将RGB值，利用2控制参数直接输入
            color_id = "\033[38;2;%d;%d;%dm%s"%(img[y][x][0],img[y][x][1],img[y][x][2],grays[2])      #输出！  
            #38为前景  ->> 48为背景 ,使用grays[-1/-2]输出
            strline+= color_id #按行写入控制台
        print(strline)

if __name__=="__main__":
    #图片名字
    img_name = 'mwzz.jpg'
    #图片的相对路径
    foldr_dir = os.path.dirname(__file__) 
    if foldr_dir == "":
        foldr_dir = '.'
    img_dir = foldr_dir + "/"+ img_name
    print(img_dir)
    img_cv2 = cv2.imread(img_dir)  #读入图片为cv2
    img =cv2.cvtColor(img_cv2,cv2.COLOR_BGR2RGB)
    img_RGBcolor_ascii(img)
