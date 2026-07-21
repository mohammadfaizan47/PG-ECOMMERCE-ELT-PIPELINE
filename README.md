# PG-ECOMMERCE-ELT-PIPELINE
Production-Grade E-Commerce ELT Pipeline - "Batch ELT with Managed SaaS Stack" \
\
A production-grade ELT (Extract, Load, Transform) data pipeline simulating a real-world 
e-commerce platform's backend data infrastructure. Built to demonstrate practical data 
engineering skills — from data generation and ingestion to transformation, orchestration, 
and quality monitoring — using a mix of managed SaaS tools and open-source frameworks.

## Project Goal 
Simulate an e-commerce company's data platform where transactional data (users, products, 
orders, order items, inventory) is generated, stored in a relational database, replicated 
into a cloud data lake, transformed through a medallion architecture (Bronze → Silver → Gold), 
validated for quality, and orchestrated end-to-end — mirroring how real companies build 
scalable, production-grade data infrastructure.

## Tech Stack:
```text
Data Generation     : Python, Faker
Source Database     : AWS RDS (PostgreSQL 18)
Ingestion / EL      : Fivetran (CDC via updated_at cursor)
Storage (Bronze)    : AWS S3
```
