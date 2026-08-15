import pandas as pd


def find_missing_values(df: pd.DataFrame) -> dict:
    missing_counts = df.isnull().sum()

    return {
        column: int(count)
        for column, count in missing_counts.items()
        if count > 0
    }