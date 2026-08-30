from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd

from app.validators.duplicate_validator import find_duplicate_records
from app.validators.null_validator import find_missing_values
from app.validators.email_validator import find_invalid_emails
from app.validators.date_validator import find_invalid_dates


router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    # Check file type
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are currently supported."
        )

    # Read CSV file
    df = pd.read_csv(file.file)

    # Duplicate check
    duplicates = find_duplicate_records(
        df,
        "customer_id"
    )

    # Missing-value check
    missing_values = find_missing_values(df)

    # Email validation
    invalid_emails = find_invalid_emails(
        df,
        "email"
    )

    # Date validation
    invalid_dates = find_invalid_dates(
        df,
        "date_of_birth"
    )

    # Return quality results
    return {
        "filename": file.filename,
        "total_records": len(df),

        "total_duplicates": len(duplicates),

        "missing_values": missing_values,

        "invalid_emails": len(invalid_emails),

        "invalid_dates": len(invalid_dates),

        "duplicate_records": duplicates.to_dict(
            orient="records"
        )
    }