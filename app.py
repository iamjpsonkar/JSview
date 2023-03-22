from PyQt5.QtWidgets import QTabWidget, QAction, QPlainTextEdit, QPushButton
from PyQt5.Qt import QApplication
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit, QTextEdit
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
import json

import pickle


try:
    with open('.backup_data', 'rb+') as backup_data:
        backup = pickle.load(backup_data)
    #print("data loaded")
except:
    backup = []

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global backup
        
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

        self.loadjsonshortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.loadjsonshortcut.activated.connect(self.save_data)

        self.loadjsonshortcut = QShortcut(QKeySequence("Ctrl+K"), self)
        self.loadjsonshortcut.activated.connect(self.delete_data)

        self.loadjsonshortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        self.loadjsonshortcut.activated.connect(self.save_all)

        if len(backup) == 0:
            self.add_new_tab()
            #print("fresh start")
        else:
            for data in backup:
                #print("|",data,"|")
                if data!="" and data!=None:
                    self.add_new_tab()
                    self.tab_list[self.cur_tab].insertPlainText(data)
                    #print("New Tab")
        
    def add_new_tab(self):
        global backup
        self.cur_tab = len(self.tab_list)
        self.tab_list.append(QTextEdit(self))
        self.tabs.addTab(self.tab_list[self.cur_tab], "New Tab")
        self.tab_list[self.cur_tab].setAcceptRichText(True)
        self.tab_list[self.cur_tab].autoFormatting()
        # self.tab_list[self.cur_tab].setStyleSheet("QTextEdit {font-weight:bold;font-family:Helvetica}")
        if self.cur_tab>=len(backup):
            backup.append("")

    def process_json(self):
        global backup
        self.cur_tab = self.tabs.currentIndex()
        text = self.tab_list[self.cur_tab].toPlainText()
        self.tab_list[self.cur_tab].clear()
        text = json.dumps(json.loads(text), sort_keys=True, indent=4)
        self.tab_list[self.cur_tab].insertPlainText(text)

    def save_data(self):
        global backup
        self.cur_tab = self.tabs.currentIndex()
        if self.cur_tab < len(backup):
            backup[self.cur_tab] = self.tab_list[self.cur_tab].toPlainText()
        else:
            backup.append(self.tab_list[self.cur_tab].toPlainText())
        with open('.backup_data', 'wb+') as backup_data:
            pickle.dump(backup, backup_data)

    def delete_data(self):
        global backup
        self.cur_tab = self.tabs.currentIndex()
        try:
            backup[self.cur_tab] = ""
        except:
            pass
        with open('.backup_data', 'wb+') as backup_data:
            pickle.dump(backup, backup_data)
        

    def save_all(self):
        global backup
        backup = []
        for tab in self.tab_list:
            backup.append(tab.toPlainText())
        with open('.backup_data', 'wb+') as backup_data:
            pickle.dump(backup, backup_data)



# Create the PyQt application and show the window
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
with open('.backup_data', 'wb+') as backup_data:
    pickle.dump(backup, backup_data)
