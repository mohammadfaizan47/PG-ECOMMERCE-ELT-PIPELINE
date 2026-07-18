import logging
import yaml
import boto3
import json
import psycopg2
from tasks.faker_generator import (
    generate_users,
    generate_products,
    generate_orders,
    generate_order_items,
    generate_inventory
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)
logger = logging.getLogger(__name__)


def load_config(env: str = "dev") -> dict:
    with open(f"config/{env}.yaml", "r") as f:
        return yaml.safe_load(f)


def get_db_credentials() -> dict:
    secret_name = "ecommerce-pipeline/rds-credentials"
    client = boto3.client("secretsmanager", region_name="ap-south-1")
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])


def get_db_connection(credentials: dict):
    return psycopg2.connect(
        host=credentials["host"],
        port=credentials["port"],
        database=credentials["dbname"],
        user=credentials["username"],
        password=credentials["password"]
    )


def insert_users(cur, users: list[dict]) -> list[int]:
    user_ids = []
    for user in users:
        cur.execute("""
            INSERT INTO users (name, email, phone, address, created_at, updated_at, is_deleted)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING user_id
        """, (
            user["name"], user["email"], user["phone"],
            user["address"], user["created_at"],
            user["updated_at"], user["is_deleted"]
        ))
        user_ids.append(cur.fetchone()[0])
    logger.info(f"Inserted {len(user_ids)} users into database")
    return user_ids


def insert_products(cur, products: list[dict]) -> list[int]:
    product_ids = []
    for product in products:
        cur.execute("""
            INSERT INTO products (name, category, price, description, created_at, updated_at, is_deleted)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING product_id
        """, (
            product["name"], product["category"], product["price"],
            product["description"], product["created_at"],
            product["updated_at"], product["is_deleted"]
        ))
        product_ids.append(cur.fetchone()[0])
    logger.info(f"Inserted {len(product_ids)} products into database")
    return product_ids


def insert_orders(cur, orders: list[dict]) -> list[int]:
    order_ids = []
    for order in orders:
        cur.execute("""
            INSERT INTO orders (user_id, status, total_amount, created_at, updated_at, is_deleted)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING order_id
        """, (
            order["user_id"], order["status"], order["total_amount"],
            order["created_at"], order["updated_at"], order["is_deleted"]
        ))
        order_ids.append(cur.fetchone()[0])
    logger.info(f"Inserted {len(order_ids)} orders into database")
    return order_ids


def insert_order_items(cur, items: list[dict]) -> None:
    for item in items:
        cur.execute("""
            INSERT INTO order_items (order_id, product_id, quantity, price_at_purchase, subtotal, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            item["order_id"], item["product_id"], item["quantity"],
            item["price_at_purchase"], item["subtotal"],
            item["created_at"], item["updated_at"]
        ))
    logger.info(f"Inserted {len(items)} order items into database")


def insert_inventory(cur, inventory: list[dict]) -> None:
    for item in inventory:
        cur.execute("""
            INSERT INTO inventory (product_id, stock_quantity, last_updated)
            VALUES (%s, %s, %s)
        """, (
            item["product_id"], item["stock_quantity"], item["last_updated"]
        ))
    logger.info(f"Inserted {len(inventory)} inventory records into database")


def run():
    """Main function to generate and insert all fake data."""
    logger.info("Starting Faker data generation pipeline...")

    config = load_config("dev")
    gen_config = yaml.safe_load(open("config/gen.yaml"))["generation"]

    logger.info("Fetching database credentials from Secrets Manager...")
    credentials = get_db_credentials()
    conn = get_db_connection(credentials)
    cur = conn.cursor()

    try:
        users = generate_users(gen_config["num_users"])
        user_ids = insert_users(cur, users)

        products = generate_products(gen_config["num_products"])
        product_ids = insert_products(cur, products)

        orders = generate_orders(gen_config["num_orders"], user_ids)
        order_ids = insert_orders(cur, orders)

        items = generate_order_items(
            gen_config["num_order_items"], order_ids, product_ids
        )
        insert_order_items(cur, items)

        inventory = generate_inventory(product_ids)
        insert_inventory(cur, inventory)

        conn.commit()
        logger.info("All data committed to database successfully")

    except Exception as e:
        conn.rollback()
        logger.error(f"Error during data generation: {e}")
        raise

    finally:
        cur.close()
        conn.close()
        logger.info("Database connection closed")


if __name__ == "__main__":
    run()