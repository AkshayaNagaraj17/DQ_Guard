def calculate_quality_score(
    total_records: int,
    duplicate_count: int,
    missing_count: int,
    invalid_email_count: int,
    invalid_date_count: int
) -> float:

    if total_records == 0:
        return 0.0

    # Calculate issue rates
    duplicate_rate = duplicate_count / total_records
    missing_rate = missing_count / total_records
    email_error_rate = invalid_email_count / total_records
    date_error_rate = invalid_date_count / total_records

    # Convert each issue rate into a quality score
    duplicate_score = max(0, 1 - duplicate_rate)
    missing_score = max(0, 1 - missing_rate)
    email_score = max(0, 1 - email_error_rate)
    date_score = max(0, 1 - date_error_rate)

    # Apply weights
    final_score = (
        duplicate_score * 30
        + missing_score * 25
        + email_score * 20
        + date_score * 25
    )

    return round(final_score, 2)