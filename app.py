import streamlit as st
import numpy as np
import pickle

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Prediksi Gagal Jantung", layout="centered")

st.title("🫀 Prediksi Kematian Akibat Gagal Jantung")
st.write("Masukkan data pasien untuk memprediksi risiko kematian akibat gagal jantung.")

# Input pengguna
age = st.number_input("Usia", min_value=0)
anaemia = st.selectbox("Anaemia (Hemoglobin Rendah)", [0, 1])
creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase", min_value=0)
diabetes = st.selectbox("Riwayat Diabetes", [0, 1])
ejection_fraction = st.number_input("Ejection Fraction (%)", min_value=0)
high_blood_pressure = st.selectbox("Tekanan Darah Tinggi", [0, 1])
platelets = st.number_input("Jumlah Platelet", min_value=0.0)
serum_creatinine = st.number_input("Serum Creatinine", min_value=0.0)
serum_sodium = st.number_input("Serum Sodium", min_value=0)
sex = st.selectbox("Jenis Kelamin", options=[(1, "Laki-laki"), (0, "Perempuan")], format_func=lambda x: x[1])[0]
smoking = st.selectbox("Merokok", [0, 1])
time = st.number_input("Waktu Follow-up (hari)", min_value=0)

# Prediksi
if st.button("🔍 Prediksi"):
    data = np.array([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                      high_blood_pressure, platelets, serum_creatinine, serum_sodium,
                      sex, smoking, time]])

    prediction = model.predict(data)[0]
    result = "⚠️ Pasien berisiko MENINGGAL akibat gagal jantung." if prediction == 1 else "✅ Pasien diprediksi SELAMAT."
    
    st.subheader("Hasil Prediksi:")
    st.success(result) if prediction == 0 else st.error(result)
