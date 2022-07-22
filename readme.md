# 爬取b站搜索信息

我们这里项目主要目的是通过关键词搜出 “综合”，“最多点击”， “最多弹幕”、“最新发布”、“最多收藏”的视频信息结果，并且将其汇总到excel表格中

## 前提条件

基本网址：
https://api.bilibili.com/x/web-interface/search/type?&search_type=video&page_size=50&page=1&order=pubdate&keyword=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0

参数说明：

- page: 1~70左右 超过最大值 页面出现重复 
- page_size: 50 这里50是最大数量
- order: 
    - "" 综合
    - click 最多点击
    - dm 最多弹幕
    - pubdate 最新发布
    - stow 最多收藏
- keyword: 搜索内容

爬取前首先获得自己浏览器的header,按F12控制台上输入以下命令可以获得： <b>javascript:alert(navigator.userAgent)</b>


抓包内容的基本json结构（精简版）：
```
{
    data:{
        result:[
            author: ""
            title: ""
            description: ""
            typename:""
            tag:""
            arcurl:""

        ]
    }
}
```

## 网址爬取

https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page=1&page_size=42&order=pubdate&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&category_id=&search_type=video&dynamic_offset=0&preload=true&com2co=true


https://api.bilibili.com/x/web-interface/search/type?&page=1&page_size=50&order=pubdate&from_spmid=333.337&platform=pc&keyword=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&search_type=video

//最新发布
order = pubdate 
https://api.bilibili.com/x/web-interface/search/type?&page=1&page_size=50&order=pubdate&keyword=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&search_type=video

//综合
order = 

https://api.bilibili.com/x/web-interface/search/all/v2?page=1&page_size=50&order=&keyword=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&search_type=video

// 最多点击
order = click

//最多弹幕

order = dm

//最多收藏
order = stow


公共参数
  __refresh__=true
  &page=1
  &page_size=42
  &order=pubdate
  &from_spmid=333.337
  &platform=pc&highlight=1
  &single_column=0
  &keyword=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0
  &search_type=video
  &dynamic_offset=0
  &preload=true
  &com2co=true

一页的最大值为50
