# Orders Table

## Description
Stores all customer orders placed on the e-commerce platform.

## Schema
| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| order_id | SERIAL | NO | Primary key, unique order identifier |
| user_id | INTEGER | NO | Foreign key → users.user_id |
| status | VARCHAR | NO | Order status (pending/processing/shipped/delivered/cancelled) |
| total_amount | NUMERIC | NO | Total order value (sum of order_items subtotals) |
| created_at | TIMESTAMP | NO | Record creation timestamp |
| updated_at | TIMESTAMP | NO | Last modification timestamp (cursor column) |
| is_deleted | BOOLEAN | NO | Soft delete flag (true = deleted) |

## Notes
- `updated_at` used by Fivetran as cursor column for incremental sync
- `total_amount` is updated after order_items are inserted
- `status` flow: pending → processing → shipped → delivered (or cancelled)