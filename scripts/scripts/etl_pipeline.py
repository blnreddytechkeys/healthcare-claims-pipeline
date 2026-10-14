import pandas as pd
from pathlib import Path

RAW_DATA = Path("data/sample_claims.csv")
CLEAN_DATA = Path("data/cleaned_claims.csv")

def extract(file_path):
    print("Extracting data...")
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} records")
    return df

def transform(df):
    print("Transforming data...")
    df['claim_date'] = pd.to_datetime(df['claim_date'])
    df['status'] = df['status'].str.title()
    df['is_high_value'] = df['claim_amount'] > 400
    df = df.drop_duplicates(subset=['claim_id'])
    print("Transformation completed")
    return df

def load(df, output_path):
    print("Loading data...")
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

def main():
    raw_df = extract(RAW_DATA)
    clean_df = transform(raw_df)
    load(clean_df, CLEAN_DATA)
    
    print("\n--- Summary ---")
    print(clean_df['status'].value_counts())
    print(f"\nTotal Claim Amount: ${clean_df['claim_amount'].sum():,.2f}")

if __name__ == "__main__":
    main()