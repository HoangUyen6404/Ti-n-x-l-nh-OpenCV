import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh từ file
img = cv2.imread(r"E:\Python\a.PNG")  # Đảm bảo đường dẫn đúng và ảnh tồn tại

if img is None:
    print("Không thể tải ảnh. Hãy kiểm tra lại đường dẫn hoặc tên ảnh.")
    exit()

# Hiển thị kích thước ảnh gốc
print('Origin image shape: {}'.format(img.shape))

rows, cols = img.shape[:2]

# Các điểm gốc và điểm đích
pts1 = np.float32([[50, 50], [350, 50], [50, 350], [350, 350]])
pts2 = np.float32([[0, 0], [200, 50], [50, 300], [300, 300]])

# Hiển thị các điểm ban đầu và điểm mục tiêu
print("Original points (pts1):")
print(pts1)
print("\nTarget points (pts2):")
print(pts2)

# Ma trận biến đổi phối cảnh
M = cv2.getPerspectiveTransform(pts1, pts2)
print("\nPerspective transformation matrix (M):")
print(M)

# Áp dụng phép biến đổi phối cảnh
dst = cv2.warpPerspective(img, M, (300, 300))
print("\nTransformed image shape: {}".format(dst.shape))

# Chuyển ảnh sang RGB để matplotlib hiển thị đúng màu
def to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Hiển thị ảnh gốc và các điểm ban đầu
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(to_rgb(img))
plt.title('Input Image with Original Points')
for (x, y) in pts1:
    plt.scatter(x, y, s=50, c='white', marker='x')

# Hiển thị ảnh sau biến đổi và các điểm đích
plt.subplot(122)
plt.imshow(to_rgb(dst))
plt.title('Perspective Transformed Image')
for (x, y) in pts2:
    plt.scatter(x, y, s=50, c='white', marker='x')

plt.tight_layout()
plt.show()
