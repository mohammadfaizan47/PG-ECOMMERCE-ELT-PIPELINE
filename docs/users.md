# Users Table

## Description
Stores customer information for the e-commerce platform.

## Schema
| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| user_id | INTEGER | NO | Primary key, unique user identifier |
| name | VARCHAR | NO | Full name of the customer |
| email | VARCHAR | NO | Unique email address |
| phone | VARCHAR | YES | Contact phone number |
| address | VARCHAR | YES | Delivery address |
| created_at | TIMESTAMP | NO | Record creation timestamp |
| updated_at | TIMESTAMP | NO | Last modification timestamp (cursor column) |
| is_deleted | BOOLEAN | NO | Soft delete flag (true = deleted) |

## Notes
- `updated_at` is used by Fivetran as the cursor column for incremental sync
- `is_deleted` handles soft deletes — records are never hard deleted