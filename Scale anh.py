import cv2
import numpy as np
import requests
import matplotlib.pyplot as plt

url = 'https://i.imgur.com/1vzDG2J.jpg'  # Ảnh từ Imgur

def _downloadImage(url):
    headers = {'User-Agent': 'Mozilla/5.0'}  # Giả làm trình duyệt
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        img_array = np.asarray(bytearray(resp.content), dtype="uint8")
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return img
    else:
        print(f"Lỗi tải ảnh: {resp.status_code}")
        return None

img = _downloadImage(url)

if img is None:
    print("Không thể tải ảnh. Kiểm tra lại URL hoặc kết nối mạng.")
else:
    print('origin image shape: {}'.format(img.shape))

    h, w = img.shape[:2]
    imgScale = cv2.resize(img, (int(w*2), int(h*2)), interpolation=cv2.INTER_LINEAR)
    print('scale image shape: {}'.format(imgScale.shape))

    # Chuyển BGR -> RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgScale_rgb = cv2.cvtColor(imgScale, cv2.COLOR_BGR2RGB)

    # Hiển thị ảnh
    plt.figure(figsize=(10, 5))
    plt.subplot(121), plt.imshow(img_rgb), plt.title('Origin Image')
    plt.subplot(122), plt.imshow(imgScale_rgb), plt.title('Scaled Image')
    plt.show()
