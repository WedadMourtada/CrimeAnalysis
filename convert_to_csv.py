import pandas as pd
import os

print("Starting citywide.xlsx conversion test...")  # Force visible output

# Convert just one file to test
xlsx_path = os.path.join('datasets', 'citywide.xlsx')
csv_path = os.path.join('datasets', 'citywide.csv')

# Check available sheets first
xls = pd.ExcelFile(xlsx_path)
print("Sheets:", xls.sheet_names)

# Read the correct sheet by name or index
df = pd.read_excel(xlsx_path, sheet_name=0)
df.to_csv(csv_path, index=False)
print(f"Converted citywide.xlsx to citywide.csv")
