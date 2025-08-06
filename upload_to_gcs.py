from google.cloud import storage
import os

# --- KONFIGURASI ---
PROJECT_ID = "numeric-polygon-468208-a7"

BUCKET_NAME = "ryanbesto-churn-project-data-lake-2025"

# Nama file lokal yang akan diunggah
SOURCE_FILE_NAME = "telco_churn.csv"

# Nama file yang diinginkan di Google Cloud Storage
DESTINATION_BLOB_NAME = "raw_data/telco_churn.csv"
# -------------------

def upload_to_gcs(project_id, bucket_name, source_file_name, destination_blob_name):
    """Mengunggah file ke Google Cloud Storage bucket."""
    
    # Inisialisasi client
    # Kredensial akan diambil secara otomatis dari gcloud auth application-default login
    storage_client = storage.Client(project=project_id)
    
    # Mendapatkan bucket tujuan
    bucket = storage_client.bucket(bucket_name)
    
    # Membuat referensi ke object/blob tujuan
    blob = bucket.blob(destination_blob_name)
    
    # Cek apakah file sumber ada
    if not os.path.exists(source_file_name):
        raise FileNotFoundError(f"Error: File sumber tidak ditemukan di '{source_file_name}'")

    # Mengunggah file
    print(f"Mengunggah file '{source_file_name}' ke 'gs://{bucket_name}/{destination_blob_name}'...")
    blob.upload_from_filename(source_file_name)
    
    print(f"File berhasil diunggah.")

if __name__ == "__main__":
    # Cek apakah file sumber ada
    if not os.path.exists(SOURCE_FILE_NAME):
        print(f"ERROR: File '{SOURCE_FILE_NAME}' tidak ditemukan. Pastikan file ada di folder yang sama dengan script.")
    else:
        try:
            # Panggil fungsi untuk mengunggah
            upload_to_gcs(PROJECT_ID, BUCKET_NAME, SOURCE_FILE_NAME, DESTINATION_BLOB_NAME)
        except Exception as e:
            print(f"Terjadi error saat mengunggah: {e}")