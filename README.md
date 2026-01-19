
# Product Recommendation and Customer Clustering Analysis

## Project Overview

This project applies machine learning techniques to segment customers based on purchasing behavior and generate personalized product recommendations. The objective is to help the business improve customer engagement, increase average order value, and drive revenue through targeted marketing and cross-selling strategies.

Stakeholders include marketing teams, product managers, sales leaders, and data analysts responsible for customer growth and retention.

---

## Problem Statement

As the customer base grows, delivering personalized experiences becomes increasingly difficult. The business seeks to answer the following questions:

* Can customers be grouped based on similar purchasing behavior?
* What customer segments exist within the dataset?
* How can product recommendations be tailored to each segment?
* How can clustering insights be used to improve marketing campaigns and sales strategies?

---

## Data Structure

The dataset contains transactional and customer-level data, including:

* **Customer:** Customer ID, demographics (if available)
* **Transaction:** Order ID, order date, quantity, purchase frequency
* **Product:** Product category, product ID, price
* **Derived Features:** Total spend, average order value, recency, frequency

[<img width="900" alt="customer-clustering" src="images/customer_clusters.png" />](https://customer-recommendation-dashboard-kxchadoqnwhbgxz8v7fhbp.streamlit.app/)

---

## Data Analysis & Modeling Process

1. **Data Cleaning:** Removed duplicates, handled missing values, and standardized formats.
2. **Feature Engineering:** Created RFM (Recency, Frequency, Monetary) metrics and purchase behavior indicators.
3. **Exploratory Data Analysis:** Analyzed customer spending patterns, frequency distribution, and product popularity.
4. **Customer Clustering:**

   * Algorithm used: K-Means
   * Optimal clusters determined using the Elbow Method and Silhouette Score
5. **Product Recommendation:**

   * Generated recommendations based on top products per cluster
   * Used similarity in purchasing behavior to suggest relevant products

---

## Key Findings / Insights

* **Customer Segments Identified:**

  * High-Value Customers: Frequent buyers with high spend
  * Occasional Customers: Moderate spend and low frequency
  * Price-Sensitive Customers: Low spend, high responsiveness to discounts

* **Spending Patterns:**
  High-value customers contribute a disproportionate share of total revenue despite being fewer in number.

* **Product Preferences:**
  Each cluster shows distinct product category preferences, enabling targeted recommendations.

---

## Recommendations

1. **Personalized Marketing Campaigns**
   Design cluster-specific promotions to increase conversion and engagement.

2. **Cross-Selling and Upselling**
   Recommend premium or complementary products to high-value customers to increase average order value.

3. **Retention Strategy for High-Value Customers**
   Introduce loyalty programs and exclusive offers to retain top-performing segments.

4. **Reactivation of Low-Frequency Customers**
   Use targeted discounts and reminders to convert occasional buyers into repeat customers.

---

## Tools and Skills Applied

* **Data Cleaning & Feature Engineering:** Python (pandas, numpy)
* **Clustering:** K-Means, Elbow Method, Silhouette Score
* **Product Recommendation Logic:** Rule-based and similarity-driven approaches
* **Exploratory Data Analysis:** matplotlib, seaborn
* **Business Insight Interpretation:** Customer segmentation and marketing analytics

---

## Access the Project

* [Dataset](dataset/customer_transactions.csv)
* [Jupyter Notebook](notebooks/customer_clustering_recommendation.ipynb)
* [Cluster Visualization](images/customer_clusters.png)

---

## Business Value

This project demonstrates how unsupervised learning can be used to uncover hidden customer segments and translate them into actionable product recommendations. The approach supports data-driven marketing, improves customer experience, and increases revenue potential.

---


