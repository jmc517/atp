# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QTreeWidget
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtWidgets import QWidget


class Example(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowTitle('TreeWidget')
        self.tree = QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderLabels(['用例名称'])
        self.tree.setColumnWidth(0, 200)
        self.featureTree = QTreeWidgetItem()
        self.setGeometry(100, 100, 600, 400)
        '''
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'name1')
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, 'name2')
        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child4 = QTreeWidgetItem(child3)
        child4.setText(0, 'child4\n\nsdsdf\nsdfsdf\n')
        child4.setText(1, 'name4')
        child4.setBackground(1,QBrush(QColor(123,60,40)))

        root1 = QTreeWidgetItem(self.tree)
        root1.setText(0, 'root1')
        QTreeWidgetItem(root1).setText(0, 'aaa')
        QTreeWidgetItem(root1).setText(0, 'bbb')
        '''
        file = open('/home/ogq/learn/report.log', 'r')
        step_flag = None
        scen_flag = None
        for f in file:
            if f.strip().startswith('场景:'):
                step_flag = True
                scen_flag = True
                self.featureTree = QTreeWidgetItem(self.tree)
                self.featureTree.setText(0, f.strip()[len('场景:'):].strip())
            elif not f.strip().startswith('背景:') and not f.strip().startswith('功能:') and not f.strip() == '':
                backgroundTree = QTreeWidgetItem(self.featureTree)
                if '...' in f:
                    backgroundTree.setText(0, f.replace('\n','')[: f.index('...')])
                else:
                    backgroundTree.setText(0, f.replace('\n', ''))
                if 'passed' in f:
                    backgroundTree.setBackground(0, QBrush(QColor(0, 250, 0)))
                    step_flag = True

                if 'failed' in f:
                    backgroundTree.setBackground(0, QBrush(QColor(250, 0, 0)))
                    step_flag = False
                    scen_flag = False

                if step_flag:
                    backgroundTree.setBackground(0, QBrush(QColor(0, 250, 0)))
                else:
                    backgroundTree.setBackground(0, QBrush(QColor(250, 0, 0)))

                if scen_flag:
                    self.featureTree.setBackground(0, QBrush(QColor(0, 250, 0)))
                else:
                    self.featureTree.setBackground(0, QBrush(QColor(255, 0, 0)))


        file.close()
        self.setCentralWidget(self.tree)
'''
        for i in range(10):
            main = QTreeWidgetItem(self.tree)
            main.setText(0, str(i) * 10)
            for j in range(10,20):
                QTreeWidgetItem(main).setText(0,str(j) * 10)
                QTreeWidgetItem(main).setBackground(0,QBrush(QColor(123,60,40)))
            self.tree.addTopLevelItem(main)


        # self.tree.addTopLevelItems([root, root1])

        self.setCentralWidget(self.tree)
        # super(Example, self).__init__(parent=None)
        # self.treeView = QTreeView()

        # self.treeView.setHeaderLabels(['a', 'b'])
        # self.treeView.setItemsExpandable(True)
        # item = QTreeWidgetItem(self.treeView, ['aaa'])
        # self.treeView.addTopLevelItem(item)
        # self.treeView.insertTopLevelItem(0, QTreeWidgetItem(item,['bbb']))

        # self.show()
        '''

app = QApplication(sys.argv)
te = Example()
te.show()
app.exec_()