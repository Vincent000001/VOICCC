import os
import librosa
import numpy as np

def preprocess_audio(file_path, sr=22050):
    # Load audio file
    y, sr = librosa.load(file_path, sr=sr)
    # Normalize audio
    y = librosa.util.normalize(y)
    return y, sr

def extract_mfcc_features(y, sr, n_mfcc=13):
    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    return mfccs

if __name__ == "__main__":
    file_path = "path/to/audio/file.wav"
    y, sr = preprocess_audio(file_path)
    mfccs = extract_mfcc_features(y, sr)
    print(f"MFCCs: {mfccs.shape}")
