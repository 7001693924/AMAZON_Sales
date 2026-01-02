from dataCleaning import clean_data
from eda import perform_eda
from visualization import (
    plot_monthly_sales,
    plot_category_sales,
    plot_profit_heatmap
)
from forecasting import sales_forecast

def main():
    df = clean_data(r"C:\Users\kumar\OneDrive\Desktop\AMAZON_Sales\data\sales_data.csv")

    insights = perform_eda(df)

    print("Total Sales:", insights['total_sales'])
    print("Total Profit:", insights['total_profit'])
    print("\nTop Categories:\n", insights['top_categories'])
    print("\nTop Products:\n", insights['top_products'])
    print("\nProfit by State:\n", insights['state_profit'])

    plot_monthly_sales(insights['sales_by_month'])
    plot_category_sales(insights['top_categories'])
    plot_profit_heatmap(df)

    sales_forecast(df)

if __name__ == "__main__":
    main()
