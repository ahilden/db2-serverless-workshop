"""
app.py — Main entry point for the Db2 Inventory Sample App

Usage:
    python app.py           # Run the interactive demo
    python app.py --setup   # Create the database schema and load sample data
    python app.py --test    # Run a connectivity test only
"""

import sys
import db
import queries


def setup(conn):
    """Create schema and load sample data."""
    print("\n=== Setting up schema ===")
    queries.create_schema(conn)

    print("\n=== Loading sample data ===")
    queries.add_product(conn, "Bolt M8x20",       "Fasteners",  "Hex head bolt, M8 x 20mm, zinc plated",   0.15,  500)
    queries.add_product(conn, "Nut M8",            "Fasteners",  "Hex nut, M8, zinc plated",                 0.08,  800)
    queries.add_product(conn, "Steel Plate 2mm",   "Sheet Metal", "Cold rolled steel sheet, 2mm x 1m x 2m", 45.00,   8)
    queries.add_product(conn, "Aluminium Rod 10mm","Sheet Metal", "Aluminium round bar, 10mm diameter, 1m",  12.50,  35)
    queries.add_product(conn, "Safety Gloves L",   "PPE",        "Cut-resistant gloves, size large",          8.99,   3)
    queries.add_product(conn, "Safety Goggles",    "PPE",        "Anti-fog safety goggles, clear lens",       6.50,  50)
    queries.add_product(conn, "Cutting Disc 115mm","Consumables","Angle grinder cutting disc, 115mm",         1.20,   7)
    queries.add_product(conn, "Drill Bit 6mm",     "Consumables","HSS twist drill bit, 6mm",                  0.95, 120)

    print("\nSample data loaded. Run 'python app.py' to start the demo.")


def run_demo(conn):
    """Run a short interactive demo of the application."""
    print(f"\n{'='*50}")
    print("  Db2 Serverless Inventory App — Demo")
    print(f"{'='*50}\n")

    # List all products
    print("--- All Products ---")
    products = queries.list_products(conn)
    for p in products:
        print(f"  [{p['PRODUCT_ID']:>3}] {p['NAME']:<25} {p['CATEGORY']:<15} "
              f"stock: {p['STOCK_QTY']:>4}  €{float(p['UNIT_PRICE']):.2f}")

    # Low stock report
    print("\n--- Low Stock (< 10 units) ---")
    low = queries.get_low_stock(conn, threshold=10)
    if low:
        for p in low:
            print(f"  ⚠️  {p['NAME']:<25} only {p['STOCK_QTY']} units remaining")
    else:
        print("  All products adequately stocked.")

    # Stock movement
    print("\n--- Recording Stock Movement ---")
    queries.update_stock(conn, product_id=1, change_type="IN",  quantity=200)
    queries.update_stock(conn, product_id=5, change_type="OUT", quantity=1)

    # Search (uses the vulnerable function — for Exercise 4)
    print("\n--- Search: 'Fasteners' ---")
    results = queries.search_inventory(conn, "Fasteners")
    for r in results:
        print(f"  {r['NAME']}")

    print("\nDemo complete.\n")


def connectivity_test(conn):
    """Run a simple connectivity check."""
    import ibm_db
    sql = "SELECT TABNAME FROM SYSCAT.TABLES WHERE TABSCHEMA = CURRENT SCHEMA FETCH FIRST 5 ROWS ONLY"
    stmt = ibm_db.exec_immediate(conn, sql)
    print("\n--- Connectivity Test: tables in current schema ---")
    row = ibm_db.fetch_assoc(stmt)
    found = False
    while row:
        print(f"  {row['TABNAME']}")
        row = ibm_db.fetch_assoc(stmt)
        found = True
    if not found:
        print("  (no tables found in current schema — run --setup first)")
    print("\nConnection successful.\n")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "--demo"

    print("Connecting to Db2 Serverless...")
    conn = db.get_connection()
    print("Connected.\n")

    try:
        if mode == "--setup":
            setup(conn)
        elif mode == "--test":
            connectivity_test(conn)
        else:
            run_demo(conn)
    finally:
        db.close_connection(conn)


if __name__ == "__main__":
    main()
