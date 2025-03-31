import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

df = pd.read_csv("DataSet/OnlineSalesData.csv", encoding="utf-8")

df["Units Sold"] = df["Units Sold"].fillna(0)
df["Unit Price"] = df["Unit Price"].fillna(df["Unit Price"].median())
df["Total Revenue"] = df["Total Revenue"].fillna(df["Units Sold"] * df["Unit Price"])
df.dropna(subset=["Transaction ID", "Date"], inplace=True)

df.drop_duplicates(inplace=True)

df["Transaction ID"] = df["Transaction ID"].astype(str)
df["Units Sold"] = df["Units Sold"].astype(int)
df["Unit Price"] = df["Unit Price"].astype(float)
df["Total Revenue"] = df["Total Revenue"].astype(float)
df["Date"] = pd.to_datetime(df["Date"])

cnn = sqlite3.connect("Sales.db")
df.to_sql("OnlineSalesData", cnn, if_exists="replace", index=False)

query = """
SELECT Region, SUM("Total Revenue") AS Total_Sales
FROM OnlineSalesData
GROUP BY Region
ORDER BY Total_Sales DESC
"""
df_sales_by_region = pd.read_sql(query, cnn)

query = """
SELECT "Product Name", SUM("Units Sold") AS Total_Units
FROM OnlineSalesData
GROUP BY "Product Name"
ORDER BY Total_Units DESC
LIMIT 10
"""
df_top_products = pd.read_sql(query, cnn)

query = """
SELECT strftime ('%Y-%m', Date) AS MONTH, SUM ("Total Revenue") AS Monthly_Revenue
FROM OnlineSalesData
GROUP BY Month
ORDER BY Month
"""
df_monthly_revenue = pd.read_sql(query, cnn)

query = """
SELECT "Payment Method", COUNT(*) AS Transactions
FROM OnlineSalesData
GROUP BY "Payment Method"
ORDER BY Transactions DESC
"""
df_payment_methods = pd.read_sql(query, cnn)

plt.figure(figsize=(10, 5))
sns.barplot(data=df_sales_by_region, x="Region", y="Total_Sales")
plt.title("Total de vendas por Região")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
sns.barplot(data=df_top_products, x="Total_Units", y= "Product Name", palette="coolwarm")
plt.title("Top 10 produtos mais vendidos")
plt.show()

plt.figure(figsize=(10, 5))
sns.lineplot(data=df_monthly_revenue, x="MONTH", y="Monthly_Revenue", marker="o")
plt.title("Receita Mensal")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(df_payment_methods["Transactions"], labels=df_payment_methods["Payment Method"], autopct="%1.1f%%",startangle=90,
        colors=sns.color_palette("viridis", len(df_payment_methods)))
centre_circle = plt.Circle((0,0),0.70,fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Distribuição de Métodos de Pagamento", fontsize=14)
plt.tight_layout()
plt.show()