import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from matplotlib.ticker import FuncFormatter

def million_formatter(x, pos):
        return f'{x/1e6:.1f}M'

st.title("E-commers Performance Analysis Dashboard")

product_df = pd.read_csv("dashboard/main_data_product.csv")
city_df = pd.read_csv("dashboard/main_data_city.csv")
rfm_df = pd.read_csv("dashboard/main_data_RFM.csv")

product_by_sales = product_df.groupby('product_category_name_english').total_sold_x.sum().sort_values(ascending=False).head(5).reset_index()
product_by_revenue = product_df.groupby('product_category_name_english').total_revenue.sum().sort_values(ascending=False).head(5).reset_index()
top_city_by_sales =  city_df.groupby('customer_city').total_sales_x.sum().sort_values(ascending=False).head(5).reset_index()
top_city_by_revenue = city_df.groupby('customer_city').total_revenue.sum().sort_values(ascending=False).head(5).reset_index()
top_rfm_recency = rfm_df.sort_values(by="Recency", ascending=False).head(5)
top_rfm_frequency = rfm_df.sort_values(by="Frequency", ascending=False).head(5)
top_rfm_monetary = rfm_df.sort_values(by="Monetary", ascending=False).head(5)

for df in [product_df, city_df] :
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['year'] = df['order_purchase_timestamp'].dt.year

with st.sidebar :
    st.title('E-commers Control')

    years = sorted(product_df['year'].dropna().unique().astype(int))

    selected_year = st.selectbox(label="Pilih Tahun Analisis", options=years)

    filtered_product = product_df[product_df['year'] == selected_year]
    filtered_city = city_df[city_df['year'] == selected_year]

    st.header(f'Analisis E-commers Tahun {selected_year}')

total_product_sold_all_time = product_df['total_sold_x'].sum()
total_product_revenue_all_time = product_df['total_revenue'].sum()

st.header("E-commers Performance Overview (2016-2018)")

col_global1, col_global2 = st.columns(2)

with col_global1 :
    st.metric(label="Total Product Sold (All Time)", value=f"{total_product_sold_all_time:,}")

with col_global2 :
    st.metric(label="Total Revenue All Time", value=f"$ {total_product_revenue_all_time:,.2f}")

st.write("### Tren of Product Sales  (2016-2018)")

product_df["month_year"] = product_df["order_purchase_timestamp"].dt.to_period('M').astype(str)

trend_df = product_df.groupby('month_year')['total_sold_x'].sum().reset_index()

st.line_chart(
    data=trend_df,
    x="month_year",
    y="total_sold_x"
)

st.markdown("---")

total_product_sold = filtered_product['total_sold_x'].sum()
total_product_revenue = filtered_product['total_revenue'].sum()

st.subheader(f"E-commers Performance for {selected_year}")
col_metric1, col_metric2 = st.columns(2)

with col_metric1 :
    st.metric(label="Total Product Sold", value=f"{total_product_sold:,}")

with col_metric2 :
    st.metric(label="Total Revenue", value=f"$ {total_product_revenue:,.2f}")

trend_bulanan = filtered_product.resample('M', on='order_purchase_timestamp').total_sold_x.sum().reset_index()
trend_bulanan['month_name'] = trend_bulanan['order_purchase_timestamp'].dt.strftime('%B')

st.write(f"### Trend for {selected_year}")

st.line_chart(
    data=trend_bulanan,
    x='order_purchase_timestamp',
    y='total_sold_x'
)



st.divider()

tab1, tab2, tab3 = st.tabs(["Analisis Produk", "Analisis Kota", "Analisiss RFM"])

with tab1 : 
    st.header(f"Top 5 Product {selected_year}")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Berdasarkan Sales")

        product_by_sales = filtered_product.groupby('product_category_name_english').total_sold_x.sum().sort_values(ascending=False).head(5).reset_index()


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
        
        product_by_revenue = filtered_product.groupby('product_category_name_english').total_revenue.sum().sort_values(ascending=False).head(5).reset_index()

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




with tab2 :
    st.header(f"Top 5 City {selected_year}")
    col1, col2 = st.columns(2)

    with col1 :
        st.subheader("Berdasarkan Sales")

        top_city_by_sales = filtered_city.groupby('customer_city').total_sales_x.sum().sort_values(ascending=False).head(5).reset_index()

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

        top_city_by_revenue = filtered_city.groupby('customer_city').total_revenue.sum().sort_values(ascending=False).head(5).reset_index()

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

