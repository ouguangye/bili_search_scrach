import requests
import json
import time
import random
import xlwt

headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0'}
page_size = 65
order = [("综合排序",""),("最多点击","click"),("最新发布","pubdate"),("最多弹幕","dm"),("最多收藏","stow")]
url = 'https://api.bilibili.com/x/web-interface/search/type'
type = "video"
page_size = 50
keyword = '疾病科普'

def processStr(s1,s2):
    if s2 in s1:
        s1 = s1.replace(s2,'')
        #print(s1)
    return s1

def save(data,name):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('sheet1',cell_overwrite_ok=True)
    column = ["author","title","description","typename","tag","url"]
    for i in range(len(column)):
        sheet1.write(0,i,column[i])

    for i in range(len(data)):
        title = processStr(data[i]["title"],"<em class=\"keyword\">")
        title = processStr(title,"</em>")
        
        sheet1.write(i+1,0,data[i]["author"])
        sheet1.write(i+1,1,title)
        sheet1.write(i+1,2,data[i]["description"])
        sheet1.write(i+1,3,data[i]["typename"])
        sheet1.write(i+1,4,data[i]["tag"])
        sheet1.write(i+1,5,data[i]["url"])
        
    f.save(name + '.xls')

for o in order:
    prelist = []
    datalist = []
    for i in range(70):
        r = requests.get(url,params={"search_type":type , "page_size":page_size, "order":o[1],"keyword":keyword, "page":i+1},headers=headers)
        data = json.loads(r.text)
        data = data["data"]
        data = data["result"]

        if prelist == data:
            break
        datalist.extend(data)
        prelist = data
        time.sleep(random.random()*3)
    save(datalist,o[0])