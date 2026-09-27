# Lab 3: Db2 Serverless Use Case Labs

**Duration:** 60 minutes  
**Difficulty:** Advanced  
**Prerequisites:** Completed Labs 1 and 2  
**Facilitators:** Andrew Hilden (ahilden@ca.ibm.com) | Jillian Quiller, Db2 Serverless Product Manager (jmquille@us.ibm.com)

## 🎯 Objectives

By the end of this lab, you will have:
- Provisioned a dedicated Db2 Serverless branch for each use case using the **MCP server**
- Built a **native Java application** connecting to Db2 Serverless via the JCC JDBC driver
- Driven a complete **database management workflow** — branching, users, and SQL — using the Db2 Serverless MCP server directly from Bob
- Shared early feedback on your experience with Db2 Serverless and Bob

## 📋 Prerequisites

- [ ] Completed Labs 1 and 2
- [ ] Bob installed and running — see `resources/installation.md` (https://bob.ibm.com/download)
- [ ] IBMid configured in Bob
- [ ] Db2 Serverless MCP server configured in `~/.bob/mcp.json` — see `resources/installation.md` Step 6
- [ ] JCC JDBC driver JAR available (`db2jcc4.jar`) — for Use Case 2
- [ ] Java 11+ and Maven installed — for Use Case 2

---

> **Choose your path.** You have 60 minutes. Options:
> - Work through **Use Case 2** (Java JDBC app) for a full end-to-end application (~30 min)
> - Work through **Use Case 3** for a full MCP-driven database management workflow (~25 min)
> - Spend the full time on one use case for deeper exploration

---

## 🔑 Branch Setup — Do This First for Each Use Case

Each use case runs against its own dedicated Db2 Serverless branch created from the root branch of the project you created earlier. This keeps schemas isolated and avoids conflicts between exercises.

**Before starting each use case, ask Bob:**
```
Use the db2-serverless MCP server to create a new branch called "branch name"
on the lab1-inventory project using the main branch as the parent.
Then get the connection credentials for that branch and write them to
credentials.env in this format:

DB2_HOSTNAME=...
DB2_PORT=...
DB2_DATABASE=...
DB2_UID=...
DB2_PWD=...
DB2_SECURITY=...
```

| Use Case | Branch Name | Directory |
|---|---|---|
| Use Case 2 — Java JDBC App | `java-catalog` | `java-product-catalog/` |
| Use Case 3 — MCP Workflow | `mcp-workflow` | *(no app files — MCP only)* |

---

## 🔮 Use Case 1: REST API App Using Db2 Serverless RunSQL _(Future Workshop)_

> **This use case is reserved for a future workshop.** The Db2 Serverless REST API RunSQL endpoint specification is not yet finalized. The content below is a preview of what will be available — it is **not intended to be run today**.

**Business Value:** DBAs can build REST-backed database applications without learning complex application frameworks. Bob handles the scaffolding — you bring the SQL expertise.

### What this will cover (future workshop)
- Build a Python **expense tracker** that executes SQL over HTTPS using the Db2 Serverless REST API RunSQL endpoint — no JDBC driver required
- Bob scaffolds the full application, creates the schema, inserts sample data, and runs a security analysis
- Demonstrates how Bob bridges SQL expertise and application development for DBAs

---

## 📝 Use Case 2: Native Java Application with Db2 JCC Driver

**Priority:** High  
**Estimated Time:** 25 minutes  
**Business Value:** DBAs often need to provide Java application teams with Db2 connection code.
Bob generates production-quality JDBC boilerplate — connection URLs, SSL config, PreparedStatements,
result-set handling — in seconds instead of hours.

### Scenario

Build a **product catalog** Java application that connects directly to Db2 Serverless using the
**IBM Db2 JCC JDBC driver** (`db2jcc4.jar`).

### Tasks

**Step 1 — Provision the branch (MCP):**
```
Use the db2-serverless MCP server to create a new branch called "java-catalog"
on the lab1-inventory project using the main branch as the parent.
Get the connection credentials and write them to java-product-catalog/.env
```

**Step 2 — Scaffold the Maven project (Agent mode):**
```
Create a Java Maven application in the java-product-catalog/ directory that connects
to IBM Db2 Serverless using the JCC JDBC driver. The application should:
- Have a Db2Connection class reading DB2_HOSTNAME, DB2_PORT, DB2_DATABASE,
  DB2_UID, DB2_PWD from the .env file using a properties loader
- Use this JDBC URL format:
  jdbc:db2://<host>:<port>/<database>:sslConnection=true;
- Have a ProductCatalog class with:
    createSchema(): CREATE TABLE PRODUCTS (product_id INT NOT NULL GENERATED ALWAYS AS IDENTITY,
      name VARCHAR(100), description VARCHAR(500), price DECIMAL(10,2), category VARCHAR(50),
      PRIMARY KEY (product_id))
    addProduct(name, description, price, category): INSERT using PreparedStatement
    getProductsByCategory(category): SELECT using PreparedStatement, returns List<Map>
    searchProducts(keyword): LIKE search on name and description
    updatePrice(productId, newPrice): UPDATE using PreparedStatement
- Use try-with-resources for all connections and statements
- Include pom.xml with db2jcc4 dependency (scope: system, path: lib/db2jcc4.jar)
- Include a README explaining how to place the JCC driver JAR
```

**Step 3 — Review the generated JDBC code:**
```
Read the Db2Connection class and explain:
1. How is SSL configured for Db2 Serverless in this JDBC URL?
2. Why is try-with-resources important for JDBC connections?
3. What would happen if we didn't close the ResultSet?
```

**Step 4 — Compile and create the schema:**
```
Set the required environment variables from java-product-catalog/.env,
then compile the Maven project. If there are compilation errors, fix them.
Once compiled, run createSchema() to create the PRODUCTS table.
```

**Step 5 — Add products and query:**
```
Add three sample products in different categories: Electronics, Clothing, Books.
Then call getProductsByCategory("Electronics") and display the results.
```

**Step 6 — Bob Findings on the JDBC code:**
```
Analyze the JDBC code for:
- SQL injection vulnerabilities (are all queries using PreparedStatement?)
- Connection management issues (any unclosed connections or statements?)
- SSL/TLS configuration for Db2 Serverless
- Exception handling gaps
```

**Step 7 — Add a workload test option:**

```
Add a test option which will run a workload on the database
```

**Example Prompt:**
```
Run the workload test and show me the results.
```

**Expected Outcome:**
- A test mode is added to the application that inserts and queries a realistic volume of records
- Bob executes the workload and reports timing and row counts

### Success Criteria
- [ ] `java-catalog` branch provisioned via MCP from the `main` branch
- [ ] Maven project compiles with JCC driver
- [ ] `PRODUCTS` table created in the `java-catalog` branch
- [ ] `addProduct()` uses `PreparedStatement` — no string concatenation
- [ ] `getProductsByCategory()` returns correct results
- [ ] `try-with-resources` used consistently throughout
- [ ] Bob Findings confirm safe JDBC patterns

### 💡 Key Bob Differentiators Demonstrated
- **App scaffolding for DBAs**: JDBC boilerplate + SSL config + Maven structure in seconds vs. 2–3 hours of research
- **Sub-task opportunity**: Ask Bob to use a sub-task for schema definition vs. application logic
- **Literate coding**: Bob explains JDBC patterns (try-with-resources, PreparedStatement) in terms DBAs understand

---

## 📝 Use Case 3: Db2 Serverless Database Workflow with Bob (MCP)

**Priority:** High  
**Estimated Time:** 25 minutes  
**Business Value:** The Db2 Serverless MCP server is a real, working tool you can use today. Drive branching, user management, and SQL from natural language prompts in Bob — without ever opening the IBM Cloud console.

### Scenario

Drive a complete Db2 Serverless database management workflow — provisioning a branch, managing users, and querying the database — all from Bob using the MCP server.

### Tasks

**Step 1 — Provision a branch for this workflow (MCP):**
```
Use the db2-serverless MCP server to create a new branch called "mcp-workflow"
on the lab1-inventory project using the main branch as the parent.
Show me the branch details once it's ready.
```

**Step 2 — Get connection info:**
```
Get the connection information for the mcp-workflow branch of lab1-inventory.
Show me the hostname, port, and JDBC URL.
```

**Step 3 — List and create users:**
```
List the existing users on the mcp-workflow branch.
Then create a new user called "appuser" with group "bluusers".
```

**Step 4 — Run SQL directly from Bob:**

```
Use the db2-serverless MCP runsql tool to run the following on the mcp-workflow branch:

CREATE TABLE WORKFLOW_LOG (
  log_id    INT NOT NULL GENERATED ALWAYS AS IDENTITY,
  event     VARCHAR(200),
  logged_at TIMESTAMP DEFAULT CURRENT TIMESTAMP,
  PRIMARY KEY (log_id)
)

Then insert a row:
INSERT INTO WORKFLOW_LOG (event) VALUES ('mcp-workflow lab completed')

Then query it:
SELECT * FROM WORKFLOW_LOG
```

### MCP Tools Used in This Use Case

| Step | MCP Tool |
|---|---|
| Provision branch | `create_branch` |
| Get connection info | `get_connection_info` |
| List users | `list_users` |
| Create user | `create_user` |
| Run SQL | `run_sql` |

### Success Criteria
- [ ] `mcp-workflow` branch provisioned from `main` via MCP
- [ ] Connection info retrieved and displayed
- [ ] User created on the branch
- [ ] SQL executed via `run_sql` without leaving Bob

### 💡 Key Bob Differentiators Demonstrated
- **Full MCP coverage**: Branch, users, and SQL — all from natural language in Bob
- **No IBM Cloud console**: Every operation in this use case runs through the MCP server
- **`run_sql`**: Execute DDL, DML, and queries directly from Bob — no database client needed
- **Context persistence**: Bob tracks the branch, project, and credentials throughout the conversation

### Why This Matters for DBAs

| Traditional Workflow | With Bob + Db2 Serverless MCP |
|---|---|
| Log into IBM Cloud console | Natural language prompt in Bob |
| Navigate to instance → branch UI | `create_branch` in one prompt |
| Open DB2 CLI or admin tool for DDL | `run_sql` |
| Copy-paste connection strings | `get_connection_info` writes to `.env` |
| Manage users via console UI | `create_user`, `list_users` |

---

## 🎓 Lab 3 Key Takeaways

1. **Every use case gets its own branch** — created from `main` via MCP. Isolated schemas, no cross-exercise conflicts.
2. **JCC JDBC** — The Java path to Db2 Serverless. Bob generates correct SSL config, PreparedStatements, and try-with-resources in seconds.
3. **Db2 Serverless MCP server** — Available now. Branch, users, and SQL from natural language in Bob — no IBM Cloud console needed.
4. **`run_sql` MCP tool** — Run ad-hoc SQL, DDL, and schema exploration directly from Bob — no database client needed.
5. **Security by default** — Bob always defaults to parameterized queries and flags SQL injection risks automatically.
6. **Your feedback matters** — Db2 Serverless is pre-GA. What you experienced today will directly influence the product before it ships.

## 💰 Business Impact

### ⏱️ Productivity Gains
- **JCC JDBC setup**: JDBC boilerplate with SSL + PreparedStatement + try-with-resources in ~20 seconds vs. 1–2 hours of research
- **MCP database management**: Branch, users, and SQL from Bob prompts vs. 15–20 minutes navigating IBM Cloud console screens

### 🔒 Security Enhancements
- **100% parameterized query enforcement** in generated code — eliminates SQL injection in new code by default
- **SSL auto-configured** in all JCC connection strings
- **Credentials from MCP → `.env` → app** — never hardcoded or copy-pasted

### 💵 Cost Savings
- DBAs who can build and maintain their own application integrations reduce dependency on dedicated app development teams
- Lower barrier to Db2 Serverless adoption — teams get to working code faster

---

## ✅ Completion Checklist

**Use Case 2 — JCC JDBC Java App:**
- [ ] `java-catalog` branch provisioned via MCP
- [ ] Maven project compiles with JCC driver
- [ ] `PRODUCTS` table created
- [ ] `PreparedStatement` and `try-with-resources` confirmed

**Use Case 3 — MCP Database Workflow:**
- [ ] `mcp-workflow` branch provisioned via MCP
- [ ] Connection info and users managed from Bob
- [ ] SQL executed via `run_sql` directly in Bob

---

## 📤 Share Your Session — Pre-GA Feedback

> **This step is important.** Db2 Serverless is pre-GA and your hands-on session is exactly the kind of real-world feedback that shapes the product. Please take 2 minutes to export your chat history and send it to Andrew and Jillian.

Your Bob chat history captures the prompts you used, the tool calls Bob made, and the results it got back — invaluable signal for the Db2 Serverless team.

**Step 1 — Export your session as HTML**

In your current Bob conversation, enter this prompt:

```
You are working with Db2 Serverless via the db2-serverless MCP server.
Replay and document the following session in full with the prompts asked,
questions answered, tool calls and their results as HTML.
Mask any passwords, API keys, or secrets — replace each with [REDACTED].
```

Bob will generate a self-contained HTML document summarising your entire session.

**Step 2 — Save the HTML file**

When Bob finishes generating the HTML, ask it to save the file:

```
Save the HTML to a file called lab3-session-export.html in the current directory.
```

**Step 3 — Email it to Andrew and Jillian**

Attach `session-export.html` and send it to **ahilden@ca.ibm.com** and **jmquille@us.ibm.com** with the subject line:

```
Db2 Serverless Workshop — Lab 3 Session Export [your name]
```

> 💡 Include any additional notes in the email body — what surprised you, what felt awkward, what you wished worked differently. Every detail helps.

---

**Need Help?** Ask Andrew (ahilden@ca.ibm.com) or Jillian (jmquille@us.ibm.com)
