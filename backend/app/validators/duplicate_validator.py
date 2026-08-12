import pandas as pd


def find_duplicate_records(
    df: pd.DataFrame,
    column: str
) -> pd.DataFrame:

    duplicates = df[df.duplicated(
        subset=[column],
        keep=False
    )]

    return duplicates