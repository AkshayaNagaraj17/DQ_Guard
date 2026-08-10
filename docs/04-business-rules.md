# 04 — DQGuard Business Rules

# DQGuard — Data Quality Business Rules

## 1. Purpose

This document defines the business rules used by DQGuard to determine whether customer records are valid, invalid, or duplicates.

---

## 2. Record Classification

Each incoming record will be classified into one of the following categories:

```text
VALID
DUPLICATE
INVALID
```

A record that violates one or more validation rules will be classified as INVALID unless it is identified specifically as a duplicate according to the duplicate-handling logic.

---

## 3. Mandatory Field Rules

The following fields are mandatory:

* customer_id
* name
* email
* phone
* created_date

### Rule

A record fails validation if any mandatory field is NULL or empty.

Example:

```text
customer_id = 1001
name = Arun
email = NULL
```

Result:

```text
INVALID
Reason: Missing mandatory email
```

---

## 4. Duplicate Record Rule

A record is considered a potential duplicate when another record contains the same configured business identifier.

Initial duplicate keys:

1. customer_id
2. email
3. phone

The implementation will distinguish between exact duplicate rows and duplicate business identifiers.

---

## 5. Exact Duplicate Rule

Two records are exact duplicates when all relevant business fields contain the same values.

Example:

```text
1001 | Arun | arun@gmail.com | 9876543210
1001 | Arun | arun@gmail.com | 9876543210
```

Result:

```text
DUPLICATE
```

---

## 6. Duplicate Customer ID Rule

If the same customer ID appears more than once, the records will be flagged for duplicate investigation.

Example:

```text
1001 | Arun
1001 | Arun
```

Result:

```text
DUPLICATE_ID
```

---

## 7. Duplicate Email Rule

If the same email address appears against multiple customer records, the records will be flagged.

Example:

```text
1001 | arun@gmail.com
1002 | arun@gmail.com
```

Result:

```text
DUPLICATE_EMAIL
```

---

## 8. Missing Value Rule

Required fields must not contain:

* NULL
* Empty string
* Whitespace-only value

Example:

```text
email = NULL
```

Result:

```text
MISSING_VALUE
```

---

## 9. Email Validation Rule

Email addresses must follow a basic valid email structure.

Example valid values:

```text
arun@gmail.com
priya.smith@company.com
```

Example invalid values:

```text
arun
arun@
@company.com
invalid-email
```

---

## 10. Phone Validation Rule

The initial implementation will expect a valid phone number format according to the defined sample-data standard.

For the initial Indian sample dataset, the basic rule will validate a 10-digit numeric phone number.

Example:

```text
9876543210
```

Valid.

Example:

```text
98765
```

Invalid.

---

## 11. Date Validation Rule

Date fields must contain valid calendar dates.

Example:

```text
1998-04-12
```

Valid.

Example:

```text
1996-02-30
```

Invalid.

---

## 12. Data Type Rule

Each field must contain values compatible with its expected data type.

Example:

```text
customer_id → string/integer identifier
name → string
email → string
phone → string
date_of_birth → date
created_date → date
```

---

## 13. Data Quality Score

The initial quality score will be calculated using the proportion of valid records.

Formula:

```text
Quality Score =
Valid Records / Total Records × 100
```

Example:

```text
Total Records = 1000
Valid Records = 950

Quality Score =
950 / 1000 × 100

= 95%
```

The calculation may be refined later to include rule-level severity.

---

## 14. Error Classification

Initial error categories:

| Error Code | Description             |
| ---------- | ----------------------- |
| DQ001      | Missing mandatory field |
| DQ002      | Duplicate record        |
| DQ003      | Duplicate customer ID   |
| DQ004      | Duplicate email         |
| DQ005      | Invalid email           |
| DQ006      | Invalid phone           |
| DQ007      | Invalid date            |
| DQ008      | Invalid data type       |

---

## 15. Rule Configuration

The first version will use rules defined in code.

Future versions may move these rules into a configuration table so that new validation rules can be added without modifying application code.

---

## 16. Rule Priority

Initial processing priority:

```text
1. Mandatory field validation
2. Data type validation
3. Duplicate detection
4. Format validation
5. Record classification
6. Quality score calculation
```

---

## 17. Status

**Status:** Initial business rules

Rules may be modified as implementation and testing progress.
