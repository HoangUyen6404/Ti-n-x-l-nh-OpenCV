import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ file cục bộ (thay bằng ảnh bạn có)
img = cv2.imread(r"E:\Python\a.PNG")  # Cập nhật đường dẫn ảnh

if img is None:
    print("Không thể tải ảnh.")
    exit()

# Khởi tạo ảnh nhị phân canny
imgCanny = cv2.Canny(img, 100, 255)
plt.imshow(imgCanny)
# Tìm kiếm contours trên ảnh nhị phân từ bộ lọc canny
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)