"""
db.py — Db2 Serverless connection helper

Reads connection credentials from credentials.env in the project directory.
The credentials.env file is created by the Db2 Serverless MCP server during
lab setup (see Lab 1 Exercise 1) — you never need to edit it manually.

Use:
    from db import get_connection, close_connection
    conn = get_connection()
    # ... do work ...
    close_connection(conn)
"""

import os
import ibm_db
from dotenv import load_dotenv

# Load credentials from credentials.env in the project root
load_dotenv("credentials.env")


def get_connection():
    """
    Open and return a connection to Db2 Serverless.

    Credentials are read from credentials.env written by the
    Db2 Serverless MCP server during Lab 1 Exercise 1.

    Returns:
        ibm_db connection object

    Raises:
        EnvironmentError: if required environment variables are missing
        Exception: if the connection cannot be established
    """
    required = ["DB2_HOSTNAME", "DB2_PORT", "DB2_DATABASE", "DB2_UID", "DB2_PWD"]
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            "Run Lab 1 Exercise 1 to provision a Db2 Serverless branch and write credentials.env"
        )

    conn_str = (
        f"DATABASE={os.getenv('DB2_DATABASE')};"
        f"HOSTNAME={os.getenv('DB2_HOSTNAME')};"
        f"PORT={os.getenv('DB2_PORT')};"
        f"PROTOCOL=TCPIP;"
        f"UID={os.getenv('DB2_UID')};"
        f"PWD={os.getenv('DB2_PWD')};"
        f"SECURITY={os.getenv('DB2_SECURITY', 'SSL')};"
    )

    try:
        conn = ibm_db.connect(conn_str, "", "")
        return conn
    except Exception as e:
        raise Exception(f"Failed to connect to Db2 Serverless: {e}")


def close_connection(conn):
    """
    Close a Db2 connection.

    Args:
        conn: ibm_db connection object to close
    """
    if conn:
        ibm_db.close(conn)
