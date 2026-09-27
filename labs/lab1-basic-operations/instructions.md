# Lab 1: Core Bob Operations — Db2 Serverless Context

**Duration:** 25 minutes  
**Difficulty:** Beginner  
**Facilitators:** Andrew Hilden (ahilden@ca.ibm.com) | Jillian Quiller, Db2 Serverless Product Manager (jmquille@us.ibm.com)

## 🎯 Objectives

By the end of this lab, you will be able to:
- Use the **Db2 Serverless MCP server** to provision a project, create a branch, and retrieve connection credentials — all from Bob
- Have Bob write those credentials to a `credentials.env` file that the Python application reads automatically
- Navigate and read a Db2-connected sample project using Bob
- Make targeted code edits with `apply_diff`
- Use Bob Findings to identify SQL injection vulnerabilities
- Switch between Ask, Plan, and Agent modes effectively

## 📋 Prerequisites

Before starting, ensure you have:
- [ ] Bob installed and running — see `resources/installation.md` (https://bob.ibm.com/download)
- [ ] **IBM Data Server Client 12.1.5 installed** — see `resources/installation.md` Step 2 (required for this lab)
- [ ] IBMid configured in Bob
- [ ] **Db2 Serverless MCP server configured** in `~/.bob/mcp.json` — see `resources/installation.md` Step 5
- [ ] Make sure you have a working git and python environment
- [ ] Sample project cloned and open in Bob (see **Getting the Sample Project** below)

## 📥 Getting the Sample Project

The sample application is hosted on GitHub. Clone it and get it the first labs requirements.

> 💡 **Python and Pip** You will need to make sure you have a working python environment

```bash
git clone https://github.com/andrewhildenibm-ops/idug-emea-db2serverless.git
cd idug-emea-db2serverless/labs/lab1-basic-operations/sample-app
pip install -r requirements.txt
```

> The repo contains:
> - `.env.example` — template showing the variables the app expects
> - `db.py` — Db2 Serverless connection helper (reads from `credentials.env`)
> - `queries.py` — SQL functions (includes a flaw to find in Exercise 4!)
> - `app.py` — main application entry point
> - `requirements.txt` — Python dependencies (`ibm_db`, `python-dotenv`)

> 💡 **New to application code?** No problem — Bob handles the boilerplate.
> Your SQL and schema expertise is the most valuable skill in this lab.

---

## 📥 Open up the repo in bob

File -> Open -> Select Folder (Browse to the folder where you cloned the idug-emea-db2serverless repo)

> 💡 Bob will open the folder in Restricted Mode.  Click on `Manage` in the top message at the top of the window and click "In a Trusted Folder"

---

## 🔨 Exercises

### Exercise 1: Provision a Db2 Serverless Project and Branch via MCP (5 minutes)

**Scenario:** Before the application can run, it needs a Db2 Serverless database to connect to. Instead of logging into the IBM Cloud console, you'll use the **Db2 Serverless MCP server** directly from Bob to provision a project, create a branch, and retrieve the connection credentials.

**Tasks:**
1. Ask Bob to provision a new Db2 Serverless project using the MCP server
2. Ask Bob to create a branch on that project
3. Ask Bob to retrieve the connection credentials and write them to a `credentials.env` file

**Bob Tools Used:** `db2-serverless` MCP tools — `create_project`, `create_branch`, `get_connection_info`, `create_user`; then `write_file` to save `credentials.env`

**Example Prompts:**
```
Use the db2-serverless MCP server to provision a new project called "lab1-inventory".
```

> 💡 **Normally project will be created very quickly but during this exercise it may take a minute or so.  Wait for the project to be Active**

```
Get the status of the project I just created.
```

The sample app we will work with is in the `labs/lab1-basic-operations/sample-app` directory.

```
Create a branch called "inventory" on the lab1-inventory project.
```

> 💡 **Normally Branch will be created very quickly but during this exercise it may take a minute or so.  Wait for the Branch to be Active**


```
Get the status of the Branch I just created.
```



```
Create a user named testuser with a generated password and get the connection credentials for the inventory branch of lab1-inventory.  Write them to a labs\lab1-basic-operations\sample-app\credentials.env file using this format:
DB2_HOSTNAME=...
DB2_PORT=...
DB2_DATABASE=...
DB2_UID=...
DB2_PWD=...
DB2_SECURITY=...
```

**Expected Outcome:**
- A Db2 Serverless project and branch provisioned in seconds — no IBM Cloud console needed
- A `credentials.env` file created in the project directory containing the branch connection credentials

**💡 Real-time Value Indicator:**
What normally takes 20-25 minutes clicking through IBM Cloud portal screens (provision → configure → get credentials) happens in a single Bob conversation. The credentials land directly in the file the application needs — no copy-paste, no credential errors.

---

### Exercise 2: Understand the Sample Project (5 minutes)

**Scenario:** You've cloned the Db2 Serverless inventory application. Use Bob to understand it — without reading every file manually.

**Tasks:**
1. Ask Bob to give you a high-level overview of the project structure
2. Ask Bob to explain `db.py` — how does it read the `credentials.env` file and connect?
3. Ask Bob to explain what `queries.py` does and list the functions it contains

**Bob Tools Used:** `list_files`, `read_file`, natural language explanation (Ask mode)

**Example Prompts:**
```
List all files in the sample-app under lab 1 and give me a one-line summary of what each one does.
```
```
Read db.py and explain how it connects to Db2 Serverless.
Where does it read the credentials from?
```
```
Read queries.py and summarise all the functions — what does each one do?
```

**Expected Outcome:**
- You understand the project structure in under 2 minutes
- You know that `db.py` uses `python-dotenv` to load credentials from `credentials.env`
- You know that `queries.py` contains `add_product()`, `update_stock()`, `get_low_stock()`, `list_products()`, and `search_inventory()`

**💡 Real-time Value Indicator:**
Bob reads and explains an unfamiliar codebase in seconds. For a DBA onboarding to an application,
this replaces 30–60 minutes of manual exploration and developer Q&A.

---

### Exercise 3: Run the Application (5 minutes)

**Scenario:** The `credentials.env` file is in place from Exercise 1. Use Bob to create the schema and run the application — without switching to a separate terminal.

**Tasks:**
1. Ask Bob to create the schema by running `python app.py --setup`
2. Ask Bob to run the application demo with `python app.py`

**Bob Tools Used:** `execute_command`

**Example Prompts:**
```
Run: python app.py --setup
Tell me what tables were created and show me any errors.
```
```
Run: python app.py
Explain what the output means.
```

**Expected Outcome:**
- `INVENTORY` and `INVENTORY_LOG` tables created in the Db2 Serverless branch
- Demo output shows sample products, a low-stock warning, and a search result
- You understand how Bob executes commands without you leaving the Bob interface

---

### Exercise 4: Bob Findings — Spot the SQL Injection in `search_inventory()` (5 minutes)




**Scenario:** `queries.py` contains a deliberate SQL injection vulnerability in `search_inventory()`. This mirrors a real pattern DBAs sometimes write when first building Python applications. Ask Bob to find it.

**Tasks:**
1. Ask Bob to analyze `queries.py` for security issues
2. Identify exactly which line is vulnerable and why
3. Ask Bob to show you the safe, parameterized version

**Example Prompts:**
```
Read queries.py and analyze it for SQL injection vulnerabilities.
Give me specific findings with severity levels and the line number of the problem.
```
```
Show me the safe, parameterized version of the search_inventory() function.
Explain why the current version is dangerous and how the fix prevents the attack.
```

**Expected Outcome:**
- Bob flags the string concatenation in `search_inventory()` as a critical SQL injection risk
- Bob identifies the exact line: `sql = "SELECT * FROM INVENTORY WHERE name LIKE '%" + search_term + "%'..."`
- Bob provides a corrected version using `ibm_db.prepare()` and `ibm_db.bind_param()`
- You understand the attack: a user could pass `' OR '1'='1` to return all rows

**💡 Real-time Value Indicator:**
Bob catches SQL injection risks in seconds — the same issue a security review might only catch after code reaches staging.

---

### Exercise 5: Bob Modes in Practice (5 minutes)

**Scenario:** Experience how choosing the right Bob mode changes what you get back.

**Tasks:**
1. Use **Ask mode** — ask Bob to explain what the MCP `runsql` tool does and when you'd use it vs the Python driver
2. Use **Plan mode** — plan adding a `SUPPLIERS` table to the schema
3. Use **Agent mode** — implement the DDL file for that table
4. Explore on your own!!

> 💡 **Switch Modes** Switch to the mode before each prompt

**Example Workflow:**
```
[Ask mode]
"What is the difference between using the Db2 Serverless MCP runsql tool
and running SQL through the ibm_db Python driver? When would you use each?"

[Plan mode]
"I want to add a SUPPLIERS table (supplier_id, name, contact_email, country)
with a foreign key from INVENTORY. Plan the DDL and any application changes needed."

[Agent mode]
"Switch to Agent Mode and mplement step 1 of the plan — create a file called schema/suppliers.sql
with the CREATE TABLE and ALTER TABLE statements."
```


**💡 Complete the rest of the tasks with your own prompt:**


**Expected Outcome:**
- Ask mode explains the tradeoff: MCP = admin/setup tasks from Bob; driver = application runtime SQL
- Plan mode produces a clear, ordered set of steps
- Agent mode creates the SQL file without touching anything else

---

## 🎓 Key Takeaways

1. **Db2 Serverless MCP server for setup** — provision, branch, and get Db2 Serverless connection information using Db2 Serverless and Bob.
2. **`credentials.env` for credentials** — MCP writes connection info once; the app reads it on every run. Clean separation of concerns.
3. **Python driver for runtime SQL** — `ibm_db` is the right tool once you're in the application. Direct, fast, native.
4. **`apply_diff` for safe edits** — surgical changes that don't accidentally break other parts of a file.
5. **Security analysis** — Bob catches SQL injection and security vulnerabilities automatically.
6. **Mode switching** — Ask for knowledge, Plan for strategy, Agent for implementation.

## 💰 Business Impact

### ⏱️ Productivity Gains
- **Provisioning via MCP**: 5–10 minutes of clicks or remember command lines, provisioning time's in 10's of minutes → simple Bob prompts and deployed in seconds.
- **Credential wiring**: No copy-paste errors — Bob writes the `credentials.env` directly
- **Codebase understanding**: DBAs understand unfamiliar application code signficantly faster and more accurately.

### 🔒 Security Enhancements
- **SQL injection detection**: Catches parameterized query violations automatically
- **Credentials in `credentials.env`**: Never hardcoded in source files

### 💵 Cost Savings (IBM Client Zero data)
- **4–6 hours saved per developer per week** on routine code tasks
- **40% faster onboarding** for DBAs moving into application development

---

## ✅ Completion Checklist

- [ ] Exercise 1: Used MCP server to provision a project, create a branch, and write `credentials.env`
- [ ] Exercise 2: Understood sample project structure using Bob
- [ ] Exercise 3: Ran the application and created the schema
- [ ] Exercise 4: Used Bob Findings to identify the SQL injection risk
- [ ] Exercise 5: Practiced Ask, Plan, and Agent modes

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
Save the HTML to a file called lab1-session-export.html in the current directory.
```

Email `lab1-session-export.html` to **ahilden@ca.ibm.com** and **jmquille@us.ibm.com** with subject:

```
Db2 Serverless Workshop — Lab 1 Session Export [your name]
```

> 💡 Include any observations in the email body — what worked well, what was confusing, what you'd like to see.

## 🚀 Next Steps

→ Move on to **Lab 2: Advanced Bob Workflows**

## 📚 Resources

- **Bob Installation & MCP Setup:** `resources/installation.md`
- **Bob Documentation:** https://ibm.biz/bob-doc
- **Cheat Sheet:** `resources/cheat-sheet.md`
- **Troubleshooting:** `resources/troubleshooting.md`

---

**Need Help?** Ask Andrew (ahilden@ca.ibm.com) or Jillian (jmquille@us.ibm.com)
