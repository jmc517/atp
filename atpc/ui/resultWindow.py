# -*- coding: utf-8 -*-
import os
import sys

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
import webbrowser as web
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton, QTextEdit
from PyQt5.QtWidgets import QTreeWidget
from PyQt5.QtWidgets import QWidget
from PyQt5 import Qt

from interface.get_data import getter


class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()

    def initUI(self, id):
        self.setWindowTitle('结果查看')
        self.setWindowIcon(QIcon('./images/icon.jpg'))
        self.setGeometry(10, 10, 1024, 800)
        self.setWindowFlags(Qt.Qt.SubWindow)
        self.taskid = id
        grid = QGridLayout()

        closeBtn = QPushButton('关闭')
        downloadBtn = QPushButton('下载')
        closeBtn.resize(closeBtn.sizeHint())
        downloadBtn.resize(downloadBtn.sizeHint())
        closeBtn.clicked.connect(self.close)
        downloadBtn.clicked.connect(self.downloadLog)



        self.textArea = QTextEdit()
        self.textArea.setReadOnly(True)
        self.textArea.setTextColor(QColor(20,150,150))
        self.textArea.setFont(QFont('sanserif', 12))
        self.textArea.setPlaceholderText('没有生成报告，请确定是否执行结束')


        grid.addWidget(closeBtn, 1, 9)
        grid.addWidget(downloadBtn, 1, 10)
        grid.addWidget(self.textArea, 2, 0, 20, 11)
        cf = getter.get_app_conf()
        projectPath = str(cf.get('baseconf', 'projectLocation'))
        reportPath = os.path.join(projectPath, 'reports', str(id), 'report.log')
        if os.path.exists(reportPath):
            with open(reportPath, 'r', encoding='utf-8') as file:
                for f in file:
                    self.textArea.append(f.replace('\n',''))
        else:
            pass

        self.setLayout(grid)
        self.show()

    def downloadLog(self):
        web.open_new_tab('http://localhost:9527/' + self.taskid + '/' + 'report.log')
