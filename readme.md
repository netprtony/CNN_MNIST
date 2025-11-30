# 🧠 CNN MNIST Classifier

A **Convolutional Neural Network (CNN)** model for handwritten digit recognition using the MNIST dataset.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red?style=for-the-badge&logo=keras&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---
    
## 📋 Project Description

This project builds a CNN model to classify handwritten digits (0-9) with high accuracy on the MNIST dataset, which contains 70,000 images.

---

## 🛠️ Technologies Used

| Technology | Description |
|------------|-------------|
| **TensorFlow 2.x** | Main Deep Learning framework |
| **Keras** | High-level API for building models |
| **NumPy** | Array processing and numerical computation |
| **Matplotlib** | Data and results visualization |
| **Google Colab** | Training environment with free GPU |

---

## 🏗️ Model Architecture

```
Input (28x28x1)
       │
       ▼
┌─────────────────────────────┐
│ Conv2D (32 filters, 3x3)    │
│ Activation: ReLU            │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ MaxPooling2D (2x2)          │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ Conv2D (64 filters, 3x3)    │
│ Activation: ReLU            │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ MaxPooling2D (2x2)          │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ Conv2D (64 filters, 3x3)    │
│ Activation: ReLU            │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ Flatten                     │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ Dense (64 units)            │
│ Activation: ReLU            │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│ Dense (10 units)            │
│ Activation: Softmax         │
└─────────────────────────────┘
       │
       ▼
   Output (10 classes)
```

---

## 📊 Results

| Metric | Value |
|--------|-------|
| **Training Accuracy** | ~99% |
| **Test Accuracy** | ~99% |
| **Epochs** | 10 |
| **Batch Size** | 64 |

### 📈 Accuracy & Loss Charts

![Accuracy and Loss](image.png)

---

## 🎯 Demo

![Demo](image-1.png)

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install tensorflow numpy matplotlib
```

### Installation

```bash
# Clone the repository
git clone https://github.com/netprtony/CNN_MNIST.git

# Navigate to project directory
cd CNN_MNIST

# Run the notebook
jupyter notebook CNN_Classifier.ipynb
```

---

## 📁 Project Structure

```
CNN_MNIST/
│
├── 📓 CNN_Classifier.ipynb    # Main notebook
├── 🧠 mnist_cnn_model.h5      # Trained model
├── 📊 image.png               # Accuracy & Loss charts
├── 🎯 image-1.png             # Demo image
└── 📄 README.md               # Project documentation
```

---

## 💡 Skills Demonstrated

| Skill | Description |
|-------|-------------|
| ✅ **Deep Learning** | Building CNN models from scratch |
| ✅ **Image Preprocessing** | Data normalization and reshaping |
| ✅ **Model Training** | Training and validation with TensorFlow/Keras |
| ✅ **Data Visualization** | Plotting results with Matplotlib |
| ✅ **Model Persistence** | Saving and loading trained models |

---

## 📧 Contact

<p align="center">
  <a href="mailto:your-email@example.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
  <a href="https://linkedin.com/in/your-profile"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="https://github.com/your-username"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

---

<p align="center">
  ⭐ <strong>If you find this project useful, please give it a star!</strong> ⭐
</p>