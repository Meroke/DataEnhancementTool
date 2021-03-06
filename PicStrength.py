import cv2
import numpy as np
# import math
import random
import os

'''
图片处理四个阶段： img, dst, Ongoing, result
'''
save_path =''

'''
show(img) 显示图片
'''
def show(img):
    if img is None:
        return
    cv2.imshow('img_test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


'''
图像位移：
    [1,0,tx]  tx:水平上的移动
    [0,1,ty]  ty:垂直上的移动
'''
def Translate(img, tx=0, ty=0):

    M = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
    # 仿射变换，para: img(原图), M(变换矩阵), (shape[1],shape[0]) (输出图片大小)
    dst = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
    return dst


'''
图像旋转：
    旋转角度超过45°，略微缩小图像
'''
def Rotate(img, angle=0):
    rows, cols = img.shape[:2]
    # print(rows,cols)
    rate = 1
    if (45 < angle < 135 and angle != 180) or (270 < angle < 315):
        rate = 0.8
    # cv2.getRotationMatrix2D   para: 旋转中心，旋转角度，旋转后图像的缩放比例
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, rate)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst


'''
图片镜像：
    axis = -1, 原点镜像
           0, 垂直镜像
           1, 水平镜像
           
'''
def Mirror(img, axis=1):
    dst = cv2.flip(img, axis)
    return dst


'''
高斯噪声:
    mean : 均值，抵消部分方差效果
    var : 方差，彩色噪点
'''
def GasussNoise(img, mean=0, var=0.001):
    image = np.array(img / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    dst = np.uint8(out * 255)
    return dst


'''
亮度与对比度:
    rate: 原图的占据的比例，>1 亮， <1 暗
    g: 图像偏移量=0
'''
def Contrast_Brightness(img, rate=1.0, g=0):
    h, w, ch = img.shape  # 获取shape的数值，height和width、通道
    # 新建全零图片数组src2,将height和width，类型设置为原图片的通道类型(色素全为零，输出为全黑图片)
    src2 = np.zeros([h, w, ch], img.dtype)
    # addWeighted函数说明:计算两个图像阵列的加权和
    dst = cv2.addWeighted(img, rate, src2, 1 - rate, g)
    return dst



def saveImage(img, file_path, suffix):
    file_name = file_path.split('\\')[-1].split('.')[0]
    global save_path
    save_name = os.path.join(save_path, file_name + '_{}.png'.format(suffix))
    cv2.imwrite(save_name, img)


def Tranlate_Process(img, Tran_List, file_path):
    Ongoing = None

    for i in range(len(Tran_List)):
        Tran_List[i] = Tran_List[i] / 100
        # move_dis = 50
        if i == 0:
            move_dis = int(Tran_List[i] * img.shape[0])
            Ongoing = Translate(img, move_dis, 0)
        elif i == 1:
            move_dis = int(Tran_List[i] * img.shape[0])
            Ongoing = Translate(img, move_dis*-1, 0)
        elif i == 2:
            move_dis = int(Tran_List[i] * img.shape[1])
            Ongoing = Translate(img, 0, move_dis*-1)
        elif i == 3:
            move_dis = int(Tran_List[i] * img.shape[1])
            Ongoing = Translate(img, 0, move_dis)
        
        # if i < 2:  # 0=positive,1=negative
        #     if i == 1:
        #         move_dis *= -1
        #     Ongoing = Translate(img, move_dis, 0)
        # else:  # i = 2 or 3, 2=positive,3=negative
        #     if i == 3:
        #         move_dis *= -1
        #     Ongoing = Translate(img, 0, move_dis)
        print(move_dis)
        if Ongoing is not None:
            saveImage(Ongoing, file_path, 'Tran{}_'.format(i) + str(abs(move_dis)))

    return Ongoing


def Rotate_Process(img, Rota_list, file_path):
    # split_period = Rota * 30
    split_period = Rota_list[2]
    if(split_period < 1):
        Ongoing = img
    else:
        for angle in range(Rota_list[0], Rota_list[1], split_period):
            Ongoing = Rotate(img, angle)
            saveImage(Ongoing, file_path, 'Rota' + str(angle))
    return Ongoing

def MiRROR_Process(img, Configure_list, file_path):
    axis_list = [-1,0,1]
    for i in range(len(Configure_list)):
        Ongoing = None
        if Configure_list[i] and i == 0 :
            Ongoing = Mirror(img,axis_list[i])
        elif Configure_list[i] and i == 1:
            Ongoing = Mirror(img,axis_list[i])
        elif Configure_list[i] and i == 2:
            Ongoing = Mirror(img,axis_list[i])
        if(Ongoing is not None):
            saveImage(Ongoing, file_path , 'Mirr' + str(axis_list[i]))
    return Ongoing

def GasussNoise_Process(img,file_path,rate=0.001):
    Ongoing =None
    if(rate >= 0.01):
        rate /= 100
    Ongoing = GasussNoise(img,var=rate)
    saveImage(Ongoing, file_path, 'Gasu' + str(rate))
    return Ongoing


def Brightness_Process(img,Bright_list,file_path):
    Ongoing = None
    Difference_Rate, ret , RandomNum= Bright_list
    # for i in np.arange(0.8,1.4,0.4):
    ActualRate = Difference_Rate + 1
    Ongoing = Contrast_Brightness(img,ActualRate)
    saveImage(Ongoing,file_path,'Brig' + str(ActualRate))
    if ret:
        ActualRate = Difference_Rate*(-1) +1
        Ongoing = Contrast_Brightness(img,ActualRate)
        saveImage(Ongoing,file_path,'Brig' + str(ActualRate))
    if RandomNum !=None and RandomNum > 0:
        MaxValue = Difference_Rate + 1
        if ret:
            MinValue = Difference_Rate* (-1) + 1
        else:
            MinValue = 1
        for i in range(RandomNum):
            ActualRate = round(random.uniform(MinValue,MaxValue),2)
            Ongoing = Contrast_Brightness(img,ActualRate)
            saveImage(Ongoing,file_path,'Brig' + 'extr'+str(ActualRate))

    return Ongoing



# class Random_Reinforcement:
#     def __init__(self):
#         self.IsTranslate = -1
#         self.IsRotate = -1
#         self.IsMirror = -1
#         self.IsGasussNoise = -1
#         self.IsContrast_Brightness = -1
#         self.ModeList = []
#         self.ModeListAppend = self.ModeList.append

#     def Random_Rein(self):
#         self.IsTranslate = random.randint(1, 1)
#         self.IsRotate = random.randint(1, 3)
#         self.IsMirror = random.randint(1, 2)
#         self.IsGasussNoise = random.randint(1, 1)
#         self.IsContrast_Brightness = random.randint(1, 2)
#         self.flash_list()

#     def flash_list(self):
#         self.ModeList.clear()
#         self.ModeListAppend(self.IsTranslate)  # 0
#         self.ModeListAppend(self.IsRotate)  # 1
#         self.ModeListAppend(self.IsMirror)  # 2
#         self.ModeListAppend(self.IsGasussNoise)  # 3
#         self.ModeListAppend(self.IsContrast_Brightness)  # 4
# def Process_Mode01(file_path, master):
#     img = cv2.imread(file_path)
#     Tran = master.ModeList[0]
#     Rota = master.ModeList[1]
#     Mirr = master.ModeList[2]
#     Gasu = master.ModeList[3]
#     CoBr = master.ModeList[4]
#     result = img
#     # if Tran is not 0:
#     #     result = Tranlate_Process(img, Tran, file_path)
#     if Rota is not 0:
#         result = Rotate_Process(img, 1, file_path)
#     # if Mirr is not 0:
#     #     result = MiRROR_Process(img,Mirr,file_path)
#     if Gasu is not 0:
#         result = GasussNoise_Process(img,file_path)
#     if CoBr is not 0:
#         result = Brightness_Process(img,file_path)


# def Process_Mult_Pics(path, mode=0):
#     global save_path
#     save_path = os.path.join(path, 'NewFrom')
#     if not os.path.exists(save_path):

#         os.makedirs(save_path)
#     # mode init
#     Rein_Ways = Random_Reinforcement()
#     Rein_Ways.Random_Rein()

#     FileList = os.listdir(path)
#     if mode is 0:
#         for i in FileList:
#             if os.path.splitext(i)[1] == '.png':
#                 # print(os.path.join(path, i))
#                 file = os.path.join(path, i)
#                 # print(file.split('\\')[-1])
#                 Process_Mode01(file, Rein_Ways)


# if __name__ is "__main__":
#     # img = cv2.imread("C:\\Users\\Meroke\\Pictures\\3.png")
#     # result = Contrast_Brightness(img)
#     # show(result)
#     # path = 'E:\\File\\Picture'
#     path='E:\\Program\\Code\python\\Python_pra\\result'
#     Process_Mult_Pics(path)
