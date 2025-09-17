# streamlit_app.py
import streamlit as st
import pandas as pd

# ========== LOAD DATA ==========
@st.cache_data
def load_data():
    customers = pd.read_csv("customer_features_with_clusters.csv", dtype=str)
    top_products = pd.read_csv("top_products_per_cluster.csv", dtype=str)
    return customers, top_products

customers, top_products = load_data()

# ========== PAGE CONFIG ==========
st.set_page_config(page_title="E-Commerce Customer Insights", page_icon="🛒", layout="wide")

# ========== HEADER ==========
st.title("🛍️ E-Commerce Customer Segmentation & Recommendations")
st.markdown("Explore customer profiles, behaviors, and personalized product recommendations.")

# ========== SIDEBAR ==========
st.sidebar.header("Search Customer")
customer_id = st.sidebar.text_input("Enter Customer ID")
if st.sidebar.checkbox("Pick from list"):
    customer_id = st.sidebar.selectbox("Select customer_id", customers["CustomerID"].unique())

# ========== MAIN BODY ==========
if customer_id:
    match = customers[customers["CustomerID"].astype(str) == str(customer_id)]
    if match.empty:
        st.error("❌ Customer not found. Try another ID.")
    else:
        cust = match.iloc[0]

        # ---- Customer Profile Cards ----
        st.subheader(f"📊 Customer Profile — ID: {cust['CustomerID']}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Cluster", cust["Cluster"])
            st.metric("Recency (days)", cust["Recency"])
            st.metric("Frequency (# orders)", cust["Frequency"])
        with col2:
            st.metric("Monetary (£)", cust["Monetary"])
            st.metric("Total Quantity", cust["TotalQuantity"])
            st.metric("Avg Order Value (£)", cust["AvgOrderValue"])
        with col3:
            st.metric("Unique Products", cust["UniqueProducts"])
            st.metric("Avg Days Between Purchases", cust["AvgDaysBetweenPurchases"])
            st.metric("Fav Shopping Day", cust["FavShoppingDay"])

        # ---- Additional Insights ----
        st.markdown("### 🕒 Shopping Patterns")
        st.write(f"**Fav Shopping Hour:** {cust['FavShoppingHour']}")
        st.write(f"**Is UK Customer:** {'Yes' if cust['Is_UK']=='1' else 'No'}")

        col4, col5 = st.columns(2)
        with col4:
            st.metric("Monthly Spend Mean (£)", cust["MonthlySpendMean"])
        with col5:
            st.metric("Monthly Spend STD", cust["MonthlySpendSTD"])

        st.markdown(f"**Spending Trend:** {cust['SpendingTrend']}")

        # ---- Recommendations ----
        st.subheader("🎯 Product Recommendations")
        recs = top_products[top_products["Cluster"].astype(str) == str(cust["Cluster"])]

        if recs.empty:
            st.info("No recommendations found for this cluster.")
        else:
            st.dataframe(
                recs[["StockCode", "Description", "Quantity", "Rank"]].head(10),
                use_container_width=True
            )

# ---- Show Data Overview ----
st.markdown("---")
st.subheader("🔎 Explore All Customers")
st.dataframe(customers.head(20))
