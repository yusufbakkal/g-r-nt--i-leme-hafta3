import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntü dosyası yolları
image_paths = [
    'original/picture1.jpg',  # 1. resim
    'original/picture2.jpg',  # 2. resim
    'original/picture3.jpg'   # 3. resim
]

plt.figure(figsize=(18, 12))

for i, image_path in enumerate(image_paths):
    # Resmi oku ve gri tonlamaya çevir
    img = cv2.imread(image_path)

    if img is None:
        print(f"Unable to load image: {image_path}")
        continue  # Eğer resim yüklenemiyorsa, döngüden çık

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Histogram germe (kontrast artırma)
    img_stretched = cv2.normalize(img_gray, None, 0, 255, cv2.NORM_MINMAX)

    # Orijinal Görüntü ve Histogram
    plt.subplot(3, 4, i * 4 + 1)
    plt.title(f'Original Image {i + 1}')
    plt.imshow(img_gray, cmap='gray')
    plt.axis('off')  # Eksenleri gizle

    plt.subplot(3, 4, i * 4 + 2)
    plt.title(f'Histogram - Original Image {i + 1}')
    plt.hist(img_gray.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)

    # Histogram Gerilmiş Görüntü
    plt.subplot(3, 4, i * 4 + 3)
    plt.title(f'Stretched Image {i + 1}')
    plt.imshow(img_stretched, cmap='gray')
    plt.axis('off')  # Eksenleri gizle

    plt.subplot(3, 4, i * 4 + 4)
    plt.title(f'Histogram - Stretched Image {i + 1}')
    plt.hist(img_stretched.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)

plt.tight_layout()
plt.show()
