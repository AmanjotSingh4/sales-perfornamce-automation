import pandas as pd

def clean_data(df):
    """
    Cleans and preprocesses the sales dataset.
    """

    # Convert dates
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

    # Remove duplicates
    df = df.drop_duplicates()

    # Drop rows missing critical numeric fields
    df = df.dropna(subset=["Total Revenue", "Total Profit"])

    return df