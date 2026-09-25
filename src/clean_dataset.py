from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "car_data_raw.csv"
OUTPUT = ROOT / "data" / "car_data_cleaned.csv"

df = pd.read_csv(INPUT)

df.columns = (
    df.columns.str.strip()
      .str.replace(" ", "_", regex=False)
      .str.replace(r"[^A-Za-z0-9_]", "", regex=True)
)

for col in ["Car_Name", "Fuel_Type", "Selling_type", "Transmission"]:
    df[col] = df[col].astype("string").str.strip()

df["Car_Name"] = df["Car_Name"].str.replace(r"\s+", " ", regex=True)
df["Fuel_Type"] = df["Fuel_Type"].str.title()
df["Selling_type"] = df["Selling_type"].str.title()
df["Transmission"] = df["Transmission"].str.title()

df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")
df["Selling_Price"] = pd.to_numeric(df["Selling_Price"], errors="coerce")
df["Present_Price"] = pd.to_numeric(df["Present_Price"], errors="coerce")
df["Driven_kms"] = pd.to_numeric(df["Driven_kms"], errors="coerce").astype("Int64")
df["Owner"] = pd.to_numeric(df["Owner"], errors="coerce").astype("Int64")

df = df.drop_duplicates().reset_index(drop=True)

# If missing values are introduced by type coercion, fill them transparently.
for col in df.columns:
    if df[col].isna().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode(dropna=True).iloc[0])

df.to_csv(OUTPUT, index=False)
print(f"Saved {len(df)} cleaned rows to {OUTPUT}")
