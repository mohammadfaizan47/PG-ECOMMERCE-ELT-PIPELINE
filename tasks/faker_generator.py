import logging
import random
from datetime import datetime, timezone
from faker import Faker

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)
logger = logging.getLogger(__name__)

fake = Faker()

def generate_users(num_users: int) -> list[dict]:
    """Generate fake user records."""
    logger.info(f"Generating {num_users} users...")
    users = []
    for _ in range(num_users):
        users.append({
            "name": fake.name(),
            "email": fake.unique.email(),
            "phone": fake.phone_number(),
            "address": fake.address().replace("\n", ", "),
            "created_at": fake.date_time_between(start_date="-2y", end_date="now"),
            "updated_at": datetime.now(timezone.utc),
            "is_deleted": False
        })
    logger.info(f"Generated {len(users)} users successfully")
    return users


def generate_products(num_products: int) -> list[dict]:
    """Generate fake product records."""
    logger.info(f"Generating {num_products} products...")
    categories = ["Electronics", "Clothing", "Books", "Home & Kitchen", "Sports", "Beauty"]
    products = []
    for _ in range(num_products):
        products.append({
            "name": fake.catch_phrase(),
            "category": random.choice(categories),
            "price": round(random.uniform(10.0, 5000.0), 2),
            "description": fake.text(max_nb_chars=200),
            "created_at": fake.date_time_between(start_date="-2y", end_date="now"),
            "updated_at": datetime.now(timezone.utc),
            "is_deleted": False
        })
    logger.info(f"Generated {len(products)} products successfully")
    return products


def generate_orders(num_orders: int, user_ids: list[int]) -> list[dict]:
    """Generate fake order records linked to real user IDs."""
    logger.info(f"Generating {num_orders} orders...")
    statuses = ["pending", "processing", "shipped", "delivered", "cancelled"]
    orders = []
    for _ in range(num_orders):
        orders.append({
            "user_id": random.choice(user_ids),
            "status": random.choice(statuses),
            "total_amount": 0.0,
            "created_at": fake.date_time_between(start_date="-1y", end_date="now"),
            "updated_at": datetime.now(timezone.utc),
            "is_deleted": False
        })
    logger.info(f"Generated {len(orders)} orders successfully")
    return orders


def generate_order_items(num_items: int, order_ids: list[int], product_ids: list[int]) -> list[dict]:
    """Generate fake order item records linked to real order and product IDs."""
    logger.info(f"Generating {num_items} order items...")
    items = []
    for _ in range(num_items):
        quantity = random.randint(1, 5)
        price = round(random.uniform(10.0, 5000.0), 2)
        items.append({
            "order_id": random.choice(order_ids),
            "product_id": random.choice(product_ids),
            "quantity": quantity,
            "price_at_purchase": price,
            "subtotal": round(quantity * price, 2),
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc)
        })
    logger.info(f"Generated {len(items)} order items successfully")
    return items


def generate_inventory(product_ids: list[int]) -> list[dict]:
    """Generate inventory records for each product."""
    logger.info(f"Generating inventory for {len(product_ids)} products...")
    inventory = []
    for product_id in product_ids:
        inventory.append({
            "product_id": product_id,
            "stock_quantity": random.randint(0, 500),
            "last_updated": datetime.now(timezone.utc)
        })
    logger.info(f"Generated {len(inventory)} inventory records successfully")
    return inventory