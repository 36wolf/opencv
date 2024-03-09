import pyautogui
import pynput
import keyboard
import time
# 创建一个空列表，用于保存鼠标轨迹
mouse_positions = []
x_time = []
a = int(input('输入1开始: '))
while a == 1:
    time.sleep(5)
    print('记录开始')
    # 循环记录鼠标位置
    qishi = time.time()
    while True:
        # 获取当前鼠标的位置
        position = pyautogui.position()
        mid = time.time()
        indi = mid - qishi
        x_time.append(indi)
        # 将鼠标位置添加到列表中
        mouse_positions.append(position)
        # 暂停一段时间，避免记录过于频繁
        # pyautogui.sleep(0.1)
        # 按下 'q' 键退出循环
        if keyboard.is_pressed('q'):
            break

    # 打印鼠标轨迹
    # print(mouse_positions)
    # print(type(mouse_positions))

    y_distance = []
    for position in mouse_positions:
        y_distance.append(position.x)
    with open('distance.txt','w') as f:
        for i in range(len(y_distance)):
            f.write(str(y_distance[i])+ '\n')
    with open('time.txt','w') as f:
        for i in range(len(x_time)):
            f.write(str(x_time[i])+ '\n')
    print(y_distance)
    # print(x_time)


        # print(type(position))

