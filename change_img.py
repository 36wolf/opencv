import cv2
import numpy as np
import time
'''img = cv2.imread('./img/test.png')
B,G,R=cv2.split(img)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
H,S,V=cv2.split(hsv_img)

ret1, thres= cv2.threshold(V, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('thres', thres)

k1 = np.ones((5, 5), np.uint8)
thres = cv2.morphologyEx(thres, cv2.MORPH_OPEN, k1)  # 闭运算
cv2.imshow('MORPH_OPEN', thres)

k2 = np.ones((5, 5), np.uint8)
thres = cv2.morphologyEx(thres, cv2.MORPH_CLOSE, k2)  # 闭运算
cv2.imshow('MORPH_CLOSE', thres)

cv2.waitKey(0)'''


def offsetfun(*args):
    GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
    GAUSSIAN_BLUR_SIGMA_X = 0
    CANNY_THRESHOLD1 = 200
    CANNY_THRESHOLD2 = 420

    def get_gaussian_blur_image(image):
        return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)
    def get_canny_image(image):
        return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)
    def get_contours(image):
        contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    filepath = args[0]
    # print(type(filepath))
    image_raw = cv2.imread(filepath)

    image_height, image_width, _ = image_raw.shape
    print(image_width,image_height)
    image_gaussian_blur = get_gaussian_blur_image(image_raw)
    # cv2.imshow('gauss',image_gaussian_blur)
    image_canny = get_canny_image(image_gaussian_blur)
    # cv2.imshow('canny',image_canny)
    contours = get_contours(image_canny)
    for result in contours:
        result_1 = cv2.boundingRect(result)
        print(result_1)

        ''' 即：xyxy（左上右下） ——> xywh（中心宽高）
        xyxy（左上右下）:左上角的xy坐标和右下角的xy坐标
        xywh（中心宽高）:边界框中心点的xy坐标和图片的宽度和高度'''




    def get_contour_area_threshold(image_width, image_height):
        contour_area_min = (image_width * 0.15) * (image_height * 0.25) * 0.8
        contour_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.2
        return contour_area_min, contour_area_max


    def get_arc_length_threshold(image_width, image_height):
        arc_length_min = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 0.7
        arc_length_max = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 1.3
        return arc_length_min, arc_length_max

    def get_offset_threshold(image_width):
        offset_min = 0.2 * image_width
        offset_max = 0.9 * image_width
        return offset_min, offset_max

    '''get_contour_area_threshold：定义目标轮廓的下限和上限面积，分别为 contour_area_min 和 contour_area_max。
    get_arc_length_threshold：定义目标轮廓的下限和上限周长，分别为 arc_length_min 和 arc_length_max。
    get_offset_threshold：定义目标轮廓左侧的下限和上限偏移量，分别为 offset_min 和 offset_max。'''
    contour_area_min, contour_area_max = get_contour_area_threshold(image_width, image_height)
    arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
    offset_min, offset_max = get_offset_threshold(image_width)
    offset = None
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # print(contour_area_min,cv2.contourArea(contour),contour_area_max,cv2.arcLength(contour, True))
        # print('-----------------------------')
        # print(arc_length_min,cv2.arcLength(contour, True),arc_length_max)
        # print(offset_min , x , offset_max)
        # print(contour_area_min < w*h < contour_area_max)
        if contour_area_min < w * h < contour_area_max and \
                arc_length_min < (w + h)*2 < arc_length_max and \
                offset_min < x < offset_max:

            cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)
            x += w/2
            offset = x

    cv2.imwrite('image_label.png', image_raw)
    if offset is not None:

        offset = (offset - 31) * (260 / image_width)
    # 处理 offset 为 None 的情况，可以设置一个默认值或者采取其他操作
    return offset
# s = offsetfun(('./img/test1.png'))
# print(s)
# print('offset', offset)
#
# cv2.waitKey(0)