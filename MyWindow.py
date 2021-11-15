'''
Author: Meroke
Date: 2021-11-13 14:16:20
LastEditors: Meroke
LastEditTime: 2021-11-15 15:12:45
Description: file content
FilePath: \Python_pra\PYQT\DataEnhancementTool\MyWindow.py
'''
# from PYQT.DataEnhancementTool.PicStrength import Brightness_Process
from Ui_Window import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QFileDialog
#,QInputDialog,QApplication, QMainWindow 
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont
import os
import sys
import PicStrength
import cv2

class MyMainForm(Ui_MainWindow):
    def __init__(self,MainWindow):
        super().setupUi(MainWindow)
        MainWindow.setWindowTitle("数据增强工具")
        ##------------------------------------------------------------##User Code Start
        self.CheckBox_Triger()
        self.init_FileBtn()
        self.init_Rotate_Configure()
        # Vital Enter Function
        self.Last_Generate_Button()
        self.CancleBtn.pressed.connect(self.CancleWindow)
        self.init_FilePath()
        self.init_GaussSlider_Confgure()
        self.init_Move_Configure()
        self.init_Mirror_Configure()
        self.init_Bright_Configure()
        ##------------------------------------------------------------## User Code END
    '''
    各类模块的初始化，并连接槽函数
    '''
    def init_Bright_Configure(self):
        self.BrightRateSlider.setValue(2)
        self.BrightRateSlider.setRange(0,5)
        self.BrightRateSlider.valueChanged.connect(self.BrightRateSlider_Moved)
        self.BrightRateText.setText('0.2')
        self.BrightRandomBtn.stateChanged.connect(self.BrightRandomBtn_StateChanged)
        if(not self.BrightRandomBtn.isChecked()):
            self.BrightRandomNumLine.setEnabled(False)
    def BrightRandomBtn_StateChanged(self):
        if(self.BrightRandomBtn.isChecked()):
            self.BrightRandomNumLine.setEnabled(True)
        else:
            self.BrightRandomNumLine.setEnabled(False)

    def BrightRateSlider_Moved(self):
        value = str(self.BrightRateSlider.value() / 10)
        self.BrightRateText.setText(value)

    def Read_Bright_Configure(self):
        list = []
        list.append(self.BrightRateSlider.value()/10)
        list.append(self.BrightTwoWayBtn.isChecked())
        list.append(int(self.BrightRandomNumLine.text()))
        return list

    def init_Mirror_Configure(self):
        self.HorizontalCheckBox.setChecked(True)
        self.VerticalCheckBox.setChecked(True)
        self.OriginCheckBox.setChecked(True)

    def Read_Mirror_Configure(self):
        list = []
        list.append(self.OriginCheckBox.isChecked())
        list.append(self.VerticalCheckBox.isChecked())
        list.append(self.HorizontalCheckBox.isChecked())
        return list
        
    def init_Move_Configure(self):
        self.Move_Conf_Up.setText(str(20))
        self.Move_Conf_Down.setText(str(20))
        self.Move_Conf_Left.setText(str(20))
        self.Move_Conf_Right.setText(str(20))
    def Read_Move_Configure(self):
        list = []
        list.append(int(self.Move_Conf_Up.text()))
        list.append(int(self.Move_Conf_Down.text()))
        list.append(int(self.Move_Conf_Left.text()))
        list.append(int(self.Move_Conf_Right.text()))
        return list

    def init_FilePath(self):
        OpenPath = 'E:/File/Picture'
        SavePath = 'E:/File/Picture/lat'
        if(not os.path.exists(OpenPath)):
            OpenPath = None
        if(not os.path.exists(SavePath)):
            SavePath = None
        self.FilePathEdit.setText(OpenPath)
        self.FilePathEdit_2.setText(SavePath)

    def init_GaussSlider_Confgure(self):
        self.GaussRateSlider.setRange(0,16)
        self.GaussRateSlider.setSingleStep(1)
        # self.GaussRateSlider.sliderMoved.connect(self.GaussRateSlider_Moved)
        self.GaussRateSlider.setValue(6)
        self.GaussRateText.setText(str(0.6))
        self.GaussRateSlider.valueChanged.connect(self.GaussRateSlider_Moved)
    def GaussRateSlider_Moved(self):
        value = self.GaussRateSlider.value()
        self.GaussRateText.setText(str(value/10 ))
        # self.GaussRateText.setFont(QFont("Timers", 40))

        

    '''
    MessageBox
    对话框初始化，目前使用两种，警告Warn，提示Info
    警告Warn 提供返回值确定
    '''
    def WarningMessageBox(self,message):
        error = QMessageBox()      
        error.setWindowTitle('Warning!')
        error.setText(message)
        Qyes = error.addButton(('确定'),QMessageBox.YesRole)
        Qno = error.addButton(('取消'),QMessageBox.NoRole)
        error.exec()
        return error.clickedButton() == Qyes

    def InfoMessageBox(self,message):
        Info = QMessageBox()
        Info.setWindowTitle("Info!")
        Info.setText(message)
        Info.exec()


    def CancleWindow(self):
        sys.exit()

    def init_Rotate_Configure(self):
        # limit the angle of Roate, at least generate a new pic
        self.AngleMin.setText('0')
        self.AngleMax.setText('360')
        self.RotaAngleSpin.setRange(0,180)
        self.RotaAngleSpin.setValue(60)

    def Read_Rotate_Configure(self):
        list = []
        list.append(int(self.AngleMin.text()))
        list.append(int(self.AngleMax.text()))
        list.append(int(self.RotaAngleSpin.text()))
        return list

    def Last_Generate_Button(self):
        self.GenerateBtn.setCheckable(True)
        self.GenerateBtn.pressed.connect(self.GeneratePics)

    '''
    读取用户所选择的算子
    '''
    def Read_UserSelection(self):
        list = []
        list.append(self.RotaBtn.isChecked())
        list.append(self.MoveBtn.isChecked())
        list.append(self.GausBtn.isChecked())
        list.append(self.MirrBtn.isChecked())
        list.append(self.BrightBtn.isChecked())
        return list

        
    '''
    数据增强 主要执行函数 
    Generate_Pics_Mult_Ways()
    para: stren_mode_list 返回所有算子的用户选择情况 默认[0,0,0,0]
    '''
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
                            Angle_Configure = self.Read_Rotate_Configure()
                            if(Angle_Configure[2] ==  0):
                                self.WarningMessageBox('旋转图片生成失败，请设置旋转步长')
                            else:
                                PicStrength.Rotate_Process(img,Angle_Configure,SinglePicPath)
                        # Move
                        elif(stren_mode_list[mode] == True and mode == 1):
                            Move_Configure_List = self.Read_Move_Configure()
                            PicStrength.Tranlate_Process(img, Move_Configure_List, SinglePicPath)
                        # Gauss    
                        elif(stren_mode_list[mode] == True and mode == 2):
                            rate = float(self.GaussRateText.text())
                            PicStrength.GasussNoise_Process(img,SinglePicPath,rate)
                        # Mirror
                        elif(stren_mode_list[mode] == True and mode == 3):
                            Mirror_Configure_List =self.Read_Mirror_Configure()
                            PicStrength.MiRROR_Process(img,Mirror_Configure_List, SinglePicPath)
                        # Bright
                        elif(stren_mode_list[mode] == True and mode == 4):
                            Bright_Configure_list = self.Read_Bright_Configure()
                            PicStrength.Brightness_Process(img,Bright_Configure_list, SinglePicPath)
                        
        return True


    '''
    数据增强 用户入口 触发函数
    '''
    def GeneratePics(self):
        flag = self.GenerateBtn.isChecked()
        if(not flag):
            # Finally Generate pics
            OpenFilePath = self.FilePathEdit.text()
            SaveFilePath = self.FilePathEdit_2.text()

            if(OpenFilePath and SaveFilePath):
                if(len(os.listdir(SaveFilePath))>0):
                    User_Selection = self.WarningMessageBox("保存文件夹内已存在文件，可能会导致重名覆盖，请问确认继续吗")
                    if(not User_Selection):
                        return
                PicStrength.save_path = SaveFilePath
                FinishFlag = self.Generate_Pics_Mult_Ways(self.Read_UserSelection())
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

    