import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def run_automation():
    # Sesuaikan dengan nama file dataset laptop Anda
    input_file = 'laptop_price.csv' 
    output_path = 'preprocessing/laptop_sales_preprocessed.csv'
    
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} tidak ditemukan!")
        return

    df = pd.read_csv(input_file, encoding='latin-1')
    
    # A. Menghapus kolom yang tidak relevan
    df = df.drop(['laptop_ID'], axis=1, errors='ignore')

    # B. Membuat Target Kategorikal (Binning Harga)
    def categorize_price(price):
        if price < 600: return 0
        elif price < 1300: return 1
        else: return 2

    df['price_category'] = df['Price_euros'].apply(categorize_price)
    df = df.drop('Price_euros', axis=1)

    # C. Encoding Categorical Data
    le = LabelEncoder()
    categorical_cols = ['Company', 'TypeName', 'Cpu', 'Gpu', 'OpSys']
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col].astype(str))

    # C2. Normalisasi kolom numerik bertipe string
    # Ubah 'Ram' ke angka (GB)
    df['Ram'] = (
        df['Ram']
        .astype(str)
        .str.extract(r'(\d+\.?\d*)')[0]
        .str.replace(',', '.', regex=False)
        .astype(float)
    )

    # Ubah 'Weight' ke angka (kg)
    df['Weight'] = (
        df['Weight']
        .astype(str)
        .str.extract(r'(\d+\.?\d*)')[0]
        .str.replace(',', '.', regex=False)
        .astype(float)
    )

    # Pastikan 'Inches' numerik
    df['Inches'] = pd.to_numeric(df['Inches'], errors='coerce')

    # Tangani nilai kosong dengan median
    numerical_cols = ['Inches', 'Ram', 'Weight']
    for col in numerical_cols:
        df[col] = df[col].fillna(df[col].median())

    # D. Scaling Fitur Numerik
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    # Pastikan folder preprocessing ada
    os.makedirs('preprocessing', exist_ok=True)
    
    # Simpan hasil
    df.to_csv(output_path, index=False)
    print(f"✅ Otomasi Berhasil! Data disimpan di: {output_path}")

if __name__ == "__main__":
    run_automation()