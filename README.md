# Analisis Sentimen Ulasan Aplikasi Shopee Indonesia

Repositori ini berisi kode dan dokumentasi untuk analisis sentimen pada ulasan aplikasi Shopee Indonesia di Google Play Store menggunakan pendekatan machine learning (TF-IDF + Logistic Regression, LinearSVC) dan deep learning (IndoBERT).

---

## Deskripsi Proyek
Studi ini bertujuan membangun sistem analisis sentimen yang andal terhadap ulasan pengguna aplikasi Shopee Indonesia. Data dikumpulkan melalui proses scraping, kemudian diproses, dilabeli, dan digunakan untuk pelatihan serta evaluasi model.

Target utama: akurasi minimal 85% pada data pengujian.

## Struktur Direktori
```
sentiment_submission/
├── data/                # Dataset hasil scraping dan labeling
├── models/              # Model hasil pelatihan
├── scraping_google_play.py  # Script scraping data
├── training_sentiment_analysis.ipynb  # Notebook pelatihan model
├── requirements.txt     # Daftar dependensi
└── README.md            # Dokumentasi proyek
```

## Panduan Penggunaan

1. Instalasi dependensi:
	```bash
	pip install -r requirements.txt
	```

2. Jalankan proses scraping:
	```bash
	python scraping_google_play.py
	```
	Output:
	- data/shopee_playstore_raw.csv
	- data/shopee_playstore_labeled.csv

3. Jalankan pelatihan dan evaluasi model:
	- Buka dan jalankan seluruh cell pada `training_sentiment_analysis.ipynb`.

## Catatan
- Notebook pelatihan memuat seluruh tahapan: preprocessing, EDA, pelatihan, evaluasi, dan inference.
- Untuk eksperimen IndoBERT, disarankan menggunakan Google Colab.
- Parameter aplikasi dapat diubah pada variabel `APP_ID` di `scraping_google_play.py`.


Informasi lebih lanjut dan narasi lengkap dapat dilihat pada file `deskripsi.md`.
# Sentiment Analysis Shopee Indonesia

Analisis sentimen ulasan aplikasi Shopee Indonesia di Google Play Store menggunakan TF-IDF, LinearSVC, dan IndoBERT.

## Deskripsi
Proyek ini melakukan scraping data ulasan aplikasi Shopee Indonesia dari Google Play Store, melakukan preprocessing, pelabelan berdasarkan rating, dan pelatihan model analisis sentimen dengan tiga pendekatan:
1. TF-IDF + Logistic Regression
2. TF-IDF + LinearSVC
3. IndoBERT fine-tuning

Target utama: akurasi minimal 85% pada data testing.

## Struktur Folder
- data/: Dataset hasil scraping dan labeling
- models/: Model hasil pelatihan
- scraping_google_play.py: Script scraping data
- training_sentiment_analysis.ipynb: Notebook pelatihan model
- requirements.txt: Daftar dependensi

## Cara Menjalankan
1. Jalankan scraping: `python scraping_google_play.py`
2. Jalankan pelatihan dan evaluasi model di notebook `training_sentiment_analysis.ipynb`

---

> Untuk detail narasi, lihat narasi_submission_template.md

### 1. Install dependensi
```bash
pip install -r requirements.txt
```

### 2. Jalankan scraping
```bash
python scraping_google_play.py
```

Script akan membuat file:
- `data/shopee_playstore_raw.csv`
- `data/shopee_playstore_labeled.csv`

### 3. Jalankan notebook
Buka `training_sentiment_analysis.ipynb`, lalu jalankan semua cell dari atas ke bawah.

## Catatan Penting untuk Submission

Pastikan folder zip final Anda berisi:

- notebook pelatihan `.ipynb`
- file scraping `.py`
- `requirements.txt`
- dataset hasil scraping `.csv`

Notebook juga sudah memuat:

- preprocessing
- EDA singkat
- 3 eksperimen model
- evaluasi
- cell inference
- penyimpanan model terbaik

## Saran Agar Hasil Bagus

- Jalankan di Google Colab jika ingin mencoba IndoBERT
- Jika runtime terbatas, eksperimen 1 dan 2 tetap bisa dijalankan di laptop lokal
- Untuk screenshot inferensi, gunakan cell inference terakhir di notebook

## Judul Submission yang Bisa Dipakai

**Analisis Sentimen Ulasan Aplikasi Shopee Indonesia pada Google Play Store Menggunakan TF-IDF, LinearSVC, dan IndoBERT**

## Jika Ingin Ganti Topik

Anda bisa ganti `APP_ID` di `scraping_google_play.py`, misalnya:
- Tokopedia: `com.tokopedia.tkpd`
- Gojek: `com.gojek.app`

Lalu tetap gunakan alur notebook yang sama.
