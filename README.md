# 🩺 Healthcare Data ETL Pipeline & Interactive Dashboard

Projek Data Engineering sederhana untuk memproses, mentransformasi, dan mengagregasi data indikator kesehatan pasien, serta menyajikannya dalam bentuk dashboard web interaktif.

---

## 📌 Fitur Utama

- **Batch Extraction:** Membaca data mentah medis dari format Excel (`.xlsx`).
- **Data Transformation:** 
  - Kategori usia pasien (`AGE_GROUP`).
  - Pengelompokan tingkat risiko gula darah (`GLU_CATEGORY`).
  - Kalkulasi rasio kolesterol (`RATIO_LDL_HDL`).
- **Data Loading:** Menyimpan data terstruktur ke **CSV** dan Database **SQLite**.
- **Interactive Dashboard:** Visualisasi data kesehatan menggunakan **Streamlit** dan **Plotly**.

---

## 📁 Struktur Folder Projek

```text
4th-data-engineer/
├── data/
│   ├── raw/                  # Data mentah (input)
│   └── processed/            # Data hasil olahan ETL (output)
├── database/                 # Penyimpanan database SQLite local
├── src/                      # Source code Python
│   ├── etl_project.py        # Pipeline utama Extract, Transform, Load
│   ├── verify_db.py          # Script pengujian SQL Query
│   └── app.py                # Dashboard Web Streamlit
└── README.md                 # Dokumentasi projek
