
# DATASET — Shopee Indonesia Google Play Reviews

---

**Deskripsi:**
Dataset berisi hasil scraping ulasan aplikasi Shopee Indonesia dari Google Play Store. Data digunakan untuk analisis sentimen dan pelatihan model machine learning/deep learning.

**File utama:**
- `shopee_playstore_raw.csv` — Data mentah hasil scraping
- `shopee_playstore_labeled.csv` — Data yang sudah dilabeli sentimen

**Kolom utama:**
- reviewId
- userName
- content
- score
- thumbsUpCount
- reviewCreatedVersion
- at
- replyContent
- repliedAt
- appVersion
- label

**Cara mendapatkan dataset:**
Jalankan:
```bash
python scraping_google_play.py
```

---

*Pastikan data ini hanya digunakan untuk keperluan pembelajaran dan riset.*
