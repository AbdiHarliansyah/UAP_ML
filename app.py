import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2, ResNet50
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing import image
import os

# Fungsi untuk memuat model MobileNetV2
def load_mobilenet_model(model_path):
    base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    base_model.trainable = False  # Jika Anda tidak ingin melatih ulang layer dasar
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(2, activation='softmax')  # 2 kelas: Normal dan Tuberkulosis
    ])
    model.load_weights(model_path, by_name=True)
    return model

# Fungsi untuk memuat model ResNet50
def load_resnet_model(model_path):
    base_model = ResNet50(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
    base_model.trainable = False  # Jika Anda tidak ingin melatih ulang layer dasar
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(2, activation='softmax')  # 2 kelas: Normal dan Tuberkulosis
    ])
    model.load_weights(model_path, by_name=True)
    return model

# Fungsi untuk memproses gambar
def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Tambahkan batch size
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return img_array

# Fungsi utama aplikasi Streamlit
def main():
    st.title("Klasifikasi Tuberkulosis menggunakan MobileNetV2 atau ResNet50")
    
    # Path model
    mobilenet_model_path = 'D:/UAPML/model/mobilenet_tb_classifier.h5'
    resnet_model_path = 'D:/UAPML/model/resnet_tb_classifier.h5'
    
    # Verifikasi apakah file ada
    if not os.path.exists(mobilenet_model_path):
        st.error(f"Model MobileNet tidak ditemukan di: {mobilenet_model_path}")
    else:
        mobilenet_model = load_mobilenet_model(mobilenet_model_path)

    if not os.path.exists(resnet_model_path):
        st.error(f"Model ResNet tidak ditemukan di: {resnet_model_path}")
    else:
        resnet_model = load_resnet_model(resnet_model_path)

    # Upload gambar untuk klasifikasi
    uploaded_image = st.file_uploader("Pilih Gambar", type=["jpg", "jpeg", "png"])
    
    if uploaded_image is not None:
        img = image.load_img(uploaded_image)
        processed_img = preprocess_image(img)
        
        # Pilih model yang ingin digunakan
        model_choice = st.selectbox("Pilih Model untuk Klasifikasi", ["MobileNetV2", "ResNet50"])
        
        if model_choice == "MobileNetV2":
            prediction = mobilenet_model.predict(processed_img)
        else:
            prediction = resnet_model.predict(processed_img)

        # Interpretasi hasil
        class_names = ['Normal', 'Tuberkulosis']
        predicted_class = class_names[np.argmax(prediction)]
        st.image(img, caption="Gambar yang Diunggah", use_column_width=True)
        st.write(f"Prediksi: {predicted_class} dengan kemungkinan: {100 * np.max(prediction):.2f}%")

# Jalankan aplikasi Streamlit
if __name__ == "__main__":
    main()
