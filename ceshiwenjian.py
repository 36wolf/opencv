
import cv2

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 250
CANNY_THRESHOLD2 = 450
def get_gaussian_blur_image(image):
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)


def get_canny_image(image):
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)


def get_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours

filepath = 'D:/opencv_ocr/img/test1.png'
image_raw = cv2.imread(filepath)
image_height, image_width, _ = image_raw.shape
print(image_width, image_height)
image_gaussian_blur = get_gaussian_blur_image(image_raw)
cv2.imshow('gauss',image_gaussian_blur)
image_canny = get_canny_image(image_gaussian_blur)
cv2.imshow('canny',image_canny)
contours = get_contours(image_canny)
# for result in contours:
#     result_1 = cv2.boundingRect(result)
#     print(result_1)
ip = 1
for contour in contours:

    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)
    print(f'第{ip}个框, ',x,y,w,h)
    cv2.imwrite(f'.\imgtset\image_label{ip}.png', image_raw)
    ip += 1
cv2.waitKey(0)




