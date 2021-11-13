'''
Author: Meroke
Date: 2021-11-09 22:25:43
LastEditors: Meroke
LastEditTime: 2021-11-13 21:37:09
Description: file content
FilePath: \Python_pra\PYQT\test\main.py
'''
# from Ui_Window  import QtCore, QtGui, QtWidgets, Ui_MainWindow

from MyWindow import *
# from qt_material import apply_stylesheet
import qdarkstyle
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyMainForm(MainWindow)
    # ui.setupUi(MainWindow)
    # apply_stylesheet(app, theme='light_blue.xml')
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    MainWindow.show()
    sys.exit(app.exec_())