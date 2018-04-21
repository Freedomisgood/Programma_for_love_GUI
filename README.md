# Programma_for_love_GUI
所依赖的库:
``` 
APScheduler==3.5.1
beautifulsoup4==4.6.0
bs4==0.0.1
certifi==2018.4.16
chardet==3.0.4
cycler==0.10.0
idna==2.6
itchat==1.3.10
kiwisolver==1.0.1
matplotlib==2.2.2
numpy==1.14.2
pyparsing==2.2.0
pypng==0.0.18
PyQRCode==1.2.1
PyQt5==5.10.1
python-dateutil==2.7.2
pytz==2018.4
requests==2.18.4
sip==4.19.8
six==1.11.0
tzlocal==1.5.1
urllib3==1.22
xlrd==1.1.0
```


开发环境为:python3.6
安装依赖库: pip3 install -r requirements.txt
运行文件: python main.py(请在装完库的情况下，同时若在虚拟环境下安装的库，请进入虚拟环境再运行)

---

功能介绍：
1.分析聊天记录

2.显示情侣间的故事、有关情侣的热搜（百度、微博、搜狗）

3.定时发送、每日一句的微信消息

4.纪念日设置，最近的节假日提醒。

5.求生欲训练。

---

![加载界面](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/2.jpg)

​	嗯，没错，加载界面就是软研群里专门用来膜拜的图。由于写了个简单的爬虫，在界面加载时就会立刻爬取百度、微博、搜狗、以及情侣故事网中的故事（以免热搜的条目不够，避免因为self.label.getText()报错），所以会耗时比较久，因此做了个加载界面。

---

功能2：情侣热搜事

![热搜](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/22.jpg)

热搜榜上爬取下来的数据，有些可能不能完全显示，忘记做超过限制长度就用...来省略。

▲.如果没有联网打开这个程序，会抛出异常，无法运行

---

功能1：聊天日常分享

![日常](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/9.jpg)

按下打开按钮选择聊天记录（.txt）（主要设计的就是导入情侣间的QQ聊天日常，平时的话很少会这样记录吧），导入后会对聊天记录进行分析，如果[图片]出现的次数大于文字行的数量，则会显示"两位斗图鬼才用表情包征服了彼此！",反之会弹出“情话绵绵，爱情已融入生活中的点滴！”。然后会出现聊天时间的分析表，分析两人最频繁的聊天时间段。如果选择不导入QQ聊天记录而是其他文本，则不会弹出分析表，但还是会有‘文字’和‘图片’次数的分析。

![分析图](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/11.jpg)

!!!....至于菜单栏中的‘登录’和上传按钮，由于云服务器502的问题，展示聊天记录的网站出错，就没有再继续写这两个的功能

![登录](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/10.jpg)

---

功能3：微信发送每日问候（可定时）

![微信定时发送]( https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/1.jpg )

可选择发送金山词霸提供的中英文每日一句，也可以选择发送自定义语句

若选择立刻发送，则会弹出‘选择好友’窗口，在此之前会有扫码过程。选择的好友顺序为‘有备注的优先，其次为微信好友的昵称’，选择完后就会立刻发送。

如果选择定时发送会首先弹出定时窗口，若所选时间在今天之前，则会弹出‘时间错误，请重设’，若设置正确则会弹出扫码界面（若首次登陆），其次是选择好友，好友列表同上，选择完成后会弹出提示框（见图3）.点击确定，定时完成

!!!!!!!!

▲.注意:

1.首次使用此过程时弹出扫码（记得在手机上按下确定登录啊！！！），程序可能出现图4的未响应，反应有点慢。此时只需扫好码静静等待即可。

2.登录后，会进入选择好友的弹窗，在此之前可能也会出现‘未响应’，甚至出现“关闭程序”或是“调试”，仍只需静等即可

3.定时发送全设置好后，定时任务发布，但这时程序会陷入“无响应“，但内容仍会定时发送，但程序会一直卡在无响应，（这算个不足），无法进行其他操作

4.定时发送任务提交后，不能关闭软件，否则无效

（图一）

![选择好友](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/3.jpg)

（图二）

![时间错误](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/x.jpg)

（图三）

![设置完成](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/4.jpg)

（图四）

![未响应](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/5.jpg)

---

功能2：纪念日设置
（图一）

![日历1](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/6.jpg)

首次界面为图一，点击日历上日期再按下设置按钮即可设置成功，但也可以设置在今天之后，算个BUG（若在今天之后，设为无效忘记写了）。
还有个小问题是，设置后图二的“在一起已经x天啦”需要再次启动才可见（其实可以在按下设置后，读取下'date.json',emmm，反正现在忘记做了）
最近的节假日，节假日有哪些都是我在程序内设置好的，忘记要加生日了。
在一起的时间好像是负数？貌似是now-date写反了，写成date-now了。

![日历2](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/ri.jpg)

---

功能5：求生欲训练
（图一）

![求生欲](https://github.com/Freedomisgood/Programma_for_love_GUI/tree/master/readme/8.jpg)

按下做题按钮会在Q：编辑窗口中出现题目，只需在A：中填下回答即可，再按下提交，就会反馈给你女友对回答的满意程度（根据关键字来判断的哦!）

△.数据保存在了train.json文件，若此文件丢失，则该功能无法正常运行。（其实可以在程序中直接定义，然后初始化窗口的时候也生成这个文件，但....，当初还是忘记写了）

---
肝了三天，总算写完啦。遗憾的是，展示的时候崩了3个功能，感觉心态也蹦了。QAQ。
界面有点简陋。可能天生没有艺术天赋吧23333.....

库有点多，就没有打包成.exe二进制文件。

---

### 运行环境：在windows下开发，可以运行，linux未试。
