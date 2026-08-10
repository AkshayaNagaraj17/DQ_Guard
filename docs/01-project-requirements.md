# 01 — DQGuard Project Requirements Document

# DQGuard — Data Quality & Duplicate Detection Platform

## 1. Document Information

| Item          | Details                                     |
| ------------- | ------------------------------------------- |
| Project Name  | DQGuard                                     |
| Project Type  | Data Quality & Duplicate Detection Platform |
| Version       | 1.0                                         |
| Status        | Draft                                       |
| Author        | Akshaya                                     |


---

## 2. Project Overview

DQGuard is an end-to-end data quality platform designed to identify duplicate, missing, and invalid records in incoming datasets.

The platform will process customer data, apply configurable data-quality rules, identify problematic records, store validated and error data in Snowflake, and provide a web-based dashboard for monitoring data quality.

The initial implementation will focus on CSV-based customer datasets.

---

## 3. Business Problem

Organizations receive data from multiple sources such as applications, files, APIs, and operational systems.

Incoming data may contain:

* Duplicate records
* Duplicate business identifiers
* Missing mandatory fields
* Invalid email addresses
* Invalid phone numbers
* Invalid dates
* Incorrect data formats

Poor-quality data can affect reporting, analytics, customer records, and downstream data pipelines.

Manual data-quality validation is time-consuming and difficult to scale.

DQGuard aims to automate these validation activities and provide users with a centralized view of data-quality issues.

---

## 4. Project Objective

The primary objective of DQGuard is to build an automated data-quality platform that:

1. Accepts customer data as CSV input.
2. Validates incoming records.
3. Detects duplicate records.
4. Detects missing and invalid values.
5. Classifies records as valid or invalid.
6. Calculates an overall data-quality score.
7. Stores processed data and quality results in Snowflake.
8. Provides a web dashboard for monitoring results.

---

## 5. Proposed Solution

The proposed solution consists of the following major components:

```text
CSV Dataset
     ↓
Data Validation Engine
     ↓
Data Quality Rules
     ↓
Valid / Invalid / Duplicate Classification
     ↓
Snowflake
     ↓
React Dashboard
```

The initial implementation will use Python and Pandas for data processing and Snowflake for data storage and analysis.

Apache Airflow will be introduced in a later phase to automate the data pipeline.

---

## 6. Target Users

### 6.1 Data Engineer

The Data Engineer can:

* Process incoming datasets.
* Monitor validation results.
* Investigate duplicate records.
* Review data-quality failures.
* Monitor pipeline execution after Airflow integration.

### 6.2 Data/Business User

The business user can:

* View overall data quality.
* Review invalid records.
* Review duplicate records.
* View quality metrics.
* Filter and search problematic records.

---

## 7. Project Scope

### 7.1 In Scope

The initial release will include:

* CSV file processing.
* Customer dataset validation.
* Duplicate detection.
* Duplicate ID detection.
* NULL/missing-value detection.
* Email validation.
* Phone validation.
* Date validation.
* Data-quality score.
* Valid record identification.
* Invalid record identification.
* Snowflake data storage.
* React-based dashboard.
* Search and filtering.
* Basic reporting.

### 7.2 Out of Scope

The initial release will not include:

* Real-time streaming.
* Machine learning-based anomaly detection.
* Mobile application.
* Advanced enterprise authentication.
* Production-scale distributed processing.
* Automated production deployment.
* Real customer/company data.

These may be considered as future enhancements.

---

## 8. Functional Requirements

### FR-001 — Dataset Upload

The system shall allow a user to provide a CSV customer dataset for processing.

### FR-002 — Data Validation

The system shall validate records against predefined data-quality rules.

### FR-003 — Duplicate Detection

The system shall identify duplicate records based on configured business keys.

### FR-004 — Missing Value Detection

The system shall identify missing values in mandatory fields.

### FR-005 — Email Validation

The system shall identify records containing invalid email formats.

### FR-006 — Phone Validation

The system shall identify records containing invalid phone formats.

### FR-007 — Date Validation

The system shall identify records containing invalid date values or formats.

### FR-008 — Record Classification

The system shall classify records into appropriate categories such as:

* VALID
* DUPLICATE
* INVALID

### FR-009 — Data Quality Score

The system shall calculate an overall data-quality score based on validation results.

### FR-010 — Snowflake Storage

The system shall store raw, validated, and error information in Snowflake.

### FR-011 — Dashboard

The system shall provide a dashboard containing data-quality metrics and problematic records.

### FR-012 — Filtering

The dashboard shall allow users to search and filter validation results.

---

## 9. Non-Functional Requirements

### Performance

The application should process normal-sized sample datasets within a reasonable time.

### Reliability

Validation failures should not cause the entire application to crash.

### Maintainability

The application should use modular code and documented business rules.

### Security

Credentials and secrets shall not be hardcoded in source code.

### Usability

The dashboard should be simple and understandable for technical and business users.

### Scalability

The design should allow future integration with larger datasets and automated pipelines.

---

## 10. Assumptions

* The initial input will be CSV data.
* The dataset will contain customer-related information.
* Data-quality rules will initially be predefined.
* Snowflake will be used as the analytical data store.
* Synthetic/sample data will be used for development.
* The initial project is intended for portfolio and learning purposes.

---

## 11. Constraints

* The project should use free or low-cost development tools.
* No company or confidential data will be used.
* The initial implementation should remain beginner-friendly.
* Cloud services should not be required for the initial MVP.
* Advanced technologies will be introduced incrementally.

---

## 12. Success Criteria

The MVP will be considered successful when:

1. A CSV dataset can be processed successfully.
2. Duplicate records are correctly identified.
3. Missing and invalid values are detected.
4. Records are correctly classified.
5. Data-quality metrics are calculated.
6. Results are stored in Snowflake.
7. The React dashboard displays the results.
8. The complete process can be demonstrated end-to-end.
9. The project can be documented and maintained through GitHub.

---

## 13. Future Enhancements

Potential future enhancements include:

* Apache Airflow pipeline orchestration.
* AWS S3 integration.
* FastAPI backend.
* PostgreSQL metadata storage.
* Role-based authentication.
* Email/Teams notifications.
* Advanced data-quality rules.
* Historical quality tracking.
* Automated data-quality reports.
* Data-quality trend analysis.
* Machine-learning-based anomaly detection.

---

## 14. Document Status

**Current Status:** Draft

This document will be updated when project requirements or scope changes.
