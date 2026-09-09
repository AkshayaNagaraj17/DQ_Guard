from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd

from app.services.data_quality_service import run_data_quality_checks


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

    # Run data quality checks
    results = run_data_quality_checks(df)

    # Add filename
    results["filename"] = file.filename

    return results