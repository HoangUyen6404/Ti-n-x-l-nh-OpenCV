import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"E:\Python\a.PNG")  # Đảm bảo đường dẫn đúng và ảnh tồn tại

if img is None:
    print("Không thể tải ảnh. Hãy kiểm tra lại đường dẫn hoặc tên ảnh.")
    exit()

print('Origin image shape: {}'.format(img.shape))
rows, cols = img.shape[:2]

tx, ty = 200, 200
M1 = np.float32([[1, 0, tx],  [0, 1, ty]])    # Dịch xuống góc dưới bên phải
M2 = np.float32([[1, 0, -tx], [0, 1, ty]])    # Dịch xuống góc dưới bên trái
M3 = np.float32([[1, 0, tx],  [0, 1, -ty]])   # Dịch lên góc trên bên phải
M4 = np.float32([[1, 0, -tx], [0, 1, -ty]])   # Dịch lên góc trên bên trái

tran1 = cv2.warpAffine(img, M1, (cols, rows))
tran2 = cv2.warpAffine(img, M2, (cols, rows))
tran3 = cv2.warpAffine(img, M3, (cols, rows))
tran4 = cv2.warpAffine(img, M4, (cols, rows))

def to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(18, 5))
plt.subplot(151), plt.imshow(to_rgb(img)), plt.title('Original')
plt.subplot(152), plt.imshow(to_rgb(tran1)), plt.title('Bottom Right')
plt.subplot(153), plt.imshow(to_rgb(tran2)), plt.title('Bottom Left')
plt.subplot(154), plt.imshow(to_rgb(tran3)), plt.title('Top Right')
plt.subplot(155), plt.imshow(to_rgb(tran4)), plt.title('Top Left')
plt.tight_layout()
plt.show()
