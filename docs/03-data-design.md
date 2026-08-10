# 03 — DQGuard Data Design

# DQGuard — Data Design Document

## 1. Purpose

This document defines the data structures, source dataset, validation fields, and Snowflake storage design used by DQGuard.

---

## 2. Source Dataset

The initial source dataset will represent customer information.

Example fields:

| Column        | Description                | Required |
| ------------- | -------------------------- | -------- |
| customer_id   | Unique customer identifier | Yes      |
| name          | Customer name              | Yes      |
| email         | Customer email address     | Yes      |
| phone         | Customer phone number      | Yes      |
| date_of_birth | Customer date of birth     | No       |
| city          | Customer city              | No       |
| created_date  | Record creation date       | Yes      |

---

## 3. Sample Data

Example:

| customer_id | name  | email                                     | phone      | date_of_birth | city       |
| ----------- | ----- | ----------------------------------------- | ---------- | ------------- | ---------- |
| 1001        | Arun  | [arun@gmail.com](mailto:arun@gmail.com)   | 9876543210 | 1998-04-12    | Chennai    |
| 1002        | Priya | [priya@gmail.com](mailto:priya@gmail.com) | 9876543211 | 1997-07-20    | Coimbatore |
| 1002        | Priya | [priya@gmail.com](mailto:priya@gmail.com) | 9876543211 | 1997-07-20    | Coimbatore |
| 1003        | Ravi  | NULL                                      | 9876543213 | 1995-10-15    | Madurai    |
| 1004        | Kumar | invalid-email                             | 9876543214 | 1996-02-30    | Chennai    |

The sample dataset will intentionally contain quality issues for testing.

---

## 4. Data Quality Categories

DQGuard will initially identify the following categories:

### Duplicate

A record that matches another record based on configured duplicate rules.

### Missing Value

A required field containing NULL or empty data.

### Invalid Format

A value that does not conform to the expected format.

### Valid

A record that passes all applicable validation rules.

---

## 5. Snowflake Database Structure

The initial Snowflake structure will be:

```text
DATA_QUALITY_DB
│
└── CUSTOMER_DQ
    │
    ├── RAW_CUSTOMER
    ├── CLEAN_CUSTOMER
    ├── DQ_ERRORS
    └── DQ_RESULTS
```

---

## 6. RAW_CUSTOMER

Purpose:

Stores incoming data before quality processing.

Example columns:

| Column        | Data Type |
| ------------- | --------- |
| customer_id   | VARCHAR   |
| name          | VARCHAR   |
| email         | VARCHAR   |
| phone         | VARCHAR   |
| date_of_birth | DATE      |
| city          | VARCHAR   |
| created_date  | DATE      |
| loaded_at     | TIMESTAMP |

---

## 7. CLEAN_CUSTOMER

Purpose:

Stores records that successfully pass the required data-quality rules.

Example columns:

| Column        | Data Type |
| ------------- | --------- |
| customer_id   | VARCHAR   |
| name          | VARCHAR   |
| email         | VARCHAR   |
| phone         | VARCHAR   |
| date_of_birth | DATE      |
| city          | VARCHAR   |
| created_date  | DATE      |
| validated_at  | TIMESTAMP |

---

## 8. DQ_ERRORS

Purpose:

Stores records that fail one or more validation rules.

Example columns:

| Column        | Data Type |
| ------------- | --------- |
| customer_id   | VARCHAR   |
| error_type    | VARCHAR   |
| error_message | VARCHAR   |
| source_record | VARCHAR   |
| detected_at   | TIMESTAMP |

---

## 9. DQ_RESULTS

Purpose:

Stores summary information about each data-quality execution.

Example columns:

| Column            | Description                 |
| ----------------- | --------------------------- |
| execution_id      | Unique execution identifier |
| total_records     | Total input records         |
| valid_records     | Number of valid records     |
| duplicate_records | Number of duplicates        |
| invalid_records   | Number of invalid records   |
| quality_score     | Overall quality percentage  |
| execution_time    | Processing timestamp        |

---

## 10. Data Flow

```text
Source CSV
    ↓
RAW_CUSTOMER
    ↓
Validation
    ↓
 ┌──────────────┬──────────────┐
 │              │              │
 ▼              ▼              ▼
CLEAN       DQ_ERRORS       DQ_RESULTS
CUSTOMER
```

---

## 11. Data Retention

For the portfolio implementation, data will be retained for demonstration and testing purposes.

Future production implementations may introduce formal data-retention policies.

---

## 12. Data Security

The project will use synthetic data.

No confidential or production customer information will be used.

Snowflake credentials will not be stored directly in source code.

Secrets will be managed through environment variables or an appropriate secret-management mechanism.

---

## 13. Future Data Design Enhancements

Potential improvements:

* Historical execution tables.
* Data-quality rule configuration table.
* Data lineage information.
* Source-system metadata.
* Rule-level quality metrics.
* Historical quality trends.

---

## 14. Status

**Status:** Initial design

This document will be updated when the Snowflake schema is finalized.
