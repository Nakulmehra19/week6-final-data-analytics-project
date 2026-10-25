# Superstore Sales & Profit Analysis

## 1. Project Overview

This project focuses on analyzing the Sample Superstore dataset using Python, Exploratory Data Analysis (EDA), data visualization, and Power BI. The main objective is to understand sales performance, profitability, regional trends, and customer segment behavior through data-driven analysis.

The project includes data cleaning, statistical analysis, visualizations, and an interactive Power BI dashboard to support business decision-making.

## 2. Problem Statement

Businesses need to understand their sales and profit patterns to make better decisions. Without proper data analysis, it can be difficult to identify high-performing categories, low-performing regions, customer preferences, and opportunities for improvement.

This project analyzes Superstore sales data to identify important business insights and provide practical recommendations.

## 3. Dataset Description

- **Dataset:** Sample Superstore
- **File:** `Sample - Superstore-Cleaned.xlsx`
- **Number of records:** 9,994 rows
- **Number of columns:** 21
- **Format:** Excel (`.xlsx`)

The dataset contains information about orders, customers, products, sales, profit, discounts, quantity, regions, and order dates.

## 4. Tools and Technologies Used

- **Python:** Data processing and analysis
- **Pandas:** Data manipulation and cleaning
- **NumPy:** Numerical operations
- **Matplotlib:** Data visualization
- **Seaborn:** Statistical visualization
- **Jupyter Notebook:** Exploratory analysis
- **Power BI:** Interactive dashboard creation
- **Microsoft Excel:** Dataset storage and inspection
- **Git and GitHub:** Version control and project hosting

## 5. Data Cleaning and Preparation

Data preparation was performed before analysis to improve data quality and usability.

The preparation process included:

- Loading and inspecting the dataset.
- Checking the dataset's rows, columns, and data types.
- Examining missing values and duplicate records.
- Checking numerical and categorical columns.
- Preparing the dataset for exploratory analysis and visualization.

The cleaned dataset was used for further analysis and dashboard development.

## 6. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the structure of the dataset and discover meaningful patterns.

The analysis focused on:

- Sales and profit distribution.
- Category-wise sales performance.
- Region-wise sales performance.
- Monthly sales trends.
- Customer segment contribution.
- Relationships among numerical variables.
- Distribution of sales, profit, quantity, and discount.

The EDA results helped identify patterns and areas requiring further business investigation.

## 7. Data Visualizations

The project contains visualizations generated using Python.

Available visualizations include:

- `sales_by_category.png`
- `sales_by_region.png`
- `monthly_sales_trend.png`
- `correlation_heatmap.png`
- `boxplot_sales.png`
- `boxplot_profit.png`
- `boxplot_quantity.png`
- `boxplot_discount.png`

These charts help explain sales performance, regional differences, monthly trends, numerical distributions, and relationships among variables.

The Python visualization code is available in:

`notebooks/data_visualization.py`

## 8. Power BI Dashboard

An interactive Power BI dashboard was developed to present the main findings in an easy-to-understand format.

**Dashboard file:** `Superstore_Sales_Dashboard.pbix`

The dashboard includes:

- Total Sales KPI
- Total Profit KPI
- Order Count KPI
- Sales by Category
- Sales by Region
- Monthly Sales Trend
- Profit by Sub-Category
- Sales Contribution by Segment
- Order Date, Category, and Region slicers

Users can interact with the slicers to explore sales and profit performance across different dates, categories, and regions.

## 9. Key Business Insights

Based on the dashboard analysis, the following insights were identified:

1. **Category Performance:** Technology has the highest sales among the three main categories, followed by Furniture. Office Supplies has comparatively lower sales.

2. **Regional Performance:** The West region has the highest sales, while the South region has the lowest sales among the regions shown in the dashboard.

3. **Customer Segments:** The Consumer segment contributes approximately 50.56% of sales, Corporate contributes 30.74%, and Home Office contributes 18.70%.

4. **Monthly Sales Trends:** The monthly sales chart shows changes in sales over time. Identifying peak and low-sales months can help improve planning and inventory management.

5. **Sub-Category Profitability:** The Profit by Sub-Category chart helps identify products that contribute more or less to profit. Copiers appear among the stronger profit contributors in the displayed analysis.

## 10. Business Recommendations

Based on the findings, the following recommendations are proposed:

1. **Improve Regional Performance:** Investigate the reasons for lower sales in the South region. Consider customer feedback, product availability, marketing activities, and regional demand before deciding on corrective actions.

2. **Focus on High-Performing Categories:** Maintain suitable inventory for Technology products and evaluate opportunities to increase sales in other categories.

3. **Plan for Sales Trends:** Use monthly sales patterns to improve inventory planning, staffing, andpromotional schedules during high-demand periods.

4. **Monitor Profitability:** Evaluate profit by sub-category and review discounting and costs where profit margins are low.

5. **Use Customer Segmentation:** Develop marketing strategies for Consumer, Corporate, and Home Office customers according to their purchasing patterns.

## 11. Project Structure

```text
week6-final-data-analytics-project/
├── data/
├── notebooks/
│   ├── eda_analysis.py
│   └── data_visualization.py
├── visualizations/
├── data_preparation.py
├── data_analysis.py
├── Superstore_Sales_Dashboard.pbix
└── README.md
```

## 12. How to Use This Project

1. Download or clone this GitHub repository.
2. Install Python and the required libraries.
3. Open the project in VS Code or another Python editor.
4. Ensure the cleaned dataset is available at the expected path.
5. Run the Python analysis and visualization scripts.
6. Open `Superstore_Sales_Dashboard.pbix` in Power BI Desktop to explore the dashboard.

## 13. Conclusion

This project demonstrates how data analytics can transform raw sales data into useful business information. Python was used for data preparation, exploratory analysis, and visualization, while Power BI was used to build an interactive dashboard.

The findings help explain sales performance, compare regions and categories, monitor profitability, and support data-driven business decisions.

---

**Project:** Week 6 Capstone — Data Analytics  
**Dataset:** Sample Superstore  
**Repository:** `week6-final-data-analytics-project`
