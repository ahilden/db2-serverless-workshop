"""
queries.py — SQL query functions for the Db2 Inventory application

Contains functions for all database operations:
  - Schema setup (CREATE TABLE)
  - Product management (insert, update, select)
  - Inventory logging
  - Search

NOTE: This file contains a deliberate security flaw in search_inventory().
      See Lab 1 Exercise 4.
"""

import ibm_db


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

DDL_INVENTORY = """
CREATE TABLE INVENTORY (
    product_id   INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY,
    name         VARCHAR(100) NOT NULL,
    category     VARCHAR(50)  NOT NULL,
    description  VARCHAR(500),
    unit_price   DECIMAL(10, 2) NOT NULL,
    stock_qty    INTEGER NOT NULL DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT TIMESTAMP,
    PRIMARY KEY (product_id)
)
"""

DDL_INVENTORY_LOG = """
CREATE TABLE INVENTORY_LOG (
    log_id      INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY,
    product_id  INTEGER NOT NULL,
    change_type VARCHAR(10) NOT NULL,
    quantity    INTEGER NOT NULL,
    changed_at  TIMESTAMP DEFAULT CURRENT TIMESTAMP,
    PRIMARY KEY (log_id),
    FOREIGN KEY (product_id) REFERENCES INVENTORY (product_id)
)
"""


def create_schema(conn):
    """
    Create the INVENTORY and INVENTORY_LOG tables.
    Skips creation if the tables already exist.

    Args:
        conn: ibm_db connection object
    """
    for ddl in [DDL_INVENTORY, DDL_INVENTORY_LOG]:
        try:
            ibm_db.exec_immediate(conn, ddl)
            print("Table created successfully.")
        except Exception as e:
            if "-601" in str(e):  # SQL0601N — object already exists
                print("Table already exists, skipping.")
            else:
                raise


# ---------------------------------------------------------------------------
# Product operations
# ---------------------------------------------------------------------------

def add_product(conn, name, category, description, unit_price, stock_qty=0):
    """
    Insert a new product into the INVENTORY table.

    Args:
        conn:        ibm_db connection object
        name:        Product name (VARCHAR 100)
        category:    Product category (VARCHAR 50)
        description: Optional product description
        unit_price:  Unit price (DECIMAL 10,2)
        stock_qty:   Initial stock quantity (default 0)

    Returns:
        None
    """
    sql = """
        INSERT INTO INVENTORY (name, category, description, unit_price, stock_qty)
        VALUES (?, ?, ?, ?, ?)
    """
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, name)
    ibm_db.bind_param(stmt, 2, category)
    ibm_db.bind_param(stmt, 3, description)
    ibm_db.bind_param(stmt, 4, unit_price)
    ibm_db.bind_param(stmt, 5, stock_qty)
    ibm_db.execute(stmt)
    print(f"Product '{name}' added.")


def update_stock(conn, product_id, change_type, quantity):
    """
    Update the stock level for a product and write a log entry.

    Args:
        conn:        ibm_db connection object
        product_id:  ID of the product to update
        change_type: 'IN' for stock received, 'OUT' for stock dispatched
        quantity:    Number of units to add or remove

    Returns:
        None
    """
    if change_type == "IN":
        delta = quantity
    elif change_type == "OUT":
        delta = -quantity
    else:
        raise ValueError("change_type must be 'IN' or 'OUT'")

    # Update stock
    sql_update = """
        UPDATE INVENTORY
        SET stock_qty = stock_qty + ?,
            last_updated = CURRENT TIMESTAMP
        WHERE product_id = ?
    """
    stmt = ibm_db.prepare(conn, sql_update)
    ibm_db.bind_param(stmt, 1, delta)
    ibm_db.bind_param(stmt, 2, product_id)
    ibm_db.execute(stmt)

    # Log the change
    sql_log = """
        INSERT INTO INVENTORY_LOG (product_id, change_type, quantity)
        VALUES (?, ?, ?)
    """
    stmt = ibm_db.prepare(conn, sql_log)
    ibm_db.bind_param(stmt, 1, product_id)
    ibm_db.bind_param(stmt, 2, change_type)
    ibm_db.bind_param(stmt, 3, quantity)
    ibm_db.execute(stmt)

    print(f"Stock updated for product {product_id}: {change_type} {quantity} units.")


def get_low_stock(conn, threshold=10):
    """
    Return all products with stock quantity below the given threshold.

    Args:
        conn:      ibm_db connection object
        threshold: Stock level below which a product is considered low (default 10)

    Returns:
        List of dicts with keys: product_id, name, category, stock_qty
    """
    sql = """
        SELECT product_id, name, category, stock_qty
        FROM INVENTORY
        WHERE stock_qty < ?
        ORDER BY stock_qty ASC
    """
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, threshold)
    ibm_db.execute(stmt)

    results = []
    row = ibm_db.fetch_assoc(stmt)
    while row:
        results.append(dict(row))
        row = ibm_db.fetch_assoc(stmt)
    return results


def list_products(conn):
    """
    Return all products in the INVENTORY table.

    Args:
        conn: ibm_db connection object

    Returns:
        List of dicts with all INVENTORY columns
    """
    sql = "SELECT * FROM INVENTORY ORDER BY category, name"
    stmt = ibm_db.exec_immediate(conn, sql)

    results = []
    row = ibm_db.fetch_assoc(stmt)
    while row:
        results.append(dict(row))
        row = ibm_db.fetch_assoc(stmt)
    return results


# ---------------------------------------------------------------------------
# Search — ⚠️ intentional SQL injection vulnerability for Lab 1 Exercise 4
# ---------------------------------------------------------------------------

def search_inventory(conn, search_term):
    """
    Search the INVENTORY table by product name or category.

    Args:
        conn:        ibm_db connection object
        search_term: User-supplied search string

    Returns:
        List of matching product dicts
    """
    # WARNING: This function builds the SQL query by concatenating user input
    # directly into the query string. This is intentionally insecure for
    # teaching purposes. See Lab 1 Exercise 4.
    sql = "SELECT * FROM INVENTORY WHERE name LIKE '%" + search_term + "%' OR category LIKE '%" + search_term + "%'"

    stmt = ibm_db.exec_immediate(conn, sql)

    results = []
    row = ibm_db.fetch_assoc(stmt)
    while row:
        results.append(dict(row))
        row = ibm_db.fetch_assoc(stmt)
    return results
