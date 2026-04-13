# Proyek Analisis Sentimen

Paket ini disusun untuk memenuhi submission proyek analisis sentimen dengan pendekatan yang aman dan realistis:

- **Sumber data**: scraping ulasan aplikasi **Shopee Indonesia** dari Google Play Store
- **Jumlah target data**: minimal **10.000** review
- **Jumlah kelas**: **3 kelas** (`negative`, `neutral`, `positive`)
- **3 percobaan skema pelatihan**:
  1. TF-IDF + Logistic Regression
  2. TF-IDF + LinearSVC
  3. IndoBERT fine-tuning (deep learning)

## Struktur Folder

```bash
sentiment_submission/
├── data/
├── models/
├── scraping_google_play.py
├── training_sentiment_analysis.ipynb
├── requirements.txt
└── README.md
```

## Topik yang Diangkat

**Analisis sentimen ulasan aplikasi Shopee Indonesia di Google Play Store.**

Topik ini aman, tidak sensitif, dan mudah dijelaskan dalam laporan karena review aplikasi berisi opini langsung pengguna.

## Mapping Label

Label dibentuk dari rating bintang:

- **1–2** → `negative`
- **3** → `neutral`
- **4–5** → `positive`

## Cara Menjalankan

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
