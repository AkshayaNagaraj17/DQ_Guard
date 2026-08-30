import pandas as pd


def find_invalid_dates(
    df: pd.DataFrame,
    column: str = "date_of_birth"
) -> pd.DataFrame:

    converted_dates = pd.to_datetime(
        df[column],
        errors="coerce"
    )

    invalid_mask = (
        df[column].notna()
        & converted_dates.isna()
    )

    return df[invalid_mask]