# ⭐⭐⭐Welcome Everyone Try This Tool，

# ⭐⭐Welcome Issue

# ⭐This tool maybe better  due to your use

# 

在Windows 64位平台上，仅支持 **.png**, **.jpg**

### 使用教程:

1.首先选择打开文件路径和保存文件路径

2.然后选择增强算子，并配置右侧参数

3.选择确定生成，即可在保存文件路径中看到新生成的图片

<center align="center">
    <img src="https://i.loli.net/2021/11/15/aXzmnDrlefG2T1c.png" >
    <center>初始页面</center>
</center>


接下来，按每个算子及配置页面进行讲解。

---

## 旋转

<center>
    <img src="https://i.loli.net/2021/11/15/lRU5o9YnNkH4dbS.png" >
    <center>旋转配置页面</center>
</center>

可以看到右边有三个数字框：

1. `最小值` 表示图片旋转角度起始点，0° 表示未旋转
2. `最大值` 表示图片旋转角度的终点，360°表示旋转一周到原点
3. `旋转步长` 表示每隔 一个步长，生成旋转对应角度的图片。如果步长为60°，旋转范围为180°，则 会生成旋转 60° 120° 180°的三张照片。

<center>
    <img src="https://i.loli.net/2021/11/15/IyAlEk85GxX3Si6.png">
    <center>旋转示例</center>
</center>



---

## 位移

<center>
    <img src="https://i.loli.net/2021/11/15/4OXF7CwoQPYxuib.png">
    <center>位移配置界面</center>
</center>

位移指图片移动，实际效果如下：

<center>
    <img src="https://i.loli.net/2021/11/15/lcWbOngKv4iIB92.png">
    <center>位移示例</center>
</center>

上图为 `左移 10%` 的效果，图片向左移动了图片长的10%。同理，如果向上移动10%，则是向上移动图片宽的10%。

此处比例一般不建议超过 **30%**，容易移除主要目标。

---

## 高斯噪点

<center>
    <img src="https://i.loli.net/2021/11/15/HBqmgE6zskaT4yf.png">
    <center>高斯噪点界面</center>
</center>

此处通过滑动滑轨选择噪点百分比，此处设置了上限不超过1.6%。下图为 0.6%的效果

<center>
    <img src="https://i.loli.net/2021/11/15/e8zG9pijoCbXhTq.png">
    <center>高斯噪点示例</center>
</center>



---

## 镜像

<center>
    <img src="https://i.loli.net/2021/11/15/qye2ZEbHzCKh9UL.png">
    <center>镜像页面</center>
</center>

`水平` `垂直` `原点` 每个对称轴都会生成一张图片。通过候选框选择是否需要对应图片。

<center>
    <img src="https://i.loli.net/2021/11/15/zr8aDTwdV1KG4Jj.png">
    <center>原点镜像示例</center>
</center>



<center>
    <img src="https://i.loli.net/2021/11/15/VYU6ETlPwkG3dLD.png">
    <center>垂直镜像示例</center>
</center>

<center>
    <img src="https://i.loli.net/2021/11/15/73Ferg2nqajyxhw.png">
    <center>水平镜像示例</center>
</center>

---

## 镜像

<center>
    <img src="https://i.loli.net/2021/11/15/nPijJsQevNW8OuT.png">
    <center>亮度页面</center>
</center>

通过滑轨选择亮度更改的阈值，默认只提高亮度，如果想要同时生成亮度降低的图片，则需要选中`双向生成` 

`阈值内随机` ：在阈值内，能够随机生成指定个数的不同亮度的图片，亮度精度在0.01，如果随机亮度相同，则会发生替代，即实际生成数量可能小于指定数量。

<center>
    <img src="https://i.loli.net/2021/11/15/RbCenjvQPfF4G29.png">
    <center>暗 示例</center>
</center>

<center>
    <img src="https://i.loli.net/2021/11/15/x3SQjuR6mfoOlZM.png">
    <center>亮 示例</center>
</center>


