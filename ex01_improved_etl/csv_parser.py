import pandas as pd
from datetime import date

def nowdate():
    return date.today().strftime('%Y%m%d')

def filter_entries_with_credit_card(df):
    return df[['name', 'creditcard']].dropna(subset=['creditcard'], how='any')

def json_to_csv(jsonfile):
    with open(jsonfile, encoding='utf-8') as inputfile:
        data = pd.read_json(inputfile)
        
    df_filtered = filter_entries_with_credit_card(data)

    if not df_filtered.empty:
        csv_filename = f"ex01_improved_etl/exports/{nowdate()}.csv"
        df_filtered.to_csv(csv_filename, encoding='utf-8', index=False)

def main():
    json_to_csv('ex01_improved_etl/input/data.json')

if __name__ == "__main__":
    main()
