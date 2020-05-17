	# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Note/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 10
locale = "Asia/Shanghai"
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "latinos-bub/Note@gh-pages"
}

# 站点设置
site_name = "拉丁小毛的小站"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
site_favicon = "${static_prefix}favicon.ico"
author = "拉丁小毛"
email = "util.you.com@gmail.com"
author_homepage = "/"
description = "三里清风三里路，步步风里再无你"
key_words = ['拉丁小毛', 'Note', 'Maverick']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "七夏浅笑",
        "url": "https://www.julydate.com/",
        "brief": "已经不再是小鲜肉的95后水瓶座妹子一枚，热爱互联网，感兴趣的事情什么都会一点点，代码烂，游戏菜，天天等着大佬带，常用ID: 七夏浅笑，Julydate | 邮箱: i#xhtml.love (#换成@)，唯一会玩的游戏守望先锋: 七夏浅笑#5977，无关风月，不忘初心"
    },
    {
        "name": "seekbetter.me",
        "url": "https://seekbetter.me/",
        "brief": "优秀个人独立博客"
    },
    {
        "name" : "柠檬酸的情感小阁",
        "url" : "https://cherryml.com/",
	"brief": "喜欢漂亮妹子的程序猿"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/latinxiaomao",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/latinos-bub",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://www.zhihu.com/people/shiro.liang.yi/",
        "icon": "gi gi-weibo"
    }
]

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "oTSl2QltX9lo3eLGQVrAeYGD-gzGzoHsz",
    "appKey": "0vc24cG5OGEYYrDFAnPR5bs3",
}

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

# 添加到 <footer> 的内容
footer_addon = ''

# 添加到 <body> 的内容
body_addon = ''

# 背景图片
background_img = "${static_prefix}background.png"
