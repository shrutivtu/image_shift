import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

# Function to shift the image
def shift_image(image, direction):
    image = image.reshape(28, 28)  # Reshape to 28x28 matrix
    if direction == "up":
        shifted = scipy.ndimage.shift(image, [-1, 0], cval=0)  # Shift up
    elif direction == "down":
        shifted = scipy.ndimage.shift(image, [1, 0], cval=0)  # Shift down
    elif direction == "left":
        shifted = scipy.ndimage.shift(image, [0, -1], cval=0)  # Shift left
    elif direction == "right":
        shifted = scipy.ndimage.shift(image, [0, 1], cval=0)  # Shift right
    return shifted

st.title("MNIST Image Shifter")

st.write("Upload an MNIST image to shift:")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    img = plt.imread(uploaded_file)
    if img.shape != (28, 28):
        img = img[:,:,0]  # Convert to grayscale if the image has 3 channels (RGB)

    # Display the original image
    st.subheader("Original Image")
    st.image(img, width=200)

    # Select direction to shift
    direction = st.selectbox("Select Shift Direction", ["up", "down", "left", "right"])

    # Shift the image based on the selected direction
    shifted_img = shift_image(img, direction)

    # Display the shifted image
    st.subheader(f"Shifted Image ({direction})")
    st.image(shifted_img, width=200)

    # Optionally, show multiple shifted images
    st.subheader("All Shifted Versions:")
    shifted_images = [shift_image(img, d) for d in ["up", "down", "left", "right"]]
    for i, direction in enumerate(["up", "down", "left", "right"]):
        st.image(shifted_images[i], caption=f"Shifted {direction}", width=200)

