import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"E:\Python\a.PNG")  # Đảm bảo đường dẫn đúng và ảnh tồn tại

if img is None:
    print("Không thể tải ảnh. Hãy kiểm tra lại đường dẫn hoặc tên ảnh.")
    exit()

print('Origin image shape: {}'.format(img.shape))
rows, cols = img.shape[:2]

# Các ma trận dịch chuyển
tx, ty = 200, 200
M1 = np.float32([[1, 0, tx],  [0, 1, ty]])    # Dịch xuống góc dưới bên phải
M2 = np.float32([[1, 0, -tx], [0, 1, ty]])    # Dịch xuống góc dưới bên trái
M3 = np.float32([[1, 0, tx],  [0, 1, -ty]])   # Dịch lên góc trên bên phải
M4 = np.float32([[1, 0, -tx], [0, 1, -ty]])   # Dịch lên góc trên bên trái

# Áp dụng dịch chuyển
tran1 = cv2.warpAffine(img, M1, (cols, rows))
tran2 = cv2.warpAffine(img, M2, (cols, rows))
tran3 = cv2.warpAffine(img, M3, (cols, rows))
tran4 = cv2.warpAffine(img, M4, (cols, rows))

# Xoay ảnh kích thước 45 độ tại tâm của ảnh, độ phóng đại ảnh không đổi
M5 = cv2.getRotationMatrix2D(center = (cols/2, rows/2), angle=-45, scale=1)
tran5 = cv2.warpAffine(img, M5, (cols, rows))

# Xoay ảnh kích thước 45 độ tại tâm của ảnh và độ phóng đại giảm 1/2
M6 = cv2.getRotationMatrix2D(center = (cols/2, rows/2), angle=-45, scale=0.5)
tran6 = cv2.warpAffine(img, M6, (cols, rows))

# Xoay ảnh kích thước -45 độ tại tâm của ảnh
M7 = cv2.getRotationMatrix2D(center = (cols/2, rows/2), angle=45, scale=1)
tran7 = cv2.warpAffine(img, M7, (cols, rows))

# Xoay ảnh kích thước 20 độ tại góc trên bên trái
M8 = cv2.getRotationMatrix2D(center = (0, 0), angle=-20, scale=1)
tran8 = cv2.warpAffine(img, M8, (cols, rows))

# Xoay ảnh kích thước 20 độ tại góc dưới bên phải
M9 = cv2.getRotationMatrix2D(center = (cols, rows), angle=-20, scale=1)
tran9 = cv2.warpAffine(img, M9, (cols, rows))

# Hàm chuyển đổi ảnh từ BGR sang RGB để matplotlib hiển thị đúng
def to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Hiển thị ảnh
plt.figure(figsize=(18, 8))
plt.subplot(231), plt.imshow(to_rgb(img)), plt.title('Original')
plt.subplot(232), plt.imshow(to_rgb(tran5)), plt.title('Rotate 45 at centroid')
plt.subplot(233), plt.imshow(to_rgb(tran6)), plt.title('Rotate 45 resize 0.5')
plt.subplot(234), plt.imshow(to_rgb(tran7)), plt.title('Rotate -45 at centroid')
plt.subplot(235), plt.imshow(to_rgb(tran8)), plt.title('Rotate 20 at upper left corner')
plt.subplot(236), plt.imshow(to_rgb(tran9)), plt.title('Rotate 20 at bottom right corner')
plt.tight_layout()
plt.show()
