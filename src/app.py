import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Healthcare ETL Dashboard", page_icon="🩺", layout="wide"
)

st.title("🩺 Patient Health Metrics Dashboard")
st.markdown(
    "Dashboard interaktif dari hasil pipeline **ETL Data Kesehatan** (SQLite"
    " Database)."
)


@st.cache_data
def load_data():
  # Path diperbarui ke database/
  conn = sqlite3.connect("database/health_data.db")
  df = pd.read_sql_query("SELECT * FROM patient_metrics", conn)
  conn.close()
  return df


df = load_data()

st.sidebar.header("Filter Data")
selected_age_group = st.sidebar.multiselect(
    "Pilih Kelompok Usia:",
    options=df["AGE_GROUP"].unique(),
    default=df["AGE_GROUP"].unique(),
)

selected_glu_category = st.sidebar.multiselect(
    "Pilih Kategori Gula Darah:",
    options=df["GLU_CATEGORY"].unique(),
    default=df["GLU_CATEGORY"].unique(),
)

filtered_df = df[
    (df["AGE_GROUP"].isin(selected_age_group))
    & (df["GLU_CATEGORY"].isin(selected_glu_category))
]

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Pasien", len(filtered_df))
col2.metric("Rata-rata Usia", f"{filtered_df['AGE'].mean():.1f} Tahun")
col3.metric("Rata-rata Gula Darah", f"{filtered_df['GLU'].mean():.1f} mg/dL")
col4.metric(
    "Rata-rata Prog. Penyakit (Y)", f"{filtered_df['Y'].mean():.1f}"
)

st.divider()

row1_col1, row1_col2 = st.columns(2)

with row1_col1:
  st.subheader("📊 Distribusi Kategori Gula Darah")
  fig_pie = px.pie(
      filtered_df,
      names="GLU_CATEGORY",
      color="GLU_CATEGORY",
      color_discrete_map={"Normal": "#2ecc71", "Prediabetes": "#e67e22"},
      hole=0.4,
  )
  st.plotly_chart(fig_pie, use_container_width=True)

with row1_col2:
  st.subheader("📈 Hubungan Gula Darah vs Perkembangan Penyakit (Y)")
  fig_scatter = px.scatter(
      filtered_df,
      x="GLU",
      y="Y",
      color="GLU_CATEGORY",
      size="RATIO_LDL_HDL",
      hover_data=["AGE", "AGE_GROUP"],
      labels={
          "GLU": "Gula Darah",
          "Y": "Skor Perkembangan Penyakit",
          "RATIO_LDL_HDL": "Rasio LDL/HDL",
      },
  )
  st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()
st.subheader("📋 Data Pasien Terfilter")
st.dataframe(filtered_df, use_container_width=True)