import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

def million_formatter(x, pos):
        return f'{x/1e6:.1f}M'

st.title("E-commers Performance Analysis Dashboard")

product_df = pd.read_csv("dashboard/main_data_product.csv")
city_df = pd.read_csv("dashboard/main_data_city.csv")
rfm_df = pd.read_csv("dashboard/main_data_RFM.csv")

product_by_sales = product_df.sort_values(by="total_sold_x", ascending=False).head(5)
product_by_revenue = product_df.sort_values(by="total_revenue", ascending=False).head(5)
top_city_by_sales =  city_df.sort_values(by="total_sales_x", ascending=False).head(5)
top_city_by_revenue = city_df.sort_values(by="total_revenue", ascending=False).head(5)
top_rfm_recency = rfm_df.sort_values(by="Recency", ascending=False).head(5)
top_rfm_frequency = rfm_df.sort_values(by="Frequency", ascending=False).head(5)
top_rfm_monetary = rfm_df.sort_values(by="Monetary", ascending=False).head(5)


tab1, tab2, tab3 = st.tabs(["Analisis Produk", "Analisis Kota", "Analisiss RFM"])

with tab1 : 
    st.header("Top 5 Product : Sales vs Revenue")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Berdasarkan Sales")


        fig1, ax1 = plt.subplots(figsize=(10, 6))

        sns.barplot(
            data=product_by_sales,
            x="total_sold_x",
            y="product_category_name_english",
            ax=ax1
        )

        ax1.set_title('Top 5 Best-Selling Product Categories', fontsize=14)
        ax1.set_xlabel('Total Sold')
        ax1.set_ylabel('Product Category')

        fig1.tight_layout()
        st.pyplot(fig1)



    with col2:
        st.subheader("Berdasarkan Revenue")
        
        fig2, ax_prod = plt.subplots(figsize=(10, 6))

        sns.barplot(
            data=product_by_revenue,
            x='total_revenue',
            y='product_category_name_english',
            palette='magma',
            ax=ax_prod
)

        ax_prod.bar_label(ax_prod.containers[0], padding=5, fmt='{:,.0f}', fontsize=10)
        ax_prod.xaxis.set_major_formatter(FuncFormatter(million_formatter))
        ax_prod.set_title('Top 5 Best-revenue Product Categories', fontsize=14)
        ax_prod.set_xlabel('Total Revenue')
        ax_prod.set_ylabel('Product Category')

        fig2.tight_layout()
        st.pyplot(fig2)

    with st.expander("Insight"):
        st.write(
        """Dari vvisualisasi diatas, kita bisa melihat bahwa produk dengan penjualan terbanyak  tidak berarti menjadi produk paling memberikan revenue yang besar.

        kita bisa melihat ada top 5 produk dengan penjualan terbanyak dan produk dengan revenue terbesar:

        kita mulai dengan produk dengan penjualan terbesar berada di kategori bed/bath/table yang merupakan kumpulan dari barang=barang yang ada di rumah khususnya di kamar, kamar mandi, dan furniture.

        yang kedua adalah produk dengan revenue teresar justru ada di kategori kesehatan dan kecantikan , produk-produk body care menjadi produk dengan revenue tertinggi ini bisa menjadi indikasi bahwasan nya nilai barang dari produk kesehatan lebih tinggi dari produk-produk rumah taangga."""
    )

    with st.expander("Conclusion"):
        st.write(
        """ Dari dua insight tersebut saya menyarankan untuk meningkatkan promosi terhadap produk-produk dengan nilai revenue yang cukup besar karena jika berhasil di tingkatkan maka profit yang akan dihasilkan juga semakin bagus, lalu untuk prrduk dengan jumlah penjualan terbanyak bisa lebih di maintance dari segi stok karrena produk ini bisa menjadi penarik perhatian para customer"""
    )


with tab2 :
    st.header("Top 5 City : Sales vs Revenue")
    col1, col2 = st.columns(2)

    with col1 :
        st.subheader("Berdasarkan Sales")

        fig1, ax1 = plt.subplots(figsize=(10, 6))

        sns.barplot(
            data=top_city_by_sales,
            x='customer_city',
            y='total_sales_x',
            ax=ax1
            
)
        
        ax1.set_title('Top 5 Cities by Total Sales')
        ax1.set_xlabel('City')
        ax1.set_ylabel('Total Item Sold')


        st.pyplot(fig1)


    with col2 :
        st.subheader("Berdasarkan Revenue")

        fig2, ax2 = plt.subplots(figsize=(10, 6))

        sns.barplot(
            data=top_city_by_revenue,
            x='customer_city',
            y='total_revenue',
            palette='magma',
            ax=ax2
        
        )

    
        ax2.bar_label(ax2.containers[0], padding=5, fmt='{:,.0f}', fontsize=10)
        ax2.yaxis.set_major_formatter(FuncFormatter(million_formatter))
        ax2.set_title("Top 5 City by Revenue")
        ax2.set_xlabel("City")
        ax2.set_ylabel("Total Revenue")

    
        st.pyplot(fig2)


    with st.expander("Insight"):
        st.write(
            """Dari visualisasi di atas kita bisa melihat bahwa kota sao paulo merupakan kota dengan jumlah penjualan dan revenue terbesar.
            
            dari sini saya menahami bahwa faktor populasi menjadi faktor utama untuk dapat mendapatkan kemungkinan costumer lebih banyak daripada kota yang lebih sedikit populasi nya.
            
            dari dua visualisasi itu juga pusat kota atau kota besar memang mendominasi dalam market penjualan online karena meleknya para penduduk terhadap teknologi menjadikan e-commers menjadi solusi untuk dapat berbelanja tanpa harus keluar rumah.
            
            """
        )

    with st.expander("Conclusion"):
        st.write(
            """dari insight yang sudah saya sampaikan saya mendapatkan sebuah kesimpulan bahwa tidak bisa di pungkiri kepadatan penduduk disertai kemampuan pnduduk dalam menggunakan teknologi menjai faktor penting bagi keberlangungan bisnis e-commers,
            saya bisa mmberikan saran untuk terus meningkatkan pelayanan dan pengalaman customer dengan menyesuaikan tren yang sedang ramai di kota tetentu agar tetap update , namun akan lebih baik jika peusahaan ini bisa menjadi pusat tren agar semakin leluasa dalam market.
            lalu untuk daerah lain pun perlu ditingkatkan dari segi awarnes custome terhadap produk-produk unggulan perusahaan agar bisa mendapat lebih banyak customer 
            """
        )




with tab3:
    st.header("Top Customer : Rencecy vs Frequency vs Monetary") 
    cols1, cols2, cols3 = st.columns(3)

    with cols1 :
        st.subheader("Berdasarkan Recency")

        fig1, ax1 = plt.subplots(figsize=(12, 6))

        sns.barplot(
            data=top_rfm_recency,
            x="Recency",
            y=top_rfm_recency['customer_unique_id'].str[-5 :],
            ax=ax1

        )

        ax1.set_title("Top 5 Customer by Recency")
        ax1.set_xlabel("Recency")
        ax1.set_ylabel("Customeer ID")

        st.pyplot(fig1)

    with cols2 :
        st.subheader("Berdasarkan Frequency")

        fig2, ax2 = plt.subplots(figsize=(12, 6))

        sns.barplot(
            data=top_rfm_frequency,
            x="Frequency",
            y=top_rfm_frequency['customer_unique_id'].str[-5 :],
            palette='magma',
            ax=ax2

        )

        ax2.set_title("Top 5 Customer by Frequency")
        ax2.set_xlabel("Frequency")
        ax2.set_ylabel("Customer ID")

        st.pyplot(fig2)    

    with cols3:
        st.subheader("Berdasaarkan Monetary")

        fig3, ax3 = plt.subplots(figsize=(12, 6))

        sns.barplot(
            data=top_rfm_monetary,
            x="Monetary",
            y=top_rfm_monetary['customer_unique_id'].str[-5 :],
            palette='rocket',
            ax=ax3

        )

        ax3.set_title("Top 5 Customer by Monetary")
        ax3.set_xlabel("Monetary")
        ax3.set_ylabel("Customer ID")

        st.pyplot(fig3)

    with st.expander("Insight"):
        st.write(
        """1. Tantangan Retensi pada High-Spender

Berdasarkan visualisasi Monetary dan Frequency, terdapat anomali yang cukup menarik: pelanggan yang memberikan kontribusi pendapatan terbesar (Top Monetary) justru mayoritas hanya melakukan satu kali transaksi saja. Hal ini menunjukkan bahwa bisnis kita sangat bergantung pada pembelian bernilai tinggi yang sifatnya "sekali beli" (one-off purchase), bukan pada loyalitas jangka panjang. Kita kehilangan potensi pendapatan berulang dari pelanggan-pelanggan kaya ini.

​   2. Risiko Kehilangan Pelanggan Utama

Jika melihat grafik Recency, terlihat bahwa banyak pelanggan "terbaik" kita memiliki rentang waktu transaksi terakhir yang sangat jauh, bahkan mencapai angka 700 hari lebih. Secara logis, pelanggan ini sudah masuk kategori at risk atau bahkan sudah tidak aktif (churn). Sangat krusial untuk menganalisis mengapa setelah transaksi besar tersebut, mereka tidak pernah kembali berinteraksi dengan platform selama hampir dua tahun.

​   3.  Karakteristik "Single-Transaction" yang Dominan

Dominasi angka 1 pada grafik Frequency di hampir semua top customer mengonfirmasi bahwa ekosistem produk kita saat ini belum berhasil menciptakan habit belanja rutin. Pelanggan datang untuk mencari produk spesifik, melakukan transaksi, dan pergi tanpa alasan untuk kembali. Hal ini mengindikasikan perlunya program loyalitas atau strategi cross-selling yang lebih personal untuk meningkatkan frekuensi belanja."""
        )

    with st.expander("Conclusion"):
        st.write(
            """dari semua insight tersebut kita bisa mengambil kesimpulan untuk meningkatkan kepuasan customer agar customer kita menjad customer yang lebih loyal dan melakuan transaksi lebih sering"""
        )

