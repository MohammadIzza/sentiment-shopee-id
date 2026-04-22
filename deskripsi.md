# Analisis Sentimen Ulasan Aplikasi Shopee Indonesia pada Google Play Store Menggunakan TF-IDF, LinearSVC, dan IndoBERT

---

## Latar Belakang
Google Play Store menyediakan ribuan ulasan pengguna yang merepresentasikan pengalaman nyata terhadap aplikasi. Analisis sentimen pada ulasan ini penting untuk memahami persepsi dan kepuasan pengguna. Studi ini menganalisis sentimen ulasan aplikasi Shopee Indonesia secara komprehensif menggunakan pendekatan machine learning dan deep learning.

## Sumber Data
Data dikumpulkan melalui scraping Google Play Store menggunakan Python (`google-play-scraper`). Dataset terdiri dari lebih dari 10.000 ulasan aplikasi Shopee Indonesia.

## Pelabelan
Label sentimen ditentukan dari rating bintang:
- 1–2: negative
- 3: neutral
- 4–5: positive

## Pra-pemrosesan Data
Tahapan utama pra-pemrosesan meliputi:
- Case folding
- Penghapusan URL, emoji, angka, tanda baca
- Tokenisasi sederhana
- Stopword removal
- Stemming (Sastrawi)

## Metodologi
Tiga pendekatan utama yang digunakan:
1. TF-IDF + Logistic Regression
2. TF-IDF + LinearSVC
3. IndoBERT fine-tuning

## Evaluasi
Evaluasi dilakukan pada data training dan testing. Metrik utama yang digunakan adalah accuracy, classification report, dan confusion matrix.

## Pengujian Model
Model terbaik diuji pada beberapa kalimat baru untuk memastikan generalisasi, menghasilkan output: negative, neutral, atau positive.

## Hasil dan Kesimpulan
- Model terbaik: [diisi sesuai hasil]
- Akurasi training: [diisi sesuai hasil]
- Akurasi testing: [diisi sesuai hasil]
- Alasan pemilihan: [misal: akurasi tertinggi, robust, dsb]

---
