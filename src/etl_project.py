import sqlite3
import pandas as pd

# ==========================================
# 1. EXTRACT
# ==========================================
# Path diperbarui ke folder data/raw/
file_path = "data/raw/data_tugas_1.xlsx"
print("--- 1. MEMULAI PROSES EXTRACT DATA ---")

df = pd.read_excel(file_path)
kolom_dipakai = ['Y', 'AGE', 'LDL', 'HDL', 'TCH', 'LTG', 'GLU']
df_clean = df[kolom_dipakai].copy()

# ==========================================
# 2. TRANSFORM
# ==========================================
print("\n--- 2. MEMULAI PROSES TRANSFORM DATA ---")


def kelompok_usia(age):
  if age < 30:
    return "Muda (<30)"
  elif 30 <= age <= 50:
    return "Dewasa (30-50)"
  else:
    return "Lansia (>50)"


def kategori_gula(glu):
  if glu < 100:
    return "Normal"
  elif 100 <= glu <= 125:
    return "Prediabetes"
  else:
    return "Diabetes"


df_clean["AGE_GROUP"] = df_clean["AGE"].apply(kelompok_usia)
df_clean["GLU_CATEGORY"] = df_clean["GLU"].apply(kategori_gula)
df_clean["RATIO_LDL_HDL"] = (df_clean["LDL"] / df_clean["HDL"]).round(2)

print("Transformasi data berhasil dilakukan!")

# ==========================================
# 3. LOAD
# ==========================================
print("\n--- 3. MEMULAI PROSES LOAD DATA ---")

# A. Path diperbarui ke data/processed/
csv_filename = "data/processed/data_pasien_clean.csv"
df_clean.to_csv(csv_filename, index=False)
print(f"-> Data berhasil disimpan ke CSV: '{csv_filename}'")

# B. Path diperbarui ke database/
db_name = "database/health_data.db"
conn = sqlite3.connect(db_name)

df_clean.to_sql("patient_metrics", conn, if_exists="replace", index=False)
conn.close()
print(f"-> Data berhasil disimpan ke Database SQLite: '{db_name}'")

print("\n=== PIPELINE ETL SELESAI & BERHASIL! ===")