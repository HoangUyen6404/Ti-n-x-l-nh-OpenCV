import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"E:\Python\a.PNG")
if img is None:
    print("Không thể tải ảnh.")
    exit()

# Chuyển sang ảnh xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng GaussianBlur để giảm nhiễu
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Áp dụng Canny để phát hiện biên
edges = cv2.Canny(blur, 50, 150)

# Tìm contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Vẽ contours lên bản sao của ảnh gốc
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

plt.figure(figsize=(12, 5))
plt.subplot(131), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.subplot(132), plt.imshow(edges, cmap='gray'), plt.title('Edges')
plt.subplot(133), plt.imshow(cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB)), plt.title('Contours')
plt.tight_layout()
plt.show()
