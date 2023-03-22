from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPlainTextEdit
import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        self.cur_tab = 0
        self.tab_list = [{}]

        

        # Create first Tab
        self.tab_list[self.cur_tab]["tabName"] = QWidget()

        
        self.tabs.addTab(self.tab_list[self.cur_tab]["tabName"], "New Tab")

        # Add widgets to the tabs
        self.tab_list[self.cur_tab]["tabLayout"] = QVBoxLayout()

        self.tab_list[self.cur_tab]["tabEditor"] = QPlainTextEdit(self.tab_list[self.cur_tab]["tabName"])

        # Add text field
        # self.b = QPlainTextEdit(self)
        self.tab_list[self.cur_tab]["tabEditor"].insertPlainText("You can write text here.\n")
        self.tab_list[self.cur_tab]["tabEditor"].move(10,10)
        self.tab_list[self.cur_tab]["tabEditor"].resize(400,200)

        self.tab_list[self.cur_tab]["tabLayout"].addWidget(self.tab_list[self.cur_tab]["tabEditor"])
        

        # self.tab1_label = QLabel("This is tab 1")
        # self.tab1_layout.addWidget(self.tab1_label)
        # self.tab1.setLayout(self.tab1_layout)

        # self.tab2_layout = QVBoxLayout()
        # self.tab2_label = QLabel("This is tab 2")
        # self.tab2_layout.addWidget(self.tab2_label)
        # self.tab2.setLayout(self.tab2_layout)

        # self.tab3_layout = QVBoxLayout()
        # self.tab3_label = QLabel("This is tab 3")
        # self.tab3_layout.addWidget(self.tab3_label)
        # self.tab3.setLayout(self.tab3_layout)




# Create the PyQt application and show the window
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()


# import sys
# from PyQt5.Qt import QApplication, QClipboard
# from PyQt5 import QtCore, QtWidgets
# from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
# from PyQt5.QtCore import QSize

# class ExampleWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)

#         self.setMinimumSize(QSize(440, 240))    
#         self.setWindowTitle("PyQt5 Textarea example") 

#         # Add text field
#         self.b = QPlainTextEdit(self)
#         self.b.insertPlainText("You can write text here.\n")
#         self.b.move(10,10)
#         self.b.resize(400,200)

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     mainWin = ExampleWindow()
#     mainWin.show()
#     sys.exit( app.exec_() )