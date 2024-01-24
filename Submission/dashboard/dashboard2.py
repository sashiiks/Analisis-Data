import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Load data
day_df = pd.read_csv("https://raw.githubusercontent.com/sashiiks/Analisis-Data/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/sashiiks/Analisis-Data/main/hour.csv")

# Convert date columns to datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Filter data for the analysis period
start_date = day_df['dteday'].min()
end_date = day_df['dteday'].max()

# Sidebar to select date range
with st.sidebar:
    st.image("https://raw.githubusercontent.com/sashiiks/Analisis-Data/main/logo%20Bike.png")
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=start_date,
        max_value=end_date,
        value=[start_date, end_date]
    )

# Filter data based on selected date range
day_df_filtered = day_df[(day_df['dteday'] >= str(start_date)) & (day_df['dteday'] <= str(end_date))]
hour_df_filtered = hour_df[(hour_df['dteday'] >= str(start_date)) & (hour_df['dteday'] <= str(end_date))]

# Plotting daily trends
st.header('Tren Peminjaman Sepeda per Hari (2011-2012)')
st.subheader('Peminjaman per Hari')

col1, col2 = st.columns(2)

with col1:
    total_rentals_per_day = day_df_filtered['cnt'].sum()
    st.metric("Total Peminjaman per Hari", value=total_rentals_per_day)

with col2:
    average_rentals_per_day = round(day_df_filtered['cnt'].mean(), 2)
    st.metric("Rata-rata Peminjaman per Hari", value=average_rentals_per_day)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    day_df_filtered['dteday'],
    day_df_filtered['cnt'],
    marker='o',
    linewidth=2,
    color="#FAD02E"  # Warna krem
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

# Plotting hourly trends
st.header('Tren Peminjaman Sepeda per Jam (2011-2012)')
st.subheader('Peminjaman per Jam')

col3, col4 = st.columns(2)

with col3:
    total_rentals_per_hour = hour_df_filtered['cnt'].sum()
    st.metric("Total Peminjaman per Jam", value=total_rentals_per_hour)

with col4:
    average_rentals_per_hour = round(hour_df_filtered['cnt'].mean(), 2)
    st.metric("Rata-rata Peminjaman per Jam", value=average_rentals_per_hour)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    hour_df_filtered['dteday'],
    hour_df_filtered['cnt'],
    marker='o',
    linewidth=2,
    color="#FFFFFF"  # Warna putih
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)

# Perbandingan antara pengguna kasual dan terdaftar
st.header('Perbandingan Pengguna Kasual dan Terdaftar')
st.subheader('Jumlah Peminjaman Sepeda')

rentals_by_user_type = day_df_filtered.groupby('weekday')[['casual', 'registered']].sum()

fig, ax = plt.subplots(figsize=(16, 8))
rentals_by_user_type.plot(kind='bar', stacked=True, ax=ax, color=['#FAD02E', '#FFFFFF'])
ax.set_xlabel('Hari Mingguan')
ax.set_ylabel('Jumlah Peminjaman')
ax.set_title('Perbandingan Pengguna Kasual dan Terdaftar')
st.pyplot(fig)

st.caption('Present By Sashi Kirana')



