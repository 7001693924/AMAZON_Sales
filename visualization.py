import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def plot_monthly_sales(sales_by_month):
    plt.figure()
    sns.lineplot(
        x=sales_by_month.index,
        y=sales_by_month.values,
        color='red'
    )
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.show()


def plot_category_sales(category_sales):
    plt.figure()
    sns.barplot(
        x=category_sales.index,
        y=category_sales.values,
        color='yellow'
    )
    plt.title("Category-wise Sales")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.show()


def plot_profit_heatmap(df):
    pivot = df.pivot_table(
        values='Profit',
        index='State',
        columns='Category',
        aggfunc='sum'
    )
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="coolwarm")
    plt.title("Profit Heatmap")
    plt.show()
