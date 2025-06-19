# 🧼 Image Denoising using Deep CNN Autoencoder

## 📝 Overview

This repository presents a Python-based application for **image denoising** using a **Convolutional Neural Network (CNN)** powered **deep autoencoder**. It offers a simple and intuitive interface for users to upload their noisy **MNIST digit images** and receive denoised outputs. The model learns to remove noise while preserving important image features by training on pairs of clean and noisy images.

---

## ✨ Features

- **🖼️ Intuitive User Interface**  
  A lightweight and easy-to-use graphical interface built with `tkinter` allows users to upload noisy digit images and view the denoised results instantly.

- **🧠 CNN-Based Deep Autoencoder**  
  Utilizes a deep convolutional autoencoder architecture to reconstruct clean images from noisy inputs. The model is trained on the MNIST dataset for robust performance on handwritten digits.

- **🛠️ Modular Codebase**  
  The project is structured for easy extension and integration. The autoencoder can be retrained on custom datasets, and the GUI can be adapted for broader applications.

---

## 🚀 Getting Started

### ✅ Prerequisites

Ensure you have the following installed:

- Python 3.x  
- `Pillow`  
- `NumPy`  
- `Matplotlib`  
- `Keras` / `TensorFlow` backend  
- `tkinter` (usually comes pre-installed with Python)

### 🔧 Installation
Clone the repository and install the required packages:

  ```bash
  git clone https://github.com/ANAMIKATIWARI2002/Image_Denoising_using_Deep_CNN_Autoencoder.git
  cd Image_Denoising_using_Deep_CNN_Autoencoder
  pip install -r requirements.txt bash
  ```

### Run the notebook or the Python script:
To open the Jupyter Notebook:

  ```bash
  jupyter notebook denoising_autoencoder.ipynb
  ```
  
OR to launch the GUI interface:
  ```bash
  python denoising_interface.py
  ```





