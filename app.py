import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import cv2
from streamlit_drawable_canvas import st_canvas

# Define the model architecture (same as training)
def create_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(28, 28, 1)),  # Use Input instead of batch_shape
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model

# Load model weights
@st.cache_resource
def load_model():
    model = create_model()
    model.load_weights('CNN_CLASSIFIER/mnist_cnn_model.h5')  # Load weights instead of full model
    return model

# Compile model to ensure it's ready for prediction
model = load_model()
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Title and description
st.title("Dự đoán chữ số viết tay với CNN")
st.write("Vẽ một chữ số (0-9) trên canvas dưới đây và nhấn 'Dự đoán' để xem kết quả.")

# Create canvas for drawing
canvas_result = st_canvas(
    fill_color="black",
    stroke_width=20,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

# Prediction button
if st.button("Dự đoán"):
    if canvas_result.image_data is not None:
        # Process the image
        img = canvas_result.image_data
        img = Image.fromarray(img.astype("uint8"))
        img = img.convert("L")  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to 28x28
        img_array = np.array(img) / 255.0  # Normalize
        img_array = img_array.reshape(1, 28, 28, 1)  # Reshape for model

        # Make prediction
        prediction = model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        # Display results
        st.write(f"**Dự đoán**: Chữ số {predicted_digit}")
        st.write(f"**Độ tin cậy**: {confidence:.2f}%")
        st.image(img, caption="Hình ảnh đã xử lý (28x28)", use_container_width=False, width=100)
    else:
        st.warning("Vui lòng vẽ một chữ số trước khi dự đoán!")

# Model summary
with st.expander("Thông tin mô hình"):
    st.write("Mô hình CNN được sử dụng:")
    model.summary(print_fn=lambda x: st.text(x))