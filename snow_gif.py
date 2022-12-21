import cv2
import random
import imageio

image = cv2.imread('images/hiver-neige.jpg')
#image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

image_resized = cv2.resize(image, None, fx=0.50, fy=0.50)
cv2.imwrite('images/resized_img.jpg', image_resized)

rows , cols, _ = image_resized.shape

snows_list = []

for i in range(400):
    x = random.randint(-200,rows)
    y = random.randint(0,cols)
    r = random.randint(2,3)
    left_right = random.choice([-1,1])

    snow = [x,y,r,left_right]
    snows_list.append(snow)   

gravity = 4
cnt = 1
for i in range(20):
    image = cv2.imread('images/resized_img.jpg')

    for snow in snows_list:
        cv2.circle(image, (snow[1], snow[0]), snow[2], (255,255,255), -1)
        snow[0] += gravity
        snow[1] += snow[3]

    cv2.imwrite(f'output_img/snow/snow{cnt}.jpg', image)
    cnt +=1

images =[]
for i in range(1,cnt+1):
    #img = imageio.imread(f'snow{i}.jpg')
    img = cv2.imread(f'output_img/snow/snow{i}.jpg')
    images.append(img)

#showing as gif
imageio.mimsave('output_img/snow/result.gif',images)
