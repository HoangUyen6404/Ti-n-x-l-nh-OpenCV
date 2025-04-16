import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"E:\Python\a.PNG")  # Đảm bảo đường dẫn đúng và ảnh tồn tại

if img is None:
    print("Không thể tải ảnh. Hãy kiểm tra lại đường dẫn hoặc tên ảnh.")
    exit()

print('Origin image shape: {}'.format(img.shape))
rows, cols = img.shape[:2]
rows, cols, ch = img.shape

# Các điểm gốc
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
print(f"Points in the original image (pts1): {pts1}")

# Các điểm mục tiêu (sau biến đổi)
pts2 = np.float32([[50, 300], [200, 150], [150, 400]])
print(f"Points in the output image (pts2): {pts2}")

M = cv2.getAffineTransform(pts1, pts2)
print(f"Affine transformation matrix (M):\n{M}")

imageAffine = cv2.warpAffine(img, M, (cols, rows))

# Hiển thị các thông tin bổ sung sau khi biến đổi
print(f"Shape of the transformed image: {imageAffine.shape}")

# Hàm chuyển đổi ảnh từ BGR sang RGB để matplotlib hiển thị đúng
def to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Hiển thị hình ảnh gốc và các điểm ban đầu
plt.subplot(121)
plt.imshow(to_rgb(img))  # Hiển thị ảnh gốc sau khi chuyển sang RGB
plt.title('Input')
for (x, y) in pts1:
    plt.scatter(x, y, s=50, c='white', marker='x')

# Hiển thị hình ảnh sau biến đổi affine và các điểm mục tiêu
plt.subplot(122)
plt.imshow(to_rgb(imageAffine))
plt.title('Output')
for (x, y) in pts2:
    plt.scatter(x, y, s=50, c='white', marker='x')

plt.tight_layout()
plt.show()
