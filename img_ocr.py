# -*- coding:utf-8 -*-
import pytesseract
from PIL import Image
import requests
import os
# 验证码识别
# 下载验证码 @输入下载数量

def code_down(num):
    imgurl = 'https://wssb6.szsi.gov.cn/NetApplyWeb/CImages'
    for i in range(num):
        data=requests.get(imgurl)
        name=str(i)
        download_img(data.content,name)

def download_img(imgdata,name):
    with open('./code_img/'+name+'.jpg','wb') as f:
        f.write(imgdata)

def code_ocr(num):
    for i in range(num):
        image=Image.open('./grey/'+"grey"+str(i)+'.jpg')
        code=pytesseract.image_to_string(image,config='-psm 7')
        print("index:%d code:%s"%(i,code))
def img_grey(num):
    for i in range(num):
        image=Image.open('./code_img/'+str(i)+'.jpg')
        grey=image.convert('L')
        grey.save("./grey/grey"+str(i)+'.jpg')

# 图片批量下载
# code_down(100)
# 图片识别
code_ocr(20)
# 图片灰度处理
# img_grey(86)
