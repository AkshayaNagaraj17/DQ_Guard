from app.validators.duplicate_validator import find_duplicate_records
from app.validators.null_validator import find_missing_values
from app.validators.email_validator import find_invalid_emails
from app.validators.date_validator import find_invalid_dates
from app.services.quality_score import calculate_quality_score


def run_data_quality_checks(df):

    total_records = len(df)

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

    # Counts
    duplicate_count = len(duplicates)
    missing_count = sum(missing_values.values())
    invalid_email_count = len(invalid_emails)
    invalid_date_count = len(invalid_dates)

    # Quality score
    quality_score = calculate_quality_score(
        total_records=total_records,
        duplicate_count=duplicate_count,
        missing_count=missing_count,
        invalid_email_count=invalid_email_count,
        invalid_date_count=invalid_date_count
    )

    # Calculate percentages
    def percentage(count):
        if total_records == 0:
            return 0.0

        return round(
            (count / total_records) * 100,
            2
        )

    return {
        "summary": {
            "total_records": total_records,
            "quality_score": quality_score
        },

        "quality_checks": {
            "duplicates": {
                "count": duplicate_count,
                "percentage": percentage(duplicate_count)
            },

            "missing_values": {
                "count": missing_count,
                "percentage": percentage(missing_count),
                "columns": missing_values
            },

            "invalid_emails": {
                "count": invalid_email_count,
                "percentage": percentage(invalid_email_count)
            },

            "invalid_dates": {
                "count": invalid_date_count,
                "percentage": percentage(invalid_date_count)
            }
        },

        "duplicate_records": duplicates.to_dict(
            orient="records"
        )
    }