# Data Cleaning Project — Car Dataset

## Dataset Selected

**Vehicle Dataset from CarDekho** — a public used-car dataset commonly distributed through Kaggle.

Source: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

This repository demonstrates a basic data-quality and cleaning workflow using **Python and Pandas**.

## Objective

Identify and fix:

- Missing values
- Duplicate records
- Incorrect data types
- Inconsistent text/categorical values

Then save the cleaned dataset and document every change.

## Dataset Summary

The supplied dataset contains **301 rows and 9 columns** before cleaning.

Columns:

| Column | Description |
|---|---|
| `Car_Name` | Car/model name |
| `Year` | Manufacturing year |
| `Selling_Price` | Selling price in lakh |
| `Present_Price` | Present/ex-showroom price in lakh |
| `Driven_kms` | Kilometers driven |
| `Fuel_Type` | Fuel type |
| `Selling_type` | Dealer or Individual |
| `Transmission` | Manual or Automatic |
| `Owner` | Number of previous owners |

## Data Quality Findings

### 1. Missing values

No missing values were found in the original dataset.

### 2. Duplicate records

**2 exact duplicate rows** were found and removed.

The duplicate records are available in:

`reports/duplicate_records.csv`

### 3. Incorrect data types

The source data was inspected and numeric columns were explicitly converted to appropriate numeric types:

- `Year` → integer
- `Selling_Price` → float
- `Present_Price` → float
- `Driven_kms` → integer
- `Owner` → integer

This makes the data type expectations explicit and reproducible.

### 4. Inconsistent values

Text fields contained formatting inconsistencies such as extra whitespace in car names.

Cleaning included:

- Leading/trailing whitespace removal
- Repeated internal whitespace normalization in `Car_Name`
- Standardized capitalization for `Fuel_Type`
- Standardized capitalization for `Selling_type`
- Standardized capitalization for `Transmission`
- Standardized column names

The allowed categorical values were checked after cleaning.

## Cleaning Steps

The cleaning process was:

1. Load the raw CSV with Pandas.
2. Inspect shape, data types, missing values, and duplicates.
3. Standardize column names.
4. Strip whitespace from text fields.
5. Normalize repeated spaces in car names.
6. Standardize categorical capitalization.
7. Convert numeric columns to appropriate numeric data types.
8. Remove exact duplicate records.
9. Check for missing values created during type conversion.
10. Validate the final dataset.
11. Export the cleaned CSV.

## Before vs After

| Metric | Before | After |
|---|---:|---:|
| Rows | 301 | 299 |
| Columns | 9 | 9 |
| Missing values | 0 | 0 |
| Exact duplicate rows | 2 | 0 |

## Repository Structure

```text
car-dataset-cleaning/
│
├── data/
│   ├── car_data_raw.csv
│   └── car_data_cleaned.csv
│
├── reports/
│   ├── data_quality_report.txt
│   ├── data_dictionary.csv
│   └── duplicate_records.csv
│
├── src/
│   └── clean_dataset.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Reproduce

Install the dependency:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/clean_dataset.py
```

The cleaned file will be written to:

```text
data/car_data_cleaned.csv
```

## Tools Used

- Python
- Pandas
- CSV
- GitHub

## Notes

The raw dataset is included for reproducibility. If the original public dataset has redistribution restrictions, remove the raw file before publishing and link to the original source instead.

## Author

**Brahmaiah Chereddy**

Data Analyst Portfolio Project
