from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import os

import sys

class MainWindow(QMainWindow):

    def navigate_home(self):
        self.browser.setUrl( QUrl("http://www.google.com") )

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.setCentralWidget(self.browser)

        #ナビゲーションバーの配置
        navtb = QToolBar("Navigation")
        navtb.setIconSize( QSize(32,32) )
        self.addToolBar(navtb)

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

        self.show()

app = QApplication(sys.argv)
window = MainWindow()

app.exec_()

