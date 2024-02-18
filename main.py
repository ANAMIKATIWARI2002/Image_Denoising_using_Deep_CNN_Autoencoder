import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model

# Load the pre-trained autoencoder model
model = load_model('D:/collage work/projects/image_denoising_new/model.h5')

def denoise_image(file_path):
    # Load the image
    img = Image.open(file_path).convert('L')  # Convert to grayscale
    img = img.resize((28, 28))  # Resize to match model input size
    img_array = np.array(img) / 255.0  # Normalize to [0, 1]

    # Reshape the image array to match model input shape
    img_array = img_array.reshape(1, 28, 28, 1)

    # Use the model to denoise the image
    denoised_img = model.predict(img_array)

    # Display the original and denoised images
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img_array.reshape(28, 28), cmap='gray')
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(denoised_img.reshape(28, 28), cmap='gray')
    plt.title('Denoised Image')
    plt.show()

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if file_path:
        denoise_image(file_path)

# Create the main window
root = tk.Tk()
root.title("Image Denoising App")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  

# Create and configure widgets
style = ttk.Style()

style.configure('TButton', font=('Arial', 14), padding=10, background='#4CAF50')  
style.map('TButton', background=[('active', '#45a049')])

label = tk.Label(root, text="Select an image for denoising:", font=('Arial', 18))
label.pack(pady=20)

browse_button = ttk.Button(root, text="Browse", command=browse_image)
browse_button.pack(pady=20)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
