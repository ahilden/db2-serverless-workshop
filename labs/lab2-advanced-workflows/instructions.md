# Lab 2: Advanced Bob Workflows — Db2 Serverless with Bob

**Duration:** 25 minutes  
**Difficulty:** Intermediate  
**Prerequisites:** Completed Lab 1  
**Facilitators:** Andrew Hilden (ahilden@ca.ibm.com) | Jillian Quiller, Db2 Serverless Product Manager (jmquille@us.ibm.com)

## 🎯 Objectives

By the end of this lab, you will be able to:
- Use the **Db2 Serverless MCP `runsql` tool** to run SQL directly from Bob — no Python required
- Use Bob's **agentic workflows** to scaffold a multi-file Db2 application from a single prompt, wiring it to an MCP-provisioned branch via `.env`
- Delegate focused work using **sub-tasks** — keeping your main conversation clean
- Switch Bob modes mid-conversation (Ask → Plan → Agent) fluidly
- Run a pre-built **Bob Workflow** (code review)
- Understand the **Bob Marketplace** as a source of MCP servers, modes, and skills

## 📋 Prerequisites

- [ ] Completed Lab 1 (Db2 Serverless MCP server configured, project and branch provisioned)
- [ ] Bob installed and running — `resources/installation.md`
- [ ] `.env` file written by Lab 1 Exercise 1 is present in your project directory

---

## 🔨 Exercises

### Exercise 1: Run SQL Directly from Bob using MCP `runsql` (5 minutes)

**Scenario:** You've built a schema in Lab 1. Now use the MCP server's `runsql` tool to query it directly from Bob — without writing a Python script or opening a database client.

**Tasks:**
1. Ask Bob to use the `runsql` MCP tool to list the tables in your schema
2. Ask Bob to run a SELECT query against the INVENTORY table
3. Ask Bob to run a more complex query — stock value by category

**Bob Tools Used:** `db2-serverless` MCP → `runsql`

**Example Prompts:**
```
Show me the schema of the database
```
```
Use runsql to query the INVENTORY table and show me all products
with stock_qty below 10, ordered by stock_qty ascending.
```
```
Use runsql to calculate total stock value by category:
```

**💡 Bonus:** Ask other questions about the data as well.


**Expected Outcome:**
- SQL results appear directly in the Bob conversation — no separate database client, no Python script
- You see the low-stock items from the sample data loaded in Lab 1
- You understand the distinction: `runsql` via MCP = admin/exploration SQL from Bob; Python driver = application runtime SQL

**💡 MCP `runsql` vs Python `ibm_db` — when to use each:**

| Situation | Use |
|---|---|
| Exploring schema, running ad-hoc queries, setup validation | MCP `runsql` |
| Application code that runs SQL at scale or in a loop | Python `ibm_db` driver |
| Schema migrations, DDL during provisioning | MCP `runsql` |
| User-facing search, insert, update in an app | Python `ibm_db` driver |

---

### Exercise 2: Agentic Workflow — Scaffold a New Db2 Application in One Prompt (8 minutes)

**Scenario:** You need a second application — an expense tracker — connected to the same Db2 Serverless branch. Use Bob to scaffold the entire project from one prompt, then wire it to the branch using the existing `.env`.

**Tasks:**
1. Ask Bob to provision a new branch for the expense tracker (MCP)
2. Write a single agentic prompt to scaffold the full application
3. Review what was generated

**Step 1 — Provision a branch:**
```
Use the db2-serverless MCP server to create a new branch called "expense"
on the lab1-inventory project. Use the "inventory" branch from Lab 1 as the
parent so the branch already has the INVENTORY schema and seed data.
Get the connection credentials and write them to expense-tracker/credentials.env
```

> Wait for the branch to become active


**Step 2 — Scaffold the application (Agent mode):**
```
Create a Python expense tracker application in the expense-tracker/ directory that:
- Loads Db2 Serverless credentials from expense-tracker/credentials.env using python-dotenv
- Connects via ibm_db
- Has a schema with one table:
    EXPENSES (expense_id IDENTITY, description VARCHAR(200), amount DECIMAL(10,2),
              category VARCHAR(50), expense_date DATE, submitted_by VARCHAR(100))
- Provides functions:
    add_expense(description, amount, category, expense_date, submitted_by)
    get_expenses_by_category(category)
    get_monthly_total(year, month)
- Uses parameterized queries throughout — no string concatenation in SQL
- Includes app.py, db.py, queries.py, requirements.txt, README.md
```

**Expected Outcome:**
- Bob creates the full `expense-tracker/` directory with all five files
- `db.py` reads from `expense-tracker/credentials.env` — the credentials MCP wrote in Step 1
- All SQL uses parameterized queries
- You've seen how MCP + agentic scaffolding work together: MCP provisions and wires, Bob builds

**💡 What makes this "agentic"?**
Bob didn't answer a question — it planned a file creation sequence, executed it in order, and verified the output. Together they replaced 30+ minutes of manual setup.

**Step 3 — Run the application:**
```
Run the expense tracker application using app.py --setup to create the schema,
then run it again to add sample expenses and display the results.
```

**Expected Outcome:**
- `EXPENSES` table created in the `expense` branch
- Sample expenses inserted and displayed
- Application runs end-to-end without leaving Bob

---

**💡 Bonus: Ask questions about the database and what was created and ask Bob to verify it. If the tables weren't created, just ask.**


### Exercise 3: Sub-Tasks — Delegating Focused Work (5 minutes)

**Scenario:** You want to add a reporting module to the expense tracker, but you don't want reporting logic to clutter your main conversation about the schema.

**Example Prompt:**
```
Create a sub-task to build a reporting module for the expense tracker in expense-tracker/reporting.py.
The sub-task should implement:
- monthly_summary(year, month): total expenses and count grouped by category
- top_spenders(limit=5): submitters ranked by total spend
- export_to_csv(report_data, filename): save any report to CSV
The sub-task should work independently and report back a summary when done.
```

**Expected Outcome:**
- Bob spawns a child task focused only on the reporting module
- Main conversation stays clean — no context overload
- Sub-task creates `reporting.py` and reports back a summary

**💡 Why sub-tasks matter:**
For large implementations — a full migration tool, a multi-table reporting suite, a test harness — sub-tasks prevent context overload and give each piece of work the full focus of a fresh conversation. You get better output and a cleaner history.

---


> Now explore and maybe add an option to the expense application to export all the results using the reporting module. Give it a try.

### Exercise 4: Mode Switching Mid-Conversation (5 minutes)

**Scenario:** Mid-implementation you need to make a design decision. Switch modes without losing context.

**Example Workflow:**
```
[Agent mode]
"Add error handling to all database functions in expense-tracker/db.py,
logging errors with a timestamp."

[Switch to Ask mode]
"What is the difference between using the MCP runsql tool and ibm_db for
running DDL statements like CREATE TABLE? Which is better for schema setup?"

[Switch to Plan mode]
"Plan how we'd add a BUDGET table to the expense tracker schema, including
the DDL, a foreign key relationship to EXPENSES, and the new Python functions."

[Switch to Agent mode]
"Implement step 1 of the plan — use the MCP runsql tool to run the CREATE TABLE
DDL for the BUDGET table on the expense-tracker branch."
```

**Expected Outcome:**
- Natural flow between knowledge, strategy, and implementation in a single conversation
- Ask mode never makes changes — safe for research
- The final Agent step uses MCP `runsql` to run DDL directly, not Python — demonstrating the right tool for setup SQL

---

### Exercise 5: Pre-Built Bob Workflow — Code Review (2 minutes)

**Scenario:** Before moving to Lab 3, run a code review on the expense tracker.

**Example Prompt:**
```
Run a code review on the expense-tracker/ application. Focus on:
- SQL injection (parameterized queries, no string concatenation)
- Error handling completeness
- Db2 best practices (connection management, query patterns)
- Missing input validation
```

**Expected Outcome:**
- Structured report with severity levels
- Consistent, repeatable output — not an ad-hoc answer

**💡 Bob Workflows are curated, multi-step processes** — they include tool calls, structured analysis, and formatted output. They run the same way every time.

---

## 🎓 Key Takeaways

1. **MCP `runsql`** — run ad-hoc and setup SQL directly from Bob. No database client, no Python script needed.
2. **MCP + agentic scaffolding** — MCP provisions and wires credentials; Bob builds the application. Together they replace 30+ minutes of manual work.
3. **Sub-tasks** — delegate large, focused pieces of work; main conversation stays clean.
4. **Mode switching** — Ask → knowledge, Plan → strategy, Agent → implementation. One conversation, multiple gears.
5. **Pre-built Workflows** — repeatable, consistent processes for code review, PR creation, documentation.

## 💰 Business Impact

### ⏱️ Productivity Gains
- **`runsql` via MCP**: Ad-hoc schema exploration and DDL from Bob — no context switching to a DB client
- **MCP + agentic scaffolding**: Full application wired to a real Db2 branch in ~90 seconds
- **Sub-tasks**: Large features complete 40% faster with less context loss

### 🔒 Security
- Code review catches SQL injection before delivery
- Parameterized queries enforced in all generated code
- Credentials flow from MCP → `.env` → app — never hardcoded

### 💵 Cost Savings (IBM Client Zero data)
- Teams using agentic workflows report **10–15 hours saved per developer per week**
- Automated code reviews catch issues **3× earlier** in the development cycle

---

## ✅ Completion Checklist

- [ ] Exercise 1: Used MCP `runsql` to run SQL queries directly from Bob
- [ ] Exercise 2: Scaffolded an expense tracker app wired to an MCP-provisioned branch
- [ ] Exercise 3: Created a sub-task for the reporting module
- [ ] Exercise 4: Practised mode switching — including using MCP `runsql` for DDL in Agent mode
- [ ] Exercise 5: Ran a pre-built code review workflow
- [ ] Understand when to use MCP `runsql` vs the Python `ibm_db` driver

## 📤 Share Your Session — Pre-GA Feedback

> This takes about 2 minutes and is the most valuable feedback you can give. Please don't skip it!

In your current Bob conversation, enter this prompt:

```
You are working with Db2 Serverless via the db2-serverless MCP server.
Replay and document the following session in full with the prompts asked,
questions answered, tool calls and their results as HTML.
Mask any passwords, API keys, or secrets — replace each with [REDACTED].
```

Then save the file:

```
Save the HTML to a file called lab2-session-export.html in the current directory.
```

Email `lab2-session-export.html` to **ahilden@ca.ibm.com** and **jmquille@us.ibm.com** with subject:

```
Db2 Serverless Workshop — Lab 2 Session Export [your name]
```

> 💡 Include any observations in the email body — what worked well, what was confusing, what you'd like to see.

## 🚀 Next Steps

→ Move on to **Lab 3: Db2 Serverless Use Case Labs**

## 📚 Resources

- **Bob Installation & MCP Setup:** `resources/installation.md`
- **Bob Documentation:** https://ibm.biz/bob-doc
- **Db2 Serverless Docs:** https://cloud.ibm.com/docs/Db2onCloud
- **Cheat Sheet:** `resources/cheat-sheet.md`
- **Troubleshooting:** `resources/troubleshooting.md`

---

**Need Help?** Ask Andrew (ahilden@ca.ibm.com) or Jillian (jmquille@us.ibm.com)
