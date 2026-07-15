# Order Items Table

## Description
Stores individual line items within each order — one row per product per order.

## Schema
| Column | Type | Nullable | Description |
|--------|------|----------|-------------|
| order_item_id | SERIAL | NO | Primary key, unique order item identifier |
| order_id | INTEGER | NO | Foreign key → orders.order_id |
| product_id | INTEGER | NO | Foreign key → products.product_id |
| quantity | INTEGER | NO | Number of units ordered |
| price_at_purchase | NUMERIC | NO | Product price at time of purchase (snapshot) |
| subtotal | NUMERIC | NO | quantity × price_at_purchase |
| created_at | TIMESTAMP | NO | Record creation timestamp |
| updated_at | TIMESTAMP | NO | Last modification timestamp (cursor column) |

## Notes
- `price_at_purchase` captures price at order time — not affected by future price changes
- `subtotal` = quantity × price_at_purchase (pre-calculated for query performance)
- No soft delete — order items are never deleted independently of their parent order