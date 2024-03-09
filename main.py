# # 这是一个示例 Python 脚本。
#
# # 按 Shift+F10 执行或将其替换为您的代码。
# # 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#
#
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
# def o(*args,**kwargs):
#     return args,kwargs
import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
from change_img import offsetfun
from selenium import webdriver
import random
from selenium.webdriver.edge.options import Options
from selenium.webdriver import Edge
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import os  # 注意要输入OS模块

# 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
# s = offsetfun(('./img/test1.png'))
# 指定绝对路径的方式（可选）
# s = Service(r"D:\opencv_ocr\edge_deliver\msedgedriver.exe")
x1 = []
x2 = [1079, 1079, 1079, 1079, 1079, 1087, 1110, 1116, 1116, 1116, 1116, 1131, 1145, 1194, 1197, 1211, 1232, 1242, 1252, 1263, 1267, 1274, 1287, 1287, 1291, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295, 1295]
for i in x2:
    i = i - 1079
    x1.append(i)

# x3 = x1[1:]
x = [x1[i]-x1[i-1] for i in range(1,len(x1))]

y1 = [0.0, 0.2306346893310547, 0.3436410427093506, 0.45230913162231445, 0.5650358200073242, 0.6668679714202881, 0.7737655639648438, 0.8814787864685059, 0.9901237487792969, 1.0910420417785645, 1.1989777088165283, 1.306955337524414, 1.4157354831695557, 1.5241496562957764, 1.6323270797729492, 1.7405312061309814, 1.846977949142456, 1.9555964469909668, 2.0556023120880127, 2.1557300090789795, 2.2661731243133545, 2.3734076023101807, 2.4818074703216553, 2.5890185832977295, 2.690173387527466, 2.798997640609741, 2.9067461490631104, 3.007749319076538, 3.1149678230285645, 3.2222001552581787, 3.330505609512329, 3.433826446533203, 3.5418190956115723, 3.6495792865753174, 3.7496213912963867, 3.8496334552764893]
# print(x)
y = [y1[i]-y1[i-1] for i in range(1,len(y1))]
# print(y)
z1 = np.polyfit(x, y, 10)  # 用3次多项式拟合，输出系数从高到0
p1 = np.poly1d(z1)  # 使用次数合成多项式

browser = webdriver.Edge(executable_path='D:\opencv_ocr\edge_deliver\msedgedriver.exe')
filename2 = '.\selenium_img\data_no_ues'
browser.get('https://captcha1.scrape.center/')
time.sleep(3)

browser.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[3]/div/button').click()#登录
if not os.path.exists(filename2):
    os.mkdir(filename2)
def test():

    time.sleep(3)
    filename = browser.find_element(By.XPATH,
                                    '/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]').screenshot_as_png
        # print("正在获取图片({})........".format(i + 1))
    with open(filename2 + '.png', mode='wb') as f:
        f.write(filename)
    time.sleep(2)


test()
output = offsetfun((filename2 + '.png'))
time.sleep(2)
yan = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[6]/div/div[2]/a/div[2]')
yan = yan.text

chaoshi = browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[4]/div[2]')
chaoshi = chaoshi.text

while(output == None):
    chaoshi = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[4]/div[2]')
    chaoshi = chaoshi.text
    if '尝试' in chaoshi:
        browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[4]/div[3]').click()
        time.sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[6]/div/div[2]/div/a[2]').click()
    print(output,'out未获取到')
    time.sleep(3)
    test()
    output = offsetfun((filename2 + '.png'))

    # sys.exit()
else:
    print(output,'已获取')

time.sleep(3)


def get_tracks(dis):
    v = 0
    m = 0.3
    # 保存0.3内的位移
    tracks = []
    current = 0
    mid = output*4/5
    while current <= dis:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        s = v0*m+0.5*a*(m**2)
        current += s
        tracks.append(round(s))
        v = v0+a*m
    return tracks


# tracks.append(-(sum(tracks)-int(output)))


# tracks = get_tracks(output)
# print(tracks)

'''div = driver.find_element_by_id("nc_1_n1z")
ActionChains(driver).click_and_hold(on_element=div).perform()
time.sleep(0.15)
ActionChains(driver).move_to_element_with_offset(to_element=div, xoffset=30, yoffset=10).perform()
time.sleep(1)
ActionChains(driver).move_to_element_with_offset(to_element=div, xoffset=100, yoffset=20).perform()
time.sleep(0.5)
ActionChains(driver).move_to_element_with_offset(to_element=div, xoffset=200, yoffset=50).perform()'''

while(yan=='极验'):
    # ------------鼠标滑动操作------------
    # 第一步：在滑块处按住鼠标左键
    '''ActionChains(browser).click_and_hold(on_element=sli_ele).perform()
        ActionChains(browser).move_by_offset(xoffset=output, yoffset=0).perform()
        ActionChains(browser).release(on_element=sli_ele).perform()
        ActionChains(browser).perform()'''

    tracks = get_tracks(int(output) + 3)
    tracks.reverse()

    yan = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div[2]/a/div[2]')
    yan = yan.text
    sli_ele = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[2]/div[2]')
    time.sleep(2)
    print('tracks[]',tracks)
    y_pre = p1(tracks)
    ActionChains(browser).click_and_hold(on_element=sli_ele).perform()
    i = 0
    for track in tracks:
        time_random = y_pre[i]
        i += 1
        time.sleep(time_random)
        ActionChains(browser).move_by_offset(xoffset=track, yoffset=0).perform()


    # action.release(sli_ele).perform()

        # 第二步：相对鼠标当前位置进行移动
    # action.move_by_offset(output, 0)
        # 第三步：释放鼠标
    ActionChains(browser).release(on_element=sli_ele).perform()
        # 执行动作
    ActionChains(browser).perform()
else:
    print('gg')
    time.sleep(5)
    browser.close()


# time.sleep(60)
# browser.close()
# browser.close()
# 关闭浏览器
# browser.close()
# browser = webdriver.Edge(service=path)
# time.sleep(2)
# browser.get('https://www.doc88.com/')
# time.sleep(20)
# browser.close()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
