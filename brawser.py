from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import os

import sys

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

DEFAULT_WAIT_TIME_SECONDS = 5

class MainWindow(QMainWindow):

    def navigate_home(self):
        self.browser.setUrl( QUrl("http://www.google.com") )

    def navigate_to_url(self):
        q = QUrl( self.urlbar.text() )
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s" % title)

    def update_urlbar(self, q):


        #ブラウザ起動オプションの設定
        options = webdriver.ChromeOptions()
        options.add_argument('/usr/local/src/chromedriver_linux64/chromedriver')
        options.add_argument('/usr/local/src/chrome-linux/chrome')

        driver = webdriver.Chrome(options=options)

        crawl_target_url = q.toString()

        print(crawl_target_url)

        driver.get(q.toString())

        time.sleep(DEFAULT_WAIT_TIME_SECONDS)


        #pass

        #if q.scheme() == 'https':
        #    #アイコンの大きさを指定したい
        #    self.httpsicon.setPixmap( QPixmap( os.path.join('icons','icon-lock.svg') ) )

        #else:
        #    #アイコンの大きさを指定したい
        #    self.httpsicon.setPixmap( QPixmap( os.path.join('icons','icon-unlock.svg') ) )

        self.urlbar.setText( q.toString() )
        self.urlbar.setCursorPosition(0)

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        #ナビゲーションバーの配置
        navtb = QToolBar("Navigation")
        navtb.setIconSize( QSize(32,32) )
        self.addToolBar(navtb)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.setCentralWidget(self.browser)

        #戻るボタンを配置
        back_btn = QAction( QIcon(os.path.join('icons','icon-back.svg')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect( self.browser.back )
        navtb.addAction(back_btn)

        #進むボタンを配置
        forward_btn = QAction( QIcon(os.path.join('icons','icon-forward.svg')), "Forward", self)
        forward_btn.setStatusTip("Forward to next page")
        forward_btn.triggered.connect( self.browser.forward )
        navtb.addAction(forward_btn)

        #更新ボタンを配置
        reload_btn = QAction( QIcon(os.path.join('icons','icon-reload.svg')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect( self.browser.reload )
        navtb.addAction(reload_btn)

        #ホームボタンを配置
        home_btn = QAction( QIcon(os.path.join('icons','icon-home.svg')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect( self.navigate_home )
        navtb.addAction(home_btn)

        ##デフォルトURLページのスキーマに合わせてデフォルトのスキーマアイコンを配置
        #アイコンの大きさを指定したい
        #self.httpsicon = QLabel()
        #self.httpsicon.setPixmap( QPixmap( os.path.join('icons','icon-unlock.svg') ) )
        #navtb.addWidget(self.httpsicon)

        #URL入力バーを配置
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect( self.navigate_to_url )
        navtb.addWidget(self.urlbar)

        #ローディング中止ボタンを配置
        stop_btn = QAction( QIcon(os.path.join('icons','icon-stop.svg')), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect( self.browser.stop )
        navtb.addAction(stop_btn)

        #URL入力バーの状態が変更された際のイベントハンドラを定義
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)

        self.show()

app = QApplication(sys.argv)
window = MainWindow()

app.exec_()

