# Template Narasi Submission

## Judul
Analisis Sentimen Ulasan Aplikasi Shopee Indonesia pada Google Play Store Menggunakan TF-IDF, LinearSVC, dan IndoBERT

## Latar Belakang
Google Play Store menyediakan banyak ulasan pengguna yang merepresentasikan pengalaman nyata terhadap suatu aplikasi. Ulasan tersebut dapat dianalisis untuk mengetahui kecenderungan sentimen pengguna, baik negatif, netral, maupun positif. Pada proyek ini dilakukan analisis sentimen terhadap ulasan aplikasi Shopee Indonesia.

## Sumber Data
Data diperoleh melalui scraping mandiri dari Google Play Store menggunakan Python dan library `google-play-scraper`. Dataset diambil dari aplikasi Shopee Indonesia dengan target minimal 10.000 ulasan.

## Pelabelan
Label sentimen dibentuk berdasarkan rating bintang:
- rating 1–2: negative
- rating 3: neutral
- rating 4–5: positive

## Tahap Preprocessing
Tahap preprocessing meliputi:
- case folding
- penghapusan URL
- penghapusan emoji
- penghapusan angka dan tanda baca
- tokenisasi sederhana
- stopword removal
- stemming menggunakan Sastrawi

## Skema Percobaan
Tiga percobaan dilakukan:
1. TF-IDF + Logistic Regression
2. TF-IDF + LinearSVC
3. IndoBERT fine-tuning

## Evaluasi
Evaluasi dilakukan menggunakan data training dan testing. Metrik utama yang digunakan adalah accuracy, disertai classification report dan confusion matrix.

## Inference
Model terbaik diuji menggunakan beberapa kalimat baru dan menghasilkan output kelas kategorikal berupa negative, neutral, atau positive.

## Kesimpulan
Tuliskan model terbaik, nilai akurasi training/testing, serta alasan singkat mengapa model tersebut dipilih.
