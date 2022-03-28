import cv2
import numpy as np
print(cv2.__version__)

img = cv2.imread("Siddharth_P\Q4\coin&pencil.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
canny = cv2.Canny(imgGray, 200, 200)
blur = cv2.GaussianBlur(canny, (5,5), 0)
detected_circles = cv2.HoughCircles(blur, 
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
               param2 = 30, minRadius = 1, maxRadius = 40)
j = 0
lst = []

# Detecting circles and adding its data to list
if detected_circles is not None:
  
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
  
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
        lst.append((a,b))
        j+=1
print(lst)
# cv2.imshow("Detected Circle", img)
# cv2.waitKey(0)
i = 0

# Finding all contours
cnt, hierarchy = cv2.findContours(blur.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(type(detected_circles))
for c in cnt:
    area = cv2.contourArea(c)
    # Conditions specifically for pen
    if area>7000 and (area<8200) or (area>8250)  and c not in detected_circles:
        print(cv2.pointPolygonTest(c, (a,b), False))
        cv2.drawContours(img, c, -1, (0,0,255), 3)
        i+=1
coins = f"Coins: {j}"
pens = f"Pens: {i}"
# Text
cv2.putText(img,text=coins, org=(30, 100),color=(0,255,0), fontFace=cv2.LINE_AA, fontScale=1.5)
cv2.putText(img,text=pens, org=(30, 150), color=(0,0,255), fontFace=cv2.LINE_AA, fontScale=1.5)

cv2.imshow("output", img)
cv2.waitKey(0)
