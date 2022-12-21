import cv2

image = cv2.imread('images/mnist.png', 0)

rows , cols = image.shape
#print(image.shape)

h = cols//100
w = rows//50

k = 0
m = 0
for i in range(0 ,rows, w):
    for j in range(0, cols, h):
        result = image[i:i+w, j:j+h]
        cv2.imwrite(f'output_img/numbers/{m}/{k}.jpg', result)
    
        if k == 499:
            m += 1
            k = 0
        else:
            k+=1
