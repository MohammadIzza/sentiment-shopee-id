"""
Scraping review Google Play Store untuk proyek analisis sentimen.

Default topik:
Analisis sentimen ulasan aplikasi Shopee Indonesia.

Menjalankan:
    python scraping_google_play.py

Output:
    data/shopee_playstore_raw.csv
    data/shopee_playstore_labeled.csv
"""

from __future__ import annotations

import os
import time
import pandas as pd
from google_play_scraper import reviews, Sort


APP_ID = "com.shopee.id"
LANG = "id"
COUNTRY = "id"
TARGET_COUNT = 10000
SLEEP_SECONDS = 0.5
OUTPUT_DIR = "data"
RAW_FILENAME = "shopee_playstore_raw.csv"
LABELED_FILENAME = "shopee_playstore_labeled.csv"


def map_label(score: int) -> str:
    if score in [1, 2]:
        return "negative"
    if score == 3:
        return "neutral"
    return "positive"


def scrape_reviews(
    app_id: str,
    lang: str = "id",
    country: str = "id",
    target_count: int = 10000,
    sleep_seconds: float = 0.5,
) -> pd.DataFrame:
    all_reviews = []
    continuation_token = None

    print(f"[INFO] Mulai scraping app_id={app_id}")
    print(f"[INFO] Target minimal review: {target_count}")

    while len(all_reviews) < target_count:
        result, continuation_token = reviews(
            app_id,
            lang=lang,
            country=country,
            sort=Sort.NEWEST,
            count=200,
            continuation_token=continuation_token,
        )

        if not result:
            print("[INFO] Tidak ada review tambahan yang bisa diambil.")
            break

        all_reviews.extend(result)
        print(f"[INFO] Total review terkumpul: {len(all_reviews)}")

        if continuation_token is None:
            print("[INFO] Continuation token habis.")
            break

        time.sleep(sleep_seconds)

    df = pd.DataFrame(all_reviews)

    if df.empty:
        raise ValueError("Data hasil scraping kosong. Coba ulangi atau ganti APP_ID.")

    # Pilih kolom penting
    selected_columns = [
        "reviewId",
        "userName",
        "content",
        "score",
        "thumbsUpCount",
        "reviewCreatedVersion",
        "at",
        "replyContent",
        "repliedAt",
        "appVersion",
    ]

    existing_columns = [col for col in selected_columns if col in df.columns]
    df = df[existing_columns].copy()

    # Bersihkan dasar
    df = df.drop_duplicates(subset=["reviewId"], keep="first")
    df["content"] = df["content"].astype(str).str.strip()
    df = df[df["content"].notna()]
    df = df[df["content"] != ""]
    df = df[df["content"].str.lower() != "nan"]

    # Tambahkan label 3 kelas berdasarkan rating
    df["label"] = df["score"].apply(map_label)

    return df


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = scrape_reviews(
        app_id=APP_ID,
        lang=LANG,
        country=COUNTRY,
        target_count=TARGET_COUNT,
        sleep_seconds=SLEEP_SECONDS,
    )

    raw_path = os.path.join(OUTPUT_DIR, RAW_FILENAME)
    labeled_path = os.path.join(OUTPUT_DIR, LABELED_FILENAME)

    df.to_csv(raw_path, index=False)
    df.to_csv(labeled_path, index=False)

    print(f"[SUCCESS] Raw dataset disimpan ke: {raw_path}")
    print(f"[SUCCESS] Labeled dataset disimpan ke: {labeled_path}")
    print("[INFO] Distribusi label:")
    print(df["label"].value_counts())
    print(f"[INFO] Jumlah akhir dataset: {len(df)}")


if __name__ == "__main__":
    main()
