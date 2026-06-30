# Retail Sales Data Engineering Pipeline
[View project documentation site](https://shambhavishanbhag1910.github.io/retail-sales-data-engineering-pipeline/)
## Project Overview

This project is an end-to-end **Retail Sales Data Engineering Pipeline** built using Python, PostgreSQL, Docker, dbt, Apache Airflow, and GitHub Actions.

The project simulates a real-world retail business where customer, product, order, order item, and inventory data are generated as CSV files, ingested into PostgreSQL, validated, transformed into analytics-ready tables, orchestrated using Airflow, and validated through CI/CD using GitHub Actions.

This project demonstrates practical Data Engineering skills including:

- ETL pipeline development
- ELT transformation using dbt
- Data quality validation
- Dimensional data modeling
- Airflow orchestration
- Docker-based local setup
- GitHub Actions CI/CD
- PostgreSQL database management

---

## Business Problem

A retail company receives daily sales and inventory data from multiple source systems. The business wants clean, reliable, and analytics-ready data to answer questions such as:

- What is the daily sales revenue?
- Which products are selling the most?
- Which customers generate the highest revenue?
- Which products are below reorder level?
- What is the monthly revenue trend?

This project builds a data pipeline that converts raw source data into business-ready analytics tables.

---

## High-Level Architecture

```text
Synthetic Retail Source Data
        ↓
CSV Files
        ↓
Python Ingestion Pipeline
        ↓
PostgreSQL Raw Tables
        ↓
Python Data Quality Checks
        ↓
dbt Staging Models
        ↓
dbt Marts Layer
        ↓
dbt Analytics Layer
        ↓
Airflow Orchestration
        ↓
GitHub Actions CI/CD
```
