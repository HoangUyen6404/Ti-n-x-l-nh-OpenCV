import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
img = cv2.imread(r"E:\Python\a.PNG")
if img is None:
    print("Không thể tải ảnh.")
    exit()

# Chuyển sang RGB để matplotlib hiển thị đúng màu
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Làm mịn ảnh bằng trung bình
kernel = np.ones((5,5), np.float32) / 25
imgSmooth = cv2.filter2D(img, -1, kernel)
imgSmooth_rgb = cv2.cvtColor(imgSmooth, cv2.COLOR_BGR2RGB)

# Hiển thị ảnh
plt.subplot(121), plt.imshow(img_rgb), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(imgSmooth_rgb), plt.title('Averaging Filter')
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
