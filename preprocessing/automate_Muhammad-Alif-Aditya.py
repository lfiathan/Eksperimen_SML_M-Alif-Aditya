import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def preprocess_data(input_path, output_path):
    # Load data
    df = pd.read_csv(input_path)
    
    # Preprocessing steps
    df = df.drop_duplicates()
    df['target'] = (df['quality'] >= 7).astype(int)
    
    # Scaling
    scaler = StandardScaler()
    features = df.drop(['quality', 'target'], axis=1, errors='ignore')
    scaled_data = scaler.fit_transform(features)
    
    # Final DataFrame
    df_final = pd.DataFrame(scaled_data, columns=features.columns)
    df_final['target'] = df['target'].values
    
    # Save output
    df_final.to_csv(output_path, index=False)
    print(f"Dataset tersimpan di: {output_path}")

if __name__ == "__main__":
    # Menyesuaikan path untuk GitHub Actions
    preprocess_data('winequality-red.csv', 'preprocessing/winequality_preprocessed.csv')