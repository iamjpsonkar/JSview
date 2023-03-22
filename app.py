from PyQt5.QtWidgets import QTabWidget, QAction, QPlainTextEdit, QPushButton
from PyQt5.Qt import QApplication
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit, QTextEdit
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
import json


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.tabs = QTabWidget()
        # self.tabs.tabsClosable()
        self.setCentralWidget(self.tabs)
        self.setWindowState(QtCore.Qt.WindowMaximized)

        
        self.cur_tab = 0
        self.tab_list = []
        self.newtabshortcut = QShortcut(QKeySequence("Ctrl+N"), self)
        self.newtabshortcut.activated.connect(self.add_new_tab)


        self.loadjsonshortcut = QShortcut(QKeySequence("Ctrl+L"), self)
        self.loadjsonshortcut.activated.connect(self.process_json)

        self.add_new_tab()
        
    def add_new_tab(self):
        self.cur_tab = len(self.tab_list)
        self.tab_list.append(QTextEdit(self))
        self.tabs.addTab(self.tab_list[self.cur_tab], "New Tab")
        self.tab_list[self.cur_tab].setAcceptRichText(True)
        self.tab_list[self.cur_tab].autoFormatting()
        

    def process_json(self):
        self.cur_tab = self.tabs.currentIndex()
        text = self.tab_list[self.cur_tab].toPlainText()
        self.tab_list[self.cur_tab].clear()
        text = json.dumps(json.loads(text), sort_keys=True, indent=4)
        self.tab_list[self.cur_tab].insertPlainText(text)



# Create the PyQt application and show the window
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()

