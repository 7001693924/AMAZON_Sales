# Amazon Sales Analytics & Forecasting 📊

## Project Overview
This project analyzes Amazon sales data using Python to extract meaningful business insights and forecast future sales. The goal is to identify trends, top-performing products and categories, state-wise profits, and visualize monthly and yearly sales patterns.

---

## Tech Stack
- **Python**  
- **Pandas** – Data cleaning and analysis  
- **NumPy** – Numerical operations  
- **Matplotlib** – Line charts and plots  
- **Seaborn** – Advanced visualizations  

---

## Key Features
- **Data Cleaning:** Handle missing values, remove duplicates, convert dates, extract month and year features.  
- **Exploratory Data Analysis (EDA):** Calculate total sales and profit, top categories, top products, and state-wise profits.  
- **Visualizations:**  
  - Monthly sales trend (line chart)  
  - Category-wise sales (bar chart)  
  - Profit heatmap by state and category  
- **Forecasting:** 3-month moving average forecast of monthly sales.

---

## Project Structure
Amazon-Sales-Analytics/
├── data/ # CSV dataset
│ └── amazon_sales_2025_timeseries.csv
├── dataCleaning.py # Data cleaning and preprocessing
├── eda.py # Exploratory data analysis
├── visualization.py # Visualizations (line, bar, heatmap)
├── forecasting.py # Moving average sales forecast
├── main.py # Main module to run the project
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/7001693924/Amazon-Sales-Analytics.git
cd Amazon-Sales-Analytics
```
2.Install dependencies:
pip install -r requirements.txt
3.Run the project:
python main.py

## Sample Output
Total Sales: 1149000
Total Profit: 208200

Top Categories:
 Category
Technology         871000
Furniture          186000
Office Supplies     92000
Name: Sales, dtype: int64

Top Products:
 Product Name
iPhone 15        147000
MacBook Air       90000
iPhone 15 Pro     88000
HP Spectre        85000
Dell XPS          79000
Name: Sales, dtype: int64

Profit by State:
 State
California    125500
Florida         8200
Illinois       11500
New York       15200
Texas          34800
Washington     13000
Name: Profit, dtype: int64
Visualizations:

Monthly sales trend (line chart)

Category-wise sales (bar chart)

State-category profit heatmap

Forecasting:

3-month moving average for monthly sales
## Insights

Technology category generated the highest revenue.

California is the most profitable state.

Sales trends peak during certain months (seasonal trend).

Top products contribute the most to revenue.






