from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import mainwindow
from login_dialog import login_Dialog
from set_dialog import set_Dialog
from apscheduler.schedulers.background import BlockingScheduler
import re
import matplotlib.pyplot as plt
import webbrowser
import json
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime
import itchat
import random

import os

url_list = []
question = {}
chacater_list = ['恋爱','结婚','喜欢','牵手','生孩子','恋情',
                 '幸福','甜蜜','美满','套路','爱情','婚姻',
                 '情书','情感','恋人','男朋友','女朋友']
class MyWindow(QtWidgets.QMainWindow,mainwindow.Ui_MainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
       # super(MyWindow,self).__init__()
        self.setupUi(self)
        self.action_4.triggered.connect(self.exit)
        self.pushButton.clicked.connect(self.baidu)
        self.pushButton_3.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.submit)
        self.pushButton_4.clicked.connect(self.once_send)           #立刻发送
        self.pushButton_5.clicked.connect(self.get_calendar_value)  #设置纪念日
        self.pushButton_6.clicked.connect(self.time_send)           #定时发送
        self.pushButton_7.clicked.connect(self.train)               #做题
        self.pushButton_8.clicked.connect(self.correct)             #判断
        self.Hot_list()
        eng,trans = get_news()
        self.textBrowser.setPlainText(eng+'\n'+trans)
        self.action.triggered.connect(self.login)
        self.label_26.setText('最近的'+createholiday()[0]+'还有'+str(createholiday()[1])+'天')
        self.isseted()
    #train
    def correct(self):
        global question
        answer = self.textBrowser_4.toPlainText()
        correctnum =0
        for key in question['keyword']:
            print(key)
            if answer.find(key)!=-1 :
                correctnum +=1
        print(len(question['keyword']))
        QMessageBox.information(self,'提示','存活率为'+str(correctnum/len(question['keyword'])))

    def train(self):
        try:
            f = open('train.json','r',encoding='utf-8')
        except:
            QMessageBox.warning(self,'警告','wrong')
        else:
            global question
            all_list = json.load(f)
            length = len(all_list)
            for i in range(0,length):
                question = all_list.pop(random.randint(0, len(all_list) - 1))
                if question:
                    self.textBrowser_3.setPlainText(question['question'])
                else:
                    self.textBrowser_3.setPlainText('None,没题目了,你可以选择再次挑战！')
            f.close()

    #微信发送
    def radio_checked(self):
        if self.radioButton.isChecked():
            return self.textBrowser.toPlainText()
        if self.radioButton.isChecked():
            return self.textBrowser_2.toPlainText()

    def choose_obj(self):
        able_list = []
        for friend_dict in get_list():
            if friend_dict['RemarkName'] != '':
                able_list.append(friend_dict['RemarkName'])
            else:
                able_list.append(friend_dict['NickName'])
        name,ok = QtWidgets.QInputDialog.getItem(self, '选择好友', '请选择', able_list)
        if ok:
            return name
        else:
            return False

    def get_username(self,name):
        username = ''
        for friend_dict in get_list():
            if name == friend_dict['RemarkName']:
                username = friend_dict['UserName']
                return username
            if name == friend_dict['NickName']:
                username = friend_dict['UserName']
                return username

    def once_send(self):
        name = self.choose_obj()
        if name:
            itchat.send(self.radio_checked(),self.get_username(name))
        else:
            QMessageBox.information(self,'提示','Wrong')

    def settime(self):
        set_form = set_Dialog()
        set_form.exec_()

    def time_send(self):
        self.settime()
        try:
            f= open('time.json', 'r')
        except:
            QMessageBox.information(self,'提示','wrong')
        else:
            data = json.load(f)
            set_time = data['time']
            data = time.strptime(set_time,'%Y-%m-%d %H:%M:%S')
            data = datetime(data[0], data[1], data[2], data[3], data[4], data[5])
            if datetime.now()<=data:
                name = self.choose_obj()
                if name:
                    scheduler = BlockingScheduler()
                    scheduler.add_job(SentChatMsg, 'date', run_date=set_time,
                            kwargs={'username':self.get_username(name), "context": self.radio_checked()})
                    QMessageBox.information(self,'提示框',"设置完成" + ":\n"
                                   "待发送时间：" + set_time + "\n"
                                                     +"待发送到：" + name + "\n"
                                                                    +"待发送内容：" + '\n'+self.radio_checked() + "\n"
                                                                                    "******************\n")
                    scheduler.start()
                else:
                    QMessageBox.information(self,'提示','Wrong')
            else :
                QMessageBox.warning(self,'提示','时间设置错误，请重新设置!')
    # ---

    # def SentChatMsg(self,username, name, context):
    #     itchat.send_msg(context, username)
    #     QMessageBox.information(self,'提示',"发送时间：" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    #                                                                    "发送到：" + name + "\n"
    #                                                                                    "发送内容：" + context + "\n")
    #
    #日历，纪念日
    def isseted(self):
        try:
            f = open('date.json','r')
        except:
            pass
        else:
            info = json.load(f)
            if info['seted'] ==1 :
                self.pushButton_5.setEnabled(False)
            if info['memorial']:
                date = info['memorial']
                self.label_19.setText('在一起已经'+str(days(date))+'天啦')
            f.close()


    def get_calendar_value(self):
        date = self.calendarWidget.selectedDate()
        info = dict()
        info['memorial'] = str(date.toPyDate())
        info['seted'] = 1
        with open('date.json','w') as f:
            json.dump(info,f)
            self.pushButton_5.setEnabled(False)
            QMessageBox.information(self,'提示','已设置')
    #
    #登录网站
    def login(self):
        login_form = login_Dialog()
        login_form.exec_()
    #
    #热搜
    def baidu(self):
        webbrowser.open('https://www.baidu.com/s?wd=' + self.lineEdit.text()+
        '&rsv_spt=1&rsv_iqid=0xfd5f7ef90001a23a&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&'
        'rsv_enter=1&rsv_sug3=10&rsv_sug1=10&rsv_sug7=100&rsv_sug2=0&inputT=4386&rsv_sug4=4386')

    def Hot_list(self):
        crawler = search()
        crawler.supple()
        crawler.weibo()
        crawler.baidu()
        crawler.sougou()
        self.label.setText(url_list.pop())
        self.label_2.setText(url_list.pop())
        self.label_3.setText(url_list.pop())
        self.label_4.setText(url_list.pop())
        self.label_5.setText(url_list.pop())
        self.label_6.setText(url_list.pop())
        self.label_7.setText(url_list.pop())
        self.label_8.setText(url_list.pop())
        self.label_9.setText(url_list.pop())
        self.label_10.setText(url_list.pop())
        self.label_11.setText(url_list.pop())
        self.label_12.setText(url_list.pop())
        self.label_13.setText(url_list.pop())
        self.label_14.setText(url_list.pop())
        self.label_15.setText(url_list.pop())
        self.label_16.setText(url_list.pop())
        self.label_17.setText(url_list.pop())
        self.label_18.setText(url_list.pop())
        self.label_20.setText(url_list.pop())
        self.label_21.setText(url_list.pop())
        self.label_22.setText(url_list.pop())
        self.label_23.setText(url_list.pop())
        self.label_24.setText(url_list.pop())
        self.label_25.setText(url_list.pop())
    #

    def exit(self):
        self.close()
    #上传聊天日常
    def openfile(self):
        file_path,filetype = QFileDialog.getOpenFileName(self,'打开文件')
        if file_path:
            with open(file_path,'r',encoding='utf-8') as f:
                text = f.read()
                self.plainTextEdit.setPlainText(text)
                self.mostphoto(file_path)
                self.cretime(file_path)
        else:
            QMessageBox.warning(self, '警告', '加载失败')

    def submit(self):
        pass
        #分析聊天日常
    def mostphoto(self,filename):
        import re
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
            times = re.findall(re.compile(r"(\d\d):\d\d:\d\d"), data)
            phototimes = re.findall(re.compile(r"[图片]"), data)
            if phototimes:
                if (len(phototimes) > (len(times) - len(phototimes))):
                    QMessageBox.information(self,'提示框','两位斗图鬼才用表情包征服了彼此！')
                else:
                    QMessageBox.information(self,'提示框','情话绵绵，爱情已融入生活中的点滴！')
            else:
                QMessageBox.information(self, '提示框', '情话绵绵，爱情已融入生活中的点滴！')

    def cretime(self,filename):#分析折线表
        time_dict = dict()
        for i in range(0, 24):
            if i < 10:
                i = '0' + str(i)
            else:
                i = str(i)
            time_dict[i] = 0

        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read()
            # 例如20:50:52，要匹配其中的20
            pa = re.compile(r"(\d\d):\d\d:\d\d")
            times = re.findall(pa, data)
            for i in time_dict.keys():
                for time in times:
                    if time == i:
                        time_dict[i] += 1
        if times:
            plt.plot(time_dict.keys(), time_dict.values())  # plot函数根据数字绘制出有意义的图形
            plt.title('Analysis of Chating', fontsize=24)  # 给图表指定标题
            plt.xlabel('Time', fontsize=10)  # 给X轴设置标题
            plt.ylabel('Times', fontsize=10)  # 给Y轴设置标题
            plt.show()  # show函数打开matplotlib查看器,并显示绘制的图形



class search():
    def weibo(self):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.get('http://s.weibo.com/top/summary?cate=realtimehot', headers=headers)
        r.encoding = 'utf-8'
        html = r.text
        bsobj = BeautifulSoup(html)
        sou_list = bsobj.find('table', {'id': "realtimehot"}).findAll('p', {'class': 'star_name'})
        for list_s in sou_list:
            a = list_s.find('a')
            a = str(a).replace('amp;', '')
            a = a.replace('/weibo', 'http://s.weibo.com/weibo')
            for chacater in chacater_list:
                if str(a).find(chacater) != -1:
                    url_list.append(a)
                    break

    def sougou(self):
        accepet_encoding = 'gzip, deflate'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/65.0.3325.181 Safari/537.36)'
        headers = {'User-Agent': user_agent, 'Accept-Encoding': accepet_encoding}
        r = requests.get('http://top.sogou.com/', headers=headers)
        r.encoding = 'utf-8'
        html = r.text
        bsobj = BeautifulSoup(html)
        sou_list = bsobj.find('div', {'class': 'hot-b'}).find('ol').findAll('li')
        for list_s in sou_list:
            a = list_s.find('a')
            a=str(a)
            for chacater in chacater_list:
                if a.find(chacater) != -1:
                    url_list.append(a)
                    break

    def baidu(self):
        accepet_encoding = 'gzip, deflate'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' \
                     '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36)'
        headers = {'User-Agent': user_agent, 'Accept-Encoding': accepet_encoding}
        r = requests.get('http://top.baidu.com/', headers=headers)
        r.encoding = 'gb2312'
        html = r.text
        bsobj = BeautifulSoup(html)
        sou_list = bsobj.find('ul', {'id': 'hot-list'}).findAll('li')
        for list_s in sou_list:
            a = list_s.find('a')
            a=str(a)
            for chacater in chacater_list:
                if a.find(chacater) != -1:
                    url_list.append(a)
                    break

    def supple(self):
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.get('https://www.jj59.com/love-gushi/', headers=headers)
        r.encoding = 'utf-8'
        html = r.text
        bsobj = BeautifulSoup(html)
        sou_list = bsobj.find('ul', {'class': "e2"}).findAll('li', {'class': 'bd'})
        for list_s in sou_list:
            a = list_s.find('h3').find('a')
            a = str(a).replace('/jjart','https://www.jj59.com/jjart')
            url_list.append(a)

def days(date):
    date = time.strptime(date,'%Y-%m-%d')
    date =datetime(date[0],date[1],date[2])
    now = datetime.now()
    return (date-now).days + 1

def createholiday():
    holiday_dict = {'元旦':'1-1','情人节':'2-14','女生节':'3-7','植树节':'3-12',
                    '愚人节':'4-1','劳动节':'5-1','母亲节':'5-13','儿童节':'6-1',
                    '父亲节':'6-17','端午节':'6-18','国庆节':'10-1','万圣节':'10-31',
                    '平安夜':'12-24','感恩节':'12-25'}
    min = 10000
    holiday =''
    for x,y in holiday_dict.items():
        date = time.strptime(y,'%m-%d')
        date = datetime(datetime.now().year,date[1],date[2])
        days = (datetime.now()-date).days + 1
        if abs(days)<min:
            min = abs(days)
            holiday = x
    return holiday,min

def get_news():
    # 获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation[5:]

def get_list():
    itchat.auto_login(hotReload=True)
    friends_list = []
    for i in itchat.get_friends(update=True)[1:]:
        friends_dict = {}
        friends_dict['UserName']=i['UserName']
        friends_dict['NickName'] = i['NickName']
        friends_dict['RemarkName'] = i['RemarkName']
        friends_list.append(friends_dict)
    return (friends_list)

def SentChatMsg(username, context):
    itchat.send_msg(context, username)