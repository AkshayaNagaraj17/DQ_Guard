# 06 — DQGuard Testing Strategy

# DQGuard — Testing Strategy

## 1. Purpose

This document defines the testing approach for validating the functionality, reliability, and data-quality rules of DQGuard.

---

## 2. Testing Levels

The project will use:

1. Unit Testing
2. Data Validation Testing
3. Integration Testing
4. UI Testing
5. End-to-End Testing
6. Negative Testing

---

## 3. Unit Testing

Individual functions will be tested independently.

Examples:

* Duplicate detection function.
* Email validation function.
* Phone validation function.
* Date validation function.
* Quality-score calculation.

---

## 4. Data Validation Test Cases

| Test ID | Scenario               | Expected Result    |
| ------- | ---------------------- | ------------------ |
| TC001   | Valid record           | VALID              |
| TC002   | Duplicate row          | DUPLICATE          |
| TC003   | Duplicate customer ID  | Duplicate detected |
| TC004   | Duplicate email        | Duplicate detected |
| TC005   | Missing email          | INVALID            |
| TC006   | Missing customer ID    | INVALID            |
| TC007   | Invalid email          | INVALID            |
| TC008   | Invalid phone          | INVALID            |
| TC009   | Invalid date           | INVALID            |
| TC010   | Valid complete dataset | 100% quality       |

---

## 5. File Validation Tests

| Test ID | Scenario                | Expected Result        |
| ------- | ----------------------- | ---------------------- |
| TC011   | Empty CSV               | Validation error       |
| TC012   | Missing required column | Validation error       |
| TC013   | Unsupported file type   | File rejected          |
| TC014   | Valid CSV               | Processing starts      |
| TC015   | Large sample CSV        | Successfully processed |

---

## 6. Snowflake Integration Tests

Verify:

* Database exists.
* Schema exists.
* Tables exist.
* Records are loaded correctly.
* Invalid records reach the error table.
* Valid records reach the clean table.
* Quality results are stored correctly.

---

## 7. Dashboard Tests

Verify:

* Dashboard loads.
* Metrics display correctly.
* Record counts match Snowflake.
* Duplicate records are displayed.
* Invalid records are displayed.
* Search works.
* Filtering works.
* Sorting works.
* Charts display correct values.

---

## 8. End-to-End Test

Complete workflow:

```text
Upload CSV
   ↓
Validation
   ↓
Duplicate Detection
   ↓
Error Detection
   ↓
Snowflake
   ↓
Dashboard
```

Expected result:

The dashboard should display the same validation results produced by the processing engine.

---

## 9. Negative Testing

The following invalid scenarios should be tested:

* Empty file.
* Corrupted CSV.
* Missing columns.
* NULL customer ID.
* Invalid email.
* Invalid phone.
* Invalid date.
* Duplicate records.
* Unsupported data format.

The application should handle these cases gracefully without crashing.

---

## 10. Data Reconciliation

The following counts should be reconciled:

```text
Total Input Records
=
Valid Records
+
Invalid Records
+
Duplicate Records
```

The exact reconciliation logic may be adjusted depending on how overlapping errors are classified.

---

## 11. Regression Testing

Whenever a new feature is introduced, existing functionality should be tested again.

Example:

After adding Airflow, verify that the original Python validation results remain correct.

---

## 12. Defect Tracking

Issues will be tracked using GitHub Issues.

Example:

```text
BUG-001
Invalid email validation returns valid

BUG-002
Duplicate count incorrect

BUG-003
Dashboard quality score does not match Snowflake
```

---

## 13. Definition of Test Completion

Testing for a feature is complete when:

* Expected test cases pass.
* Negative scenarios are handled.
* No critical defects remain.
* Data counts reconcile.
* Documentation is updated.

---

## 14. Status

**Status:** Initial testing strategy
