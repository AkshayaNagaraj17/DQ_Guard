import re
import pandas as pd


EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def find_invalid_emails(
    df: pd.DataFrame,
    column: str = "email"
) -> pd.DataFrame:

    invalid_mask = (
        df[column].notna()
        & ~df[column].astype(str).str.match(
            EMAIL_PATTERN,
            na=False
        )
    )

    return df[invalid_mask]