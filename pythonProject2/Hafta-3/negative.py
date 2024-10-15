import cv2


img_1 = cv2.imread('picture1.jpg')
img_2 = cv2.imread('picture2.jpg')
img_3 = cv2.imread('picture3.jpg')

negative_image_1 = 255 - img_1
negative_image_2 = 255 - img_2
negative_image_3 = 255 - img_3

# 1.Foto için
cv2.imwrite('picture1.jpg',negative_image_1)
cv2.imshow("1.Goruntunun Negatifi", negative_image_1)

# 2.Foto için
cv2.imwrite('picture2.jpg',negative_image_2)
cv2.imshow("2.Goruntunun Negatifi", negative_image_2)

# 3.Foto için
cv2.imwrite('picture3.jpg',negative_image_3)
cv2.imshow("3.Goruntunun Negatifi", negative_image_3)

cv2.waitKey(0)

cv2.destroyAllWindows()