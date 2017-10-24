import json
import base64
import time
import hashlib
import collections

def md5_encode(data):
    '''
    params: str
    '''
    m=hashlib.md5()
    m.update(data.encode("utf-8"))
    print('md5加密：',m.hexdigest())
    return m.hexdigest()

def base64_en(data):
    '''
    params: str
    '''
    b=json.dumps(data)#字符转换成json
    c=json.loads(b)#json转换为字符
    d=base64.encodebytes(b.encode())#base64加密成二进制
    e=d.decode()
    print('base64加密：',e)
    return e

def base64_de(data):
    '''
    base64解密
    params: str
    中文字符不支持
    '''
    try:
        a=base64.decodebytes(data.encode())
        b=a.decode()
        print('base64解密:',b)
        return b
    except:
        print('解密出错，非base64字符')

def timeTohuman(timestamp):
    '''
    转换为标准时间
    params: int  /1568550534.0
    '''
    #转换成localtime
    time_local = time.localtime(timestamp)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    print('时间戳：'+str(timestamp)+'--->时间：',dt)

def timeTostamp(timest):
    '''
    转换为时间戳
    params: 2017-01-02 12:22:22
    '''
    # 转换成时间数组
    timeArray = time.strptime(timest, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    print('时间'+timest+'---->时间戳：',timestamp)

def sort_json(data):
    '''
    字典排序
    params: dict
    '''
    dic = collections.OrderedDict()
    pic=collections.OrderedDict()
    sor_pub=sorted(data)
    # print('公共参数键排序',sor_pub)
    for i in range(len(sor_pub)):
        dic[sor_pub[i]]=data[sor_pub[i]]
    # print('公共参数排序完毕：',json.dumps(dic))
    sor_params=sorted(data['params'])
    # print('业务参数键排序',sor_params)
    j=0
    for j in range(len(sor_params)):
        pic[sor_params[j]]=data['params'][sor_params[j]]
    # print('业务参数键排序：',json.dumps(pic))
    dic['params']=pic
    result=json.dumps(dic)
    print('字典排序结果：',result)
    return result

#时间转换为时间戳
times= "2019-09-15 20:28:54"
# 时间戳转换为时间
stamp=1505120698

login={
    'act':'60190172',
    'ip':'127.0.0.2',
    'time':'2017-09-07 19:21:27',
    'user_code':'3115997',
    'params':{'user_id':'14','transaction_id':11,"cust_id":"测试11","phone":133333333,"weixin_openid":"34335fsfsfddfsf","weixin_nickname":"回忆11111111"}
}

# sor=sorted(login.items(), key=lambda e:e[0], reverse=False)
# print(sor)

# md5_encode(json.dumps(login))
# timeTostamp(times)
# timeTohuman(1568550534)
# base64_en(a)
# base64_de(asd)
sort_json(login)

# print(json.dumps(login))
# data='act=60190172&ip=127.0.0.2&params={"user_id":14,"transaction_id":11,"cust_id":"测试11","phone":133333333,"weixin_openid":"34335fsfsfddfsf","weixin_nickname":"回忆11111111"}&time=2017-09-07 19:21:27ccylulh0jpmn4pii52v0'
# print(data)


# {"act": "42020144", "ip": "10.10.10.10", "time": "2017/09/07", "ticket": "c25e148a960226f3c84baf99e14d5a2f", "params": {"mobile": "15549565533", "token": "$2a$10$p8n7HXRpJ3S4umgRL3a8k.lMNyuQ/PDhqyd2VIwoVcRwy5oyUeoHS"}, "user_code": "3115997"}
# md5加密结果： 1337e6cd9712f8bef5320d516ec73f8b
# {"time": "2017/09/07", "params": {"token": "$2a$10$p8n7HXRpJ3S4umgRL3a8k.lMNyuQ/PDhqyd2VIwoVcRwy5oyUeoHS", "mobile": "15549565533"}, "act": "42020144", "ip": "10.10.10.10", "user_code": "3115997", "ticket": "c25e148a960226f3c84baf99e14d5a2f"}
# md5加密结果： 512f2276b8ed9fabfe2eb61e21a3de39
# sdsd=base_64(sgin_interface)
# time_decode(times)
# base加密


# tic='''936d80bd68960cb2f3cb61d7941da356'''
# asd='''eyJ0aWNrZXQiOiAiYzI1ZTE0OGE5NjAyMjZmM2M4NGJhZjk5ZTE0ZDVhMmYiLCAidXNlcl9jb2Rl
# IjogIjExMTExIiwgImFjdCI6ICI0MjAyMDExMSIsICJwYXJhbXMiOiB7InVzZXJfaWQiOiAiMzEx
# NTk5OCIsICJwaG9uZSI6ICIxNTg5OTk5OTk5OSIsICJ0eXBlIjogIjEiLCAiZ2lmdF90eXBlIjog
# IjIiLCAicHJpY2UiOiAiMiIsICJnaWZ0X2lkIjogIjMxMTAifSwgInRpbWUiOiAiMjAxNy8wOS8w
# NyIsICJpcCI6ICIxMC4xMC4xMC4xMCJ9'''

# for item,s in enumerate(a):
#     print(item,s)
#