# 02 — DQGuard System Architecture

# DQGuard — System Architecture Document

## 1. Purpose

This document describes the technical architecture of the DQGuard Data Quality & Duplicate Detection Platform.

The architecture is designed to be simple enough for the initial MVP while allowing future integration with Airflow, AWS, APIs, and additional services.

---

## 2. Initial Architecture

```text
                         USER
                           │
                           ▼
                ┌────────────────────┐
                │ React + Tailwind   │
                │    Dashboard       │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Python Validation  │
                │      Engine        │
                │                    │
                │     Pandas         │
                └─────────┬──────────┘
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
      VALID RECORDS              INVALID RECORDS
             │                         │
             └────────────┬────────────┘
                          ▼
                ┌────────────────────┐
                │     Snowflake      │
                │                    │
                │ RAW                │
                │ CLEAN              │
                │ ERROR              │
                │ QUALITY RESULTS    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Quality Metrics    │
                │ & Reporting        │
                └─────────┬──────────┘
                          │
                          ▼
                React Dashboard
```

---

## 3. Architecture Components

### 3.1 React

React will provide the user interface.

Responsibilities:

* Dataset upload interface.
* Dashboard.
* Data-quality summary.
* Duplicate records page.
* Invalid records page.
* Search and filtering.
* Charts and visualizations.

---

### 3.2 Tailwind CSS

Tailwind CSS will be used to create the dashboard interface.

Responsibilities:

* Layout.
* Cards.
* Tables.
* Forms.
* Navigation.
* Responsive design.

---

### 3.3 Python

Python will be used as the primary data-processing language.

Responsibilities:

* Reading CSV files.
* Data validation.
* Duplicate detection.
* Missing-value detection.
* Data transformation.
* Quality-score calculation.

---

### 3.4 Pandas

Pandas will be used for structured data processing.

Responsibilities:

* Reading CSV files.
* DataFrame operations.
* Duplicate identification.
* Missing-value analysis.
* Data transformation.

---

### 3.5 Snowflake

Snowflake will act as the cloud data warehouse.

Responsibilities:

* Store raw data.
* Store validated data.
* Store error records.
* Store data-quality results.
* Perform SQL-based analysis.

---

## 4. Data Flow

The initial data flow is:

```text
CSV
 ↓
Python
 ↓
Pandas
 ↓
Validation Rules
 ↓
Classification
 ↓
Snowflake
 ↓
Quality Metrics
 ↓
React Dashboard
```

---

## 5. Data Classification Flow

Each record will pass through the validation engine.

```text
                 RECORD
                    │
                    ▼
             Required Fields?
               /           \
             NO             YES
             │               │
          INVALID            ▼
                       Duplicate?
                       /        \
                     YES         NO
                     │            │
                  DUPLICATE       ▼
                            Other Rules
                            /        \
                          FAIL       PASS
                           │           │
                        INVALID       VALID
```

---

## 6. Future Architecture — Airflow

After the MVP is completed, Apache Airflow will be introduced.

```text
CSV / S3
   ↓
Airflow DAG
   ↓
Python Validation
   ↓
Data Quality Checks
   ↓
Snowflake
   ↓
React Dashboard
```

Airflow will be responsible for scheduling and orchestrating the workflow.

---

## 7. Future Architecture — Cloud/API Version

The final optional architecture may include:

```text
                    AWS S3
                      │
                      ▼
                   Airflow
                      │
                      ▼
              Python/Pandas
                      │
                      ▼
                 Snowflake
                      │
                      ▼
                  FastAPI
                      │
                      ▼
               React Dashboard
                      │
                      ▼
                     User
```

This version is optional and will only be implemented after the MVP is stable.

---

## 8. Architecture Principles

The following principles will be followed:

1. Keep the MVP simple.
2. Separate data processing from presentation.
3. Keep business rules configurable where practical.
4. Avoid unnecessary technologies.
5. Protect credentials and secrets.
6. Design for future scalability.
7. Keep documentation updated.
8. Use version control for all source code and documentation.

---

## 9. Technology Stack

| Layer                   | Technology     |
| ----------------------- | -------------- |
| Frontend                | React          |
| Styling                 | Tailwind CSS   |
| Data Processing         | Python         |
| Data Processing Library | Pandas         |
| Data Warehouse          | Snowflake      |
| Query Language          | SQL            |
| Version Control         | Git            |
| Repository              | GitHub         |
| Future Orchestration    | Apache Airflow |
| Future API              | FastAPI        |
| Future Cloud Storage    | AWS S3         |

---

## 10. Architecture Status

**Current:** MVP architecture

**Future:** Airflow/API/Cloud architecture

This document will be updated when new components are introduced.
