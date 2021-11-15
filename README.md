# ⭐⭐⭐Welcome Everyone Try This Tool，

# ⭐⭐Welcome Issue

# ⭐This tool maybe better  due to your use

# 

在Windows 64位平台上，仅支持 **.png**, **.jpg**

### 使用教程:

1.首先选择打开文件路径和保存文件路径

2.然后选择增强算子，并配置右侧参数

3.选择确定生成，即可在保存文件路径中看到新生成的图片

![image-20211115204721947](https://i.loli.net/2021/11/15/aXzmnDrlefG2T1c.png)

接下来，按每个算子及配置页面进行讲解。

---

## 旋转

![image-20211115204910757](https://i.loli.net/2021/11/15/lRU5o9YnNkH4dbS.png)

可以看到右边有三个数字框：

1. `最小值` 表示图片旋转角度起始点，0° 表示未旋转
2. `最大值` 表示图片旋转角度的终点，360°表示旋转一周到原点
3. `旋转步长` 表示每隔 一个步长，生成旋转对应角度的图片。如果步长为60°，旋转范围为180°，则 会生成旋转 60° 120° 180°的三张照片。

![1_Rota60](https://i.loli.net/2021/11/15/IyAlEk85GxX3Si6.png)

---

## 位移

![image-20211115205339794](C:/Users/Meroke/AppData/Roaming/Typora/typora-user-images/image-20211115205339794.png)

位移指图片移动，实际效果如下：

![1_Tran1_30](https://i.loli.net/2021/11/15/lcWbOngKv4iIB92.png)

上图为 `左移 10%` 的效果，图片向左移动了图片长的10%。同理，如果向上移动10%，则是向上移动图片宽的10%。

此处比例一般不建议超过 **30%**，容易移除主要目标。

---

## 高斯噪点

![image-20211115205951537](https://i.loli.net/2021/11/15/HBqmgE6zskaT4yf.png)

此处通过滑动滑轨选择噪点百分比，此处设置了上限不超过1.6%。下图为 0.6%的效果

![1_Gasu0.006](https://i.loli.net/2021/11/15/e8zG9pijoCbXhTq.png)

---

## 镜像

![image-20211115210250506](https://i.loli.net/2021/11/15/qye2ZEbHzCKh9UL.png)

`水平` `垂直` `原点` 每个对称轴都会生成一张图片。通过候选框选择是否需要对应图片。



![1_Mirr-1](https://i.loli.net/2021/11/15/zr8aDTwdV1KG4Jj.png)

​                                                                                                          原点

![1_Mirr0](https://i.loli.net/2021/11/15/VYU6ETlPwkG3dLD.png)

​                                                                                                         垂直

![1_Mirr1](https://i.loli.net/2021/11/15/73Ferg2nqajyxhw.png)

​                                                                                                        水平

---

## 镜像

![image-20211115210656326](https://i.loli.net/2021/11/15/lhmKryRHY1IGM7B.png)

通过滑轨选择亮度更改的阈值，默认只提高亮度，如果想要同时生成亮度降低的图片，则需要选中`双向生成` 

`阈值内随机` ：在阈值内，能够随机生成指定个数的不同亮度的图片，亮度精度在0.01，如果随机亮度相同，则会发生替代，即实际生成数量可能小于指定数量。



![1_Brig0.7](../../../../../../File/Picture/lat/1_Brig0.7.png)

![1_Brig1.3](../../../../../../File/Picture/lat/1_Brig1.3.png)

