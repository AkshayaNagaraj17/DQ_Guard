from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd

from app.validators.duplicate_validator import find_duplicate_records

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are currently supported."
        )

    df = pd.read_csv(file.file)

    duplicates = find_duplicate_records(
        df,
        "customer_id"
    )

    return {
        "filename": file.filename,
        "total_records": len(df),
        "total_duplicates": len(duplicates),
        "duplicate_records": duplicates.to_dict(orient="records")
    }