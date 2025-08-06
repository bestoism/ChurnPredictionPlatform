import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Churn Pelanggan", layout="wide")

# --- FUNGSI UNTUK MEMUAT MODEL ---
# @st.cache_resource adalah 'decorator' yang membuat Streamlit cerdas.
@st.cache_resource
def load_model():
    model = joblib.load("notebooks/churn_model.pkl")
    return model

# --- APLIKASI UTAMA ---

# model
model_pipeline = load_model()

# judul dan subjudul
st.title("🤖 Platform Prediksi Churn Pelanggan")
st.write("Aplikasi ini memprediksi apakah seorang pelanggan berisiko berhenti berlangganan (churn) berdasarkan data mereka.")

# sidebar untuk input dari user
st.sidebar.header("Masukkan Data Pelanggan:")

# --- WIDGET INPUT DI SIDEBAR ---
# fungsi untuk mengumpulkan input agar lebih rapi
def user_input_features():
    tenure_months = st.sidebar.slider('Lama Berlangganan (Bulan)', 1, 72, 12)
    monthly_charges = st.sidebar.slider('Tagihan Bulanan ($)', 18.0, 120.0, 70.0)
    total_charges = st.sidebar.slider('Total Tagihan ($)', 18.0, 8700.0, 1400.0)
    
    contract_type = st.sidebar.selectbox('Tipe Kontrak', ('Month-to-month', 'One year', 'Two year'))
    internet_service_type = st.sidebar.selectbox('Tipe Layanan Internet', ('DSL', 'Fiber optic', 'No'))
    payment_method = st.sidebar.selectbox('Metode Pembayaran', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
    
    has_online_security = st.sidebar.selectbox('Keamanan Online', ('Yes', 'No', 'No internet service'))
    has_tech_support = st.sidebar.selectbox('Dukungan Teknis', ('Yes', 'No', 'No internet service'))
    
    gender = st.sidebar.radio('Jenis Kelamin', ('Male', 'Female'))
    has_dependents = st.sidebar.radio('Memiliki Tanggungan', (True, False))
    has_partner = st.sidebar.radio('Memiliki Pasangan', (True, False))
    has_paperless_billing = st.sidebar.radio('Tagihan Tanpa Kertas', (True, False))
    
    is_senior_citizen = 0 
    has_phone_service = True 
    has_multiple_lines = 'No' 
    has_online_backup = 'No' 
    has_device_protection = 'No' 
    has_streaming_tv = 'No' 
    has_streaming_movies = 'No' 

    data = {
        'gender': gender,
        'is_senior_citizen': is_senior_citizen,
        'has_partner': has_partner,
        'has_dependents': has_dependents,
        'tenure_months': tenure_months,
        'has_phone_service': has_phone_service,
        'has_multiple_lines': has_multiple_lines,
        'internet_service_type': internet_service_type,
        'has_online_security': has_online_security,
        'has_online_backup': has_online_backup,
        'has_device_protection': has_device_protection,
        'has_tech_support': has_tech_support,
        'has_streaming_tv': has_streaming_tv,
        'has_streaming_movies': has_streaming_movies,
        'contract_type': contract_type,
        'has_paperless_billing': has_paperless_billing,
        'payment_method': payment_method,
        'monthly_charges': monthly_charges,
        'total_charges': total_charges
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# --- TAMPILKAN INPUT DAN BUAT PREDIKSI ---
st.subheader("Data Pelanggan yang Dimasukkan:")
st.write(input_df)

if st.button('Prediksi Churn'):
    prediction = model_pipeline.predict(input_df)
    prediction_proba = model_pipeline.predict_proba(input_df)

    st.subheader('Hasil Prediksi:')
    
    if prediction[0] == 1:
        st.error('**Berisiko Tinggi untuk Churn**')
        st.write(f"Probabilitas Churn: {prediction_proba[0][1]*100:.2f}%")
    else:
        st.success('**Berisiko Rendah untuk Churn**')
        st.write(f"Probabilitas Churn: {prediction_proba[0][1]*100:.2f}%")
    
    st.write("---")
    st.write("Probabilitas untuk setiap kelas:")
    st.write(pd.DataFrame(prediction_proba, columns=['Probabilitas Tidak Churn', 'Probabilitas Churn']))