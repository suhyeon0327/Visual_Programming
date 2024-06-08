# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homework_plus.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget, QFileDialog)

class Ui_MainWindow(object):   # Ui_MainWindow 클래스 정의
    def setupUi(self, MainWindow):   # setupUi 메서드 정의
        
        # 절대 경로 저장
        self.fstr = os.path.dirname(
            os.path.abspath(__file__)
            )        
        
        # widget 설정
        if not MainWindow.objectName():   # MainWindow에 객체 이름이 없으면
            MainWindow.setObjectName(u"MainWindow")   # 객체 이름을 MainWindow로 설정
        MainWindow.resize(320, 240)   # MainWindow의 사이즈를 너비: 320, 높이: 240으로 설정
        
        # actionfile_select 생성
        self.actionfile_select = QAction(MainWindow)
        self.actionfile_select.setObjectName(u"actionfile_select")   # 이름 설정
        
        # actionOpen
        self.actionOpen = QAction(MainWindow)   # actionOpen 액션 생성
        self.actionOpen.setObjectName(u"actionOpen")   # 이름 설정
        self.actionOpen.triggered.connect(self.open_file)   # triggered signal을 open_file 슬롯에 연결
        
        icon = QIcon()   # icon 객체 생성
        icon.addFile(f"{self.fstr}/open.png", QSize(), QIcon.Normal, QIcon.Off)   # icon에 open.png 할당
        self.actionOpen.setIcon(icon)   # actionOpen에 icon 추가
        
        # actionSave
        self.actionSave = QAction(MainWindow)   # actionSave 액션 설정
        self.actionSave.setObjectName(u"actionSave")   # 이름 설정
        self.actionSave.triggered.connect(self.save_file)   # triggered signal을 save_file 슬롯에 연결
        
        icon1 = QIcon()   # icon 객체 생성
        icon1.addFile(f"{self.fstr}/save.png", QSize(), QIcon.Normal, QIcon.Off)   # icon에 save.png 할당
        self.actionSave.setIcon(icon1)   # actionSave에 icon 추가
        
        # Main Window의 중앙 위젯
        self.centralwidget = QWidget(MainWindow)   # centralwidget 설정
        self.centralwidget.setObjectName(u"centralwidget")   # 객체 이름 설정
        self.verticalLayout = QVBoxLayout(self.centralwidget)   # 수직 레이아웃 설정
        self.verticalLayout.setObjectName(u"verticalLayout")   # 객체 이름 설정
        
        # textEdit
        self.textEdit = QTextEdit(self.centralwidget)   # QTextEdit 생성
        self.textEdit.setObjectName(u"textEdit")   # 이름 설정
        self.textEdit.textChanged.connect(self.update_statusbar)   # textChanged signal을 update_statusbar 슬롯에 연결
        self.verticalLayout.addWidget(self.textEdit)   # 수직 레이아웃에 추가

        # pushButton
        self.pushButton = QPushButton(self.centralwidget)   # QPushButton 생성
        self.pushButton.setObjectName(u"pushButton")   # 이름 설정
        self.verticalLayout.addWidget(self.pushButton)   # 수직 레이아웃에 추가

        # statusbar
        self.statusbar = QStatusBar()   # Qstatusbar 생성
        self.setStatusBar(self.statusbar)   # 상태표시줄로 설정
        
        # MainWindow 설정
        MainWindow.setCentralWidget(self.centralwidget)   # Main Window의 중앙위젯을 self.centralwidget로 설정
        
        self.menubar = QMenuBar(MainWindow)   # MainWindow에 QMenuBar 생성
        self.menubar.setObjectName(u"menubar")   # menubar 이름 설정
        self.menubar.setGeometry(QRect(0, 0, 320, 22))   # menubar의 위치와 크기 설정
        
        self.menufile = QMenu(self.menubar)   # MainWindow에 QMenu 생성
        self.menufile.setObjectName(u"menufile")   # menufile 이름 설정
        MainWindow.setMenuBar(self.menubar)   # MainWindow의 메뉴바를 self.menubar로 설정
        
        self.statusbar = QStatusBar(MainWindow)   # MainWindow에 QStatusBar 생성
        self.statusbar.setObjectName(u"statusbar")   # statusbar 이름 설정
        MainWindow.setStatusBar(self.statusbar)   # MainWindow의 상태표시줄을 self.statusbar로 설정

        self.menubar.addAction(self.menufile.menuAction())   # 메뉴바에 file 메뉴 추가
        self.menufile.addAction(self.actionOpen)   # file 메뉴에 Open 액션 추가
        self.menufile.addAction(self.actionSave)   # file 메뉴에 Save 액션 추가

        self.retranslateUi(MainWindow)   # retranslateUi 메서드 호출
        self.pushButton.clicked.connect(MainWindow.close)   # pushButton을 clicked 시그널을 MainWindow.close 슬롯에 연결
        QMetaObject.connectSlotsByName(MainWindow)   # signal과 slot이 연결되도록 함
    # setupUi

    # 파일 불러와서 textEdit에 추가
    def open_file(self):
        # 파일 불러오기
        file_name, is_ok = QFileDialog.getOpenFileName(
               self,
               "Open file",
               "self.fstr",
               "txt files (*.txt)"
        )
        
        # 선택한 파일의 내용을 읽어 textEdit에 추가
        if file_name:
            with open(f"{self.fstr}/textEdit.txt", 'r') as file:
                text = file.read()
                self.textEdit.setPlainText(text)
    
    # 텍스트를 파일로 저장
    def save_file(self):
        # textEdit에 쓰여진 내용을 Save File로 저장
        filename, _ = QFileDialog.getSaveFileName(
            self, 
            "Save File",
            "",
            "txt files (*.txt)"
            )
        if filename:
            with open(filename, 'w') as file:
                file.write(self.textEdit.toPlainText())
    
    # 상태표시줄에 textEdit의 텍스트 길이를 업데이트        
    def update_statusbar(self):
        text_length = len(self.textEdit.toPlainText())   # textEdit의 텍스트 길이 값 저장
        self.statusbar.showMessage(f"length: {text_length}")   # 텍스트 길이 보여주기
    
    # retranslateUi      
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))   # 제목 설정
        self.actionfile_select.setText(QCoreApplication.translate("MainWindow", u"File select", None))   # actionfile_select의 텍스트를 File select으로 설정
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))   # actionOpen의 텍스트를 "Open"으로 설정
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))   # actionSave의 텍스트를 "Save"으로 설정 
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Close", None))   # pushButton의 텍스트를 "Close"으로 설정
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))   # menufile의 제목을 "File"으로 설정
    # retranslateUi