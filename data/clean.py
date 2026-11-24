# Fill feels the most ambiguous because filling missing value could change the accuracy. I'd want to see how much the dataset was changed with these filled values. 
# I think if someone who didn't know the dataset read my script, they'd understand why I made each decision.
# After running describe(), the most important thing I noticed about the dataset that I didn't expect was the placeholder values of the mean in quantity_sold.



# Exercise 1
# 3 data quality issues I observed in messy_sales.csv is: Order ID has missing values, Quantity sold has missing values, and Customer ID has missing values

import pandas as pd

df = pd.read_csv("messy_sales.csv")

df.info()
print(df.isnull().sum())

# Exercise 2
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.columns.tolist())

# Exercise 3
print("Shape before:", df.shape)

df = df.dropna(subset=["order_id", "order_date"])

df["quantity_sold"] = df["quantity_sold"].fillna(
    df["quantity_sold"].mean()
)
# Filled missing values with the mean
# Helps save the orders without having to remove them

# Exercise 4
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce"
)

print("Dates converted to NaT:", df["order_date"].isna().sum())

df["unit_price"] = (
    df["unit price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

df["quantity_sold"] = df["quantity_sold"].astype(int)

df["revenue"] = (
    df["unit_price"] * df["quantity_sold"]
).round(2)

print(df.dtypes)

# Exercise 5
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)

# Exercise 6
print(df.describe())

# The maximum quantity_sold is not a realistic order. Most likely, it is a placeholder value.
# The mean quantity_sold is much higher than the median. The placeholder value from quantity_sold is making the mean higher.
# Negative revenue is meaning that customers probably returned the items. 

df = df[df["quantity_sold"] != 9999]
print("Shape after removing placeholder quantities:", df.shape)

# Exercise 7
df.to_csv("data/cleaned_sales.csv", index=False)

df_check = pd.read_csv("data/cleaned_sales.csv")
df_check.info()

df = pd.read_csv(
    "data/cleaned_sales.csv",
    parse_dates=["order_date"]
)
df.info()





