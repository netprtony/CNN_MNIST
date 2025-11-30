# 🧠 CNN MNIST Classifier

Mô hình **Convolutional Neural Network (CNN)** để nhận dạng chữ số viết tay sử dụng bộ dữ liệu MNIST.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red?style=for-the-badge&logo=keras&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## 📋 Mô tả dự án

Dự án xây dựng mô hình CNN để phân loại chữ số viết tay (0-9) với độ chính xác cao trên bộ dữ liệu MNIST gồm 70,000 ảnh.

## 🛠️ Công nghệ sử dụng

| Công nghệ | Mô tả |
|-----------|-------|
| **TensorFlow 2.x** | Framework Deep Learning chính |
| **Keras** | High-level API để xây dựng mô hình |
| **NumPy** | Xử lý mảng và tính toán số học |
| **Matplotlib** | Trực quan hóa dữ liệu và kết quả |
| **Google Colab** | Môi trường huấn luyện với GPU miễn phí |

## 🏗️ Kiến trúc mô hình

```
Input (28x28x1)
    │
    ▼
Conv2D (32 filters, 3x3) + ReLU
    │
    ▼
MaxPooling2D (2x2)
    │
    ▼
Conv2D (64 filters, 3x3) + ReLU
    │
    ▼
MaxPooling2D (2x2)
    │
    ▼
Conv2D (64 filters, 3x3) + ReLU
    │
    ▼
Flatten
    │
    ▼
Dense (64 units) + ReLU
    │
    ▼
Dense (10 units) + Softmax
    │
    ▼
Output (10 classes)
```
## Biểu đồ độ chính xác và mất mát
![alt text](image.png)
## 📊 Kết quả

- **Độ chính xác huấn luyện:** ~99%
- **Độ chính xác kiểm tra:** ~99%
- **Số epoch:** 10
- **Batch size:** 64
## Demo ![alt text](image-1.png)
## 🚀 Cách sử dụng

```bash
# Clone repository
git clone https://github.com/your-username/CNN_MNIST.git

# Cài đặt dependencies
pip install tensorflow numpy matplotlib

# Chạy notebook
jupyter notebook CNN_Classifier.ipynb
```

## 📁 Cấu trúc dự án

```
CNN_MNIST/
├── CNN_Classifier.ipynb    # Notebook chính
├── mnist_cnn_model.h5      # Mô hình đã huấn luyện
└── README.md               # Tài liệu dự án
```

## 💡 Kỹ năng thể hiện

- ✅ Xây dựng mô hình Deep Learning với CNN
- ✅ Tiền xử lý dữ liệu hình ảnh
- ✅ Huấn luyện và đánh giá mô hình
- ✅ Trực quan hóa kết quả với Matplotlib
- ✅ Lưu và tải mô hình đã huấn luyện

## 📧 Liên hệ

- **Email:** your-email@example.com
- **LinkedIn:** [Your LinkedIn](https://linkedin.com/in/your-profile)
- **GitHub:** [@your-username](https://github.com/your-username)

---

⭐ **Nếu dự án hữu ích, hãy cho một star!**