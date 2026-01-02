import pandas as pd 
def perform_eda(df):
    insights = {}

    insights['total_sales'] = df['Sales'].sum()
    insights['total_profit'] = df['Profit'].sum()

    insights['sales_by_year'] = df.groupby('Year')['Sales'].sum()
    insights['sales_by_month'] = df.groupby('Month')['Sales'].sum()


    insights['top_categories'] = (
        df.groupby('Category')['Sales']
        .sum()
        .sort_values(ascending=False)
    )

    insights['top_products'] = (
        df.groupby('Product Name')['Sales']
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    insights['state_profit'] = df.groupby('State')['Profit'].sum()
    insights['avg_order_value'] = df['Sales'].mean()
    insights['profit_margin'] = (df['Profit'].sum() / df['Sales'].sum()) * 100

    return insights    
