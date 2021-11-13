'''
Author: Meroke
Date: 2021-11-13 14:16:20
LastEditors: Meroke
LastEditTime: 2021-11-13 22:10:06
Description: file content
FilePath: \Python_pra\PYQT\test\MyWindow.py
'''
from numpy import SHIFT_INVALID
from Ui_Window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog,QFileDialog
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont
import os
import sys
import PicStrength
import cv2

class MyMainForm(Ui_MainWindow):
    def __init__(self,MainWindow):
        super().setupUi(MainWindow)
        ##------------------------------------------------------------##User Code Start
        self.CheckBox_Triger()
        self.init_FileBtn()
        self.init_Rota_widget()
        # Vital Enter Function
        self.Last_Generate_Button()
        self.CancleBtn.pressed.connect(self.CancleWindow)
        self.init_FilePath()
        self.init_GaussSlider()
        ##------------------------------------------------------------## User Code END

    def init_FilePath(self):
        OpenPath = 'E:/File/Picture'
        SavePath = 'E:/File/Picture/lat'
        if(not os.path.exists(OpenPath)):
            OpenPath = None
        if(not os.path.exists(SavePath)):
            SavePath = None
        self.FilePathEdit.setText(OpenPath)
        self.FilePathEdit_2.setText(SavePath)

    def init_GaussSlider(self):
        self.GaussRateSlider.setRange(0,15)
        self.GaussRateSlider.setSingleStep(1)
        self.GaussRateSlider.sliderMoved.connect(self.GaussRateSlider_Moved)

    def GaussRateSlider_Moved(self):
        value = self.GaussRateSlider.value()
        print(value)
        # self.GaussSpinBox.setValue(value*0.001)
        self.GaussRateText.setText(str(value * 0.001))
        # self.GaussRateText.setFont(QFont("Timers", 40))

    def WarningMessageBox(self,message):
        error = QMessageBox()      
        error.setWindowTitle('Warning!')
        error.setText(message)
        error.exec()
    def InfoMessageBox(self,message):
        Info = QMessageBox()
        Info.setWindowTitle("Info!")
        Info.setText(message)
        Info.exec()


    def CancleWindow(self):
        sys.exit()

    def init_Rota_widget(self):
        # limit the angle of Roate, at least generate a new pic
        self.RotaAngleSpin.setRange(0,180)

    def Last_Generate_Button(self):
        self.GenerateBtn.setCheckable(True)
        self.GenerateBtn.pressed.connect(self.GeneratePics)
    
    def ReadCheckBox(self):
        list = []
        list.append(self.RotaBtn.isChecked())
        list.append(self.MoveBtn.isChecked())
        list.append(self.GausBtn.isChecked())
        list.append(self.MirrBtn.isChecked())
        return list

    def Generate_Pics_Mult_Ways(self,stren_mode_list):
        print(stren_mode_list)
        path = self.FilePathEdit.text()
        if(not os.path.exists(path)):
            os.makedirs(path)
        else:
            file_list = os.listdir(path)
            for i in file_list:
                SinglePicPath = os.path.join(path,i)
                img = cv2.imread(SinglePicPath)
                if os.path.splitext(i)[1] == '.png' or os.path.splitext(i)[1] == '.jpg':
                    for mode in range(len(stren_mode_list)):
                        # Rotate 
                        if(stren_mode_list[mode] == True and mode == 0):
                            StepAngle = int(self.RotaAngleSpin.text())
                            if(StepAngle ==  0):
                                self.WarningMessageBox('请设置旋转步长')
                            else:
                                PicStrength.Rotate_Process(img,StepAngle,SinglePicPath)
                        # Move
                        elif(stren_mode_list[mode] == True and mode == 1):
                            PicStrength.Tranlate_Process(img, 1, SinglePicPath)
                        # Gauss    
                        elif(stren_mode_list[mode] == True and mode == 2):
                            rate = float(self.GaussRateText.text())
                            PicStrength.GasussNoise_Process(img,SinglePicPath,rate)
                        # Mirror
                        elif(stren_mode_list[mode] == True and mode == 3):
                            PicStrength.MiRROR_Process(img,1, SinglePicPath)
        return True

    def GeneratePics(self):
        flag = self.GenerateBtn.isChecked()
        if(not flag):
            # Finally Generate pics
            OpenFilePath = self.FilePathEdit.text()
            SaveFilePath = self.FilePathEdit_2.text()
            if(len(os.listdir(SaveFilePath))>0):
                pass
            if(OpenFilePath and SaveFilePath):
                PicStrength.save_path = SaveFilePath
                FinishFlag = self.Generate_Pics_Mult_Ways(self.ReadCheckBox())
                if(FinishFlag):
                    self.InfoMessageBox("数据增强完成")

            else:
                self.WarningMessageBox('缺少文件打开路径或者文件保存路径！')
                

    def init_FileBtn(self):
        self.OpenFileBtn.pressed.connect(self.OpenFileBtn_clicked)
        self.SaveFileBtn.pressed.connect(self.SaveFileBtn_clicked)
    def SaveFileBtn_clicked(self):
        cwd = os.getcwd()
        filePath = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", cwd)
        self.FilePathEdit_2.setText(filePath)
    def OpenFileBtn_clicked(self):
        cwd = os.getcwd()
        filePath = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", cwd)
        self.FilePathEdit.setText(filePath)


    def CheckBox_Triger(self):
        self.RotaBtn.stateChanged.connect(self.the_RotaBtn_was_clicked)
        self.MoveBtn.stateChanged.connect(self.the_MoveBtn_was_clicked)
        self.GausBtn.stateChanged.connect(self.the_GausBtn_was_clicked)
        self.MirrBtn.stateChanged.connect(self.the_MirrBtn_was_clicked)

    def the_RotaBtn_was_clicked(self,s):
        if(s == Qt.Checked):
            self.tabWidget.setCurrentIndex(0)
    def the_MoveBtn_was_clicked(self,s):
        if(s == Qt.Checked):
            self.tabWidget.setCurrentIndex(1)
    def the_GausBtn_was_clicked(self,s):
        if(s == Qt.Checked):
            self.tabWidget.setCurrentIndex(2)
    def the_MirrBtn_was_clicked(self,s):
        if(s == Qt.Checked):
            self.tabWidget.setCurrentIndex(3)

    