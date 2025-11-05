import pandas as pd
import os

# Menentukan path secara dinamis
# __file__ merujuk ke file skrip ini (automate_Nama-siswa.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR) # Ini adalah folder 'Eksperimen_SML_Nama-siswa'

# Path ke data mentah
RAW_DATA_PATH = os.path.join(ROOT_DIR, 'namadataset_raw', 'winequality-red.csv')

# Path untuk menyimpan data bersih
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, 'namadataset_preprocessing')
PROCESSED_DATA_PATH = os.path.join(PROCESSED_DATA_DIR, 'wine_processed_clened.csv')

def load_data(path):
    """Memuat data dari file CSV."""
    print(f"Memuat data dari: {path}")
    if not os.path.exists(path):
        print(f"Error: File tidak ditemukan di {path}")
        return None
    # Dataset ini menggunakan pemisah titik koma
    return pd.read_csv(path, sep=';')

def preprocess_data(df):
    """Melakukan preprocessing pada dataframe."""
    print("Memulai preprocessing...")
    # Buat target klasifikasi biner: 1 jika quality > 5, selainnya 0
    df['quality_category'] = df['quality'].apply(lambda x: 1 if x > 5 else 0)
    
    # Hapus kolom 'quality' asli
    df_processed = df.drop('quality', axis=1)
    
    print("Preprocessing selesai.")
    return df_processed

def save_data(df, path):
    """Menyimpan dataframe yang telah diproses ke CSV."""
    # Pastikan direktori ada
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    print(f"Menyimpan data ke: {path}")
    df.to_csv(path, index=False)
    print("Data berhasil disimpan.")

if __name__ == "__main__":
    print("Menjalankan skrip preprocessing otomatis...")
    df_raw = load_data(RAW_DATA_PATH)
    
    if df_raw is not None:
        df_clean = preprocess_data(df_raw.copy())
        save_data(df_clean, PROCESSED_DATA_PATH)
        print("Skrip selesai.")
    else:
        print("Skrip dihentikan karena data mentah tidak ditemukan.")