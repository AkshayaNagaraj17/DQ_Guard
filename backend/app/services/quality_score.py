def calculate_quality_score(
    total_records: int,
    duplicate_count: int,
    missing_count: int,
    invalid_email_count: int,
    invalid_date_count: int
) -> float:

    if total_records == 0:
        return 0.0

    total_issues = (
        duplicate_count
        + missing_count
        + invalid_email_count
        + invalid_date_count
    )

    issue_rate = total_issues / total_records

    score = (1 - issue_rate) * 100

    return round(max(score, 0), 2)