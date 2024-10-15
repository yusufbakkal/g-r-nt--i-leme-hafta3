import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('tkagg')

# Resim yolları
image_paths = ['original/picture1.jpg', 'original/picture2.jpg', 'original/picture3.jpg']

# Gamma değeri
gam = 1.6

# Plot hazırlığı
plt.figure(figsize=(18, 12))

for i, image_path in enumerate(image_paths):
    # Resmi oku ve griye çevir
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Gamma düzeltme
    img_gamma = np.power(img / 255.0, gam) * 255.0

    # Log dönüşümü
    c = 255 / np.log(1 + np.max(img))
    log_image = c * (np.log(img + 1e-5))  # Sıfıra bölmeyi önlemek için küçük bir sabit eklenir

    # Orijinal Görüntü
    plt.subplot(3, 4, i * 4 + 1)
    plt.title(f'Original Image {i + 1}')
    plt.imshow(img, cmap='gray')

    plt.subplot(3, 4, i * 4 + 2)
    plt.title(f'Histogram - Original Image {i + 1}')
    plt.hist(img.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)

    # Gamma Düzeltilmiş Görüntü
    plt.subplot(3, 4, i * 4 + 3)
    plt.title(f'Gamma Corrected Image {i + 1}')
    plt.imshow(img_gamma, cmap='gray')

    plt.subplot(3, 4, i * 4 + 4)
    plt.title(f'Histogram - Gamma Corrected Image {i + 1}')
    plt.hist(img_gamma.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)

plt.tight_layout()
plt.show()
