# Inventory Table

## Description
Tracks current stock levels for each product.

## Schema
| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| inventory_id | SERIAL | NO | Primary key, unique inventory record identifier |
| product_id | INTEGER | NO | Foreign key → products.product_id (unique) |
| stock_quantity | INTEGER | NO | Current available stock units |
| last_updated | TIMESTAMP | NO | Last stock update timestamp (cursor column) |

## Notes
- One row per product — product_id is unique in this table
- `last_updated` used by Fivetran as cursor column for incremental sync
- `stock_quantity` decrements as orders are placed (simulated by Faker script)
- No soft delete or updated_at — inventory records are updated in place