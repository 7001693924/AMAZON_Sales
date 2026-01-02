import matplotlib.pyplot as plt

def sales_forecast(df):
    monthly_sales = (
        df.resample('M', on='Order Date')['Sales']
        .sum()
    )

    forecast = monthly_sales.rolling(window=3).mean()

    plt.figure()
    plt.plot(monthly_sales, label="Actual Sales",color='red')
    plt.plot(forecast, label="3-Month Moving Avg Forecast",color='green')
    plt.title("Amazon Sales Forecasting")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.legend()
    plt.show()

    return forecast
