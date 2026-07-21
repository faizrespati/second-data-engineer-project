import sqlite3
import pandas as pd

# Path diperbarui ke database/
conn = sqlite3.connect("database/health_data.db")

query = """
SELECT 
    GLU_CATEGORY,
    COUNT(*) AS total_pasien,
    ROUND(AVG(AGE), 1) AS avg_usia,
    ROUND(AVG(GLU), 1) AS avg_gula_darah,
    ROUND(AVG(Y), 1) AS avg_perkembangan_penyakit
FROM patient_metrics
GROUP BY GLU_CATEGORY
ORDER BY avg_gula_darah DESC
"""

df_summary = pd.read_sql_query(query, conn)
conn.close()

print("--- RESUME DATA PASIEN DARI DATABASE (SQL) ---")
print(df_summary)