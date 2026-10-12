# Sales Data Analysis Using Python and Power BI

## 1. Project Overview

This project analyzes sales transaction data to identify business trends, product performance, regional sales, profitability, customer contributions, and discount patterns.

Python was used for data cleaning, exploratory data analysis, and calculating business metrics. Power BI was used to create an interactive dashboard to visualize key performance indicators and present business insights.

The objective is to transform raw sales data into meaningful information that can support business decision-making.

## 2. Tools and Technologies

- **Python:** Data analysis and data processing
- **Pandas:** Data cleaning, manipulation, and aggregation
- **Matplotlib:** Data visualization
- **Power BI:** Interactive dashboard development
- **DAX:** KPI calculations and measures
- **CSV:** Dataset storage and data exchange
- **Visual Studio Code:** Python development environment

## 3. Dataset Description

The dataset contains 1,000 sales records with 11 original columns.

The columns include:

- `order_id` — Order identifier
- `order_date` — Date of the order
- `customer_id` — Customer identifier
- `product` — Product name
- `region` — Sales region
- `quantity` — Quantity sold
- `category` — Product category
- `unit_price` — Price per unit
- `discount_pct` — Discount percentage
- `sales` — Sales amount
- `profit` — Profit earned

The dataset is used for educational and portfolio purposes.

## 4. Data Cleaning and Preparation Using Python

Pandas was used to inspect and prepare the dataset before analysis.

The following steps were performed:

- Checked for missing values.
- Checked for duplicate records.
- Converted order dates into datetime format.
- Created additional `year`, `month`, and `month_name` columns.
- Prepared the data for grouping and aggregation.
- Exported the processed dataset to a CSV file.

### Data Quality Results

- Total records: 1,000
- Total original columns: 11
- Missing values: 0
- Duplicate rows: 0

## 5. Exploratory Data Analysis Using Python

The dataset was analyzed to understand sales performance and profitability.

The analysis included:

- Overall sales and profit calculations
- Monthly sales trends
- Product-wise sales and profit
- Regional sales and profit
- Top customers by sales
- Discount analysis
- Regional profit margins
- Category performance
- Product profitability

Pandas was used to aggregate the data, and Matplotlib was used to visualize selected trends.

## 6. Power BI Dashboard

An interactive dashboard was developed in Power BI to present the key findings visually.

### Key Performance Indicators (KPIs)

- **Total Sales:** ₹45,765,310
- **Total Profit:** ₹7,385,292.01
- **Total Orders:** 1,000
- **Profit Margin:** 16.14%

### Dashboard Visualizations

**1. Sales by Product — Bar Chart**

Compares sales across products and highlights the highest-selling products.

**2. Sales by Region — Donut Chart**

Shows how total sales are distributed across the North, South, East, and West regions.

**3. Total Sales by Month — Line Chart**

Displays monthly sales fluctuations and helps identify high- and low-performing months.

**4. Profit by Product — Treemap**

Compares the profit contribution of different products, with larger rectangles representing higher profit.

### Dashboard Preview

Add a screenshot of your completed Power BI dashboard to this section.

## 7. Key Business Insights

Based on the analysis of the dataset:

**1. Laptop is the highest-selling product.**

Laptop sales reached ₹21,537,750, making it the leading product by sales value.

**2. August recorded the highest monthly sales.**

August generated ₹5,638,300 in sales, while November recorded the lowest monthly sales at ₹2,652,245.

**3. South generated the highest regional sales.**

The South region recorded sales of ₹12,094,340, the highest among the four regions.

**4. West generated the highest regional profit.**

The West region recorded a total profit of ₹1,958,978.03, demonstrating that the region with the highest sales is not necessarily the region with the highest profit.

**5. Overall profit margin was 16.14%.**

Total profit of ₹7,385,292.01 against total sales of ₹45,765,310 resulted in an overall profit margin of approximately 16.14%.

## 8. Business Value

This project demonstrates how data analysis can help businesses:

- Monitor overall sales and profitability.
- Identify high-performing products.
- Compare regional performance.
- Understand monthly sales trends.
- Evaluate customer contributions.
- Examine discount patterns.
- Present important metrics through an interactive dashboard.

These findings can help guide further investigation into sales strategy, inventory planning, and profitability.

## 9. Conclusion

This project demonstrates an end-to-end data analysis workflow, from preparing sales data using Python and Pandas to creating an interactive Power BI dashboard.

It showcases practical skills in data cleaning, exploratory data analysis, aggregation, visualization, KPI development, and communicating business insights.

## 10. Project Files

- `Sales_analysis.py` — Python analysis script
- `Sales_Analysis_Project.csv` — Original dataset
- `Sales_Analysis_Cleaned.csv` — Processed dataset
- `Sales_Analysis.pbix` — Power BI dashboard file
- `README.md` — Project documentation

## 11. Disclaimer

This dataset is used for educational and portfolio demonstration purposes. The findings are illustrative and should not be interpreted as actual business performance or proof of causal relationships.
