# Products Table

## Description
Stores all product listings available on the e-commerce platform.

## Schema
| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| product_id | SERIAL | NO | Primary key, unique product identifier |
| name | VARCHAR | NO | Product name/title |
| category | VARCHAR | NO | Product category (Electronics, Clothing, etc.) |
| price | NUMERIC | NO | Current listed price |
| description | TEXT | YES | Product description |
| created_at | TIMESTAMP | NO | Record creation timestamp |
| updated_at | TIMESTAMP | NO | Last modification timestamp (cursor column) |
| is_deleted | BOOLEAN | NO | Soft delete flag (true = deleted) |

## Notes
- `updated_at` used by Fivetran as cursor column for incremental sync
- `is_deleted` handles soft deletes — records never hard deleted
- `category` values: Electronics, Clothing, Books, Home & Kitchen, Sports, Beauty