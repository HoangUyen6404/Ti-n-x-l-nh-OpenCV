import cv2
import matplotlib.pyplot as plt

# Đọc ảnh
img = cv2.imread(r"E:\Python\a.PNG")
if img is None:
    print("Không thể tải ảnh.")
    exit()

# Làm mờ ảnh bằng hàm blur
blur = cv2.blur(img, (5, 5))

# Chuyển ảnh sang RGB để hiển thị đúng màu với matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
blur_rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

# Hiển thị
plt.subplot(121), plt.imshow(img_rgb), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur_rgb), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()
