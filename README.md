# Customer-Shopping-Behavior-Analysis
End-to-end customer shopping behavior analysis using Python, SQL, and Power BI.

This project performs an end-to-end analysis of customer shopping behavior using Python, MySQL, and Power BI. The objective is to clean retail transaction data, analyze customer purchasing patterns using SQL, and create an interactive Power BI dashboard that provides actionable business insights.

## Objectives

* Clean and preprocess customer shopping data.
* Perform exploratory data analysis (EDA).
* Load cleaned data into MySQL.
* Analyze customer behavior using SQL queries.
* Visualize insights with an interactive Power BI dashboard.
* Generate business recommendations based on the analysis.

## Tools & Technologies

* **Python** (Pandas)
* **MySQL**
* **Power BI**
* **Git & GitHub**

## Dataset

The dataset contains **3,900 customer records** with **18 attributes**, including:

* Customer ID
* Age
* Gender
* Item Purchased
* Category
* Purchase Amount (USD)
* Location
* Season
* Review Rating
* Payment Method
* Subscription Status
* Previous Purchases
* Shipping Type
* Discount Applied
* Promo Code Used
* Frequency of Purchases


## Project Workflow

### 1. Data Loading

* Imported the customer shopping dataset using Pandas.

### 2. Data Cleaning

* Identified missing values.
* Filled missing values in the **Review Rating** column using the column mean.
* Verified data quality.
* Exported a cleaned dataset.

### 3. SQL Analysis

Performed SQL queries to answer business questions, including:

* Total customers
* Total revenue
* Revenue by product category
* Revenue by gender
* Seasonal sales trends
* Customer purchase behavior
* Payment method distribution

### 4. Power BI Dashboard

Built an interactive dashboard featuring:

* Total Revenue
* Total Customers
* Average Purchase Amount
* Average Review Rating
* Revenue by Category
* Revenue by Gender
* Revenue by Season
* Payment Method Distribution
* Interactive slicers for Gender, Category, Location, and Season

## Key Business Insights

* Clothing generated the highest revenue among all product categories.
* Male customers contributed a larger share of total revenue than female customers.
* Customer spending remained relatively consistent across all four seasons.
* The average purchase amount was approximately **$60**.
* The average customer review rating was **3.75 / 5**, indicating generally positive customer satisfaction.
* Customers used a variety of payment methods, with no single method overwhelmingly dominating purchases.

## Skills Demonstrated

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* SQL Querying
* Business Intelligence
* Data Visualization
* Dashboard Development
* Business Insight Generation


## Repository Structure

Customer-Shopping-Behavior-Analysis
│
├── cleaned_customer_data.csv
├── customer_shopping_behavior.csv
├── customer_behavior_dashboard.pbix
├── customer_behavior_sql_queries.sql
├── Customer_Shopping_Behavior_Analysis.ipynb
├── analysis.py
├── Dashboard_PowerBI.png
├── README.md

## Future Improvements

* Connect Power BI directly to the MySQL database instead of using CSV files.
* Build additional DAX measures and KPIs.
* Add customer segmentation and predictive analytics.
* Publish the dashboard using the Power BI Service.

## Author

**Tansha Varma**

Computer Science Student | Aspiring Data Analyst

**Technologies:** Python • SQL • Power BI • GitHub
