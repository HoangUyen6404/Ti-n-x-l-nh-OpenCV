import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"E:\Python\a.PNG")

if img is None:
    print("Không thể tải ảnh.")
    exit()

# Chuyển ảnh sang thang độ xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng bộ lọc Gaussian Blur để làm mịn trước khi Canny
blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)

# Áp dụng phép dò biên Canny
edges = cv2.Canny(blurred, 100, 200)

# Hiển thị kết quả
plt.figure(figsize=(12, 5))
plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(132), plt.imshow(gray, cmap='gray'), plt.title('Grayscale')
plt.subplot(133), plt.imshow(edges, cmap='gray'), plt.title('Canny Edge Detection')
plt.tight_layout()
plt.show()
