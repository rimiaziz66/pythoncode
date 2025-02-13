import pandas as pd


df = pd.read_csv(r"C:\Users\tanvi\OneDrive\Desktop\CV 2025\sample_data.csv")

print(df.head())
print(df.loc[0, "Name"])  # Get value at row 0, column "Name"
print(df.iloc[0, 1] )     # Get value at row 0, column index 1
print(df.loc[:, ["Name", "Age"]])  # Select specific columns
print(df.iloc[:, 0:2])  # Select first two columns








