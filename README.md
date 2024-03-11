通过高斯去噪，二值化，调用边缘检测函数，从而得到验证码缺口的方框的（x,y,w,h），也就是方框的左上角的坐标（x,y）以及它的宽和高，得到这些信息之后，就可以通过这个方框的面积还有周长，以及x的位置来判断是不是要贴合的缺口，其中由于python的内置函数contourArea(contour, oriented=None)计算面积是通过格林公式来计算的，这种微积分的计算方式应该来说是非常接近真实面积，但是却有时候会把面积算成0，所以我直接通过矩形的面积来算了，算法部分详见代码“if contour_area_min < w * h < contour_area_max and ”这一部分。
知乎链接：https://zhuanlan.zhihu.com/p/686176112
