import pandas as pd 
def clean_data(filepath):
    df=pd.read_csv(filepath)
    df['Order Date']=pd.to_datetime(df['Order Date'])
    df.drop_duplicates(inplace=True)
    df['Sales'].fillna(df['Sales'].mean(), inplace=True)
    df['Profit'].fillna(df['Profit'].mean(), inplace=True)
    df['Year']=df['Order Date'].dt.year
    df['Month']=df['Order Date'].dt.month
    return df 
if __name__ == "__main__":
    df=clean_data(r"C:\Users\kumar\OneDrive\Desktop\AMAZON_Sales\data\sales_data.csv") 
    print(df.head())                                                                                  
   