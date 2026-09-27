# Db2 Serverless Inventory Sample App

A simple inventory management application that connects to **IBM Db2 Serverless** using the `ibm_db` Python driver. This application is the starting point for **Lab 1** of the IDUG EMEA workshop.

---

## Project Structure

```
sample-app/
├── README.md           ← You are here
├── env-template.txt    ← Template showing the .env variables the app expects
├── .env                ← Created automatically in Lab 1 Exercise 1 (not in git)
├── db.py               ← Database connection helper (reads credentials from .env)
├── queries.py          ← SQL query functions (includes a deliberate flaw to find!)
├── app.py              ← Main application entry point
└── requirements.txt    ← Python dependencies (ibm_db, python-dotenv)
```

---

## Prerequisites

- Python 3.8+
- An IBMid registered with Andrew for workshop access
- Bob installed and configured with the Db2 Serverless MCP server (see `resources/installation.md`)

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Provision your Db2 Serverless branch and write `.env` (Lab 1 Exercise 1)

**You do not configure credentials manually.** In Lab 1 Exercise 1, Bob uses the
Db2 Serverless MCP server to:
1. Provision a project
2. Create a branch
3. Retrieve connection credentials
4. Write them to a `.env` file in this directory

The `.env` file is then loaded automatically by `db.py` at runtime via `python-dotenv`.

See `env-template.txt` for the expected variable names if you ever need to create `.env` manually.

### 3. Create the schema

```bash
python app.py --setup
```

### 4. Run the app

```bash
python app.py
```

---

## What the App Does

- Maintains an **INVENTORY** table tracking products and stock levels
- Supports adding products, updating stock, and searching by name or category
- Logs all stock changes to an **INVENTORY_LOG** table

---

## Lab 1 Exercises

| Exercise | What you'll do |
|---|---|
| Exercise 1 | Use the Db2 Serverless MCP server to provision a project, create a branch, and write `.env` |
| Exercise 2 | Explore the project structure and understand the code using Bob |
| Exercise 3 | Run the app and create the schema through Bob |
| Exercise 4 | Find and analyze a SQL injection vulnerability in `queries.py` |
| Exercise 5 | Use Bob's Ask / Plan / Agent modes to plan and implement a schema extension |
