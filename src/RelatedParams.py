
class RelatedParams:
    re={'reason': 'successed',
        'error_code': 0,
        'result': {'ji': '馀事勿取',
                    'xiongshen': '五虚 土符 触水龙',
                    'wuxing': '杨柳木 开执位',
                    'id': '1666',
                    'yinli': '甲午(马)年八月十六',
                    'yangli': '2014-09-09',
                    'jishen': '天恩 母仓 月德 不将 四相 阴德 金堂 时阳 生气 天仓',
                    'yi': '祭祀 立碑 修坟 启钻 除服 成服 馀事勿取',
                    'baiji': '癸不词讼理弱敌强 未不服药毒气入肠',
                    'chongsha': '冲牛(丁丑)煞西'}
        }
    #print(re[result])
    dict_relatedparamsvalue={}
    relatedparams="${date}=[result][yangli]"
    relatedparams=relatedparams.replace("\n","").replace("\r","").split(";")
    print(relatedparams)
    for i  in range(len(relatedparams)):
        items=relatedparams[i].split("=")
        #print(items)#拆分成一个列表
        #print(items[1][::-1])#列表第一个str元素的第一个字符到倒数第二个字符：result][yingli
        for key in items[1][1:-1].split("]["):
            print("key",key)
            temp=re[key]
            print(temp)
            re=temp

        dict_relatedparamsvalue['date']=re
        #print(dict_relatedparamsvalue)





