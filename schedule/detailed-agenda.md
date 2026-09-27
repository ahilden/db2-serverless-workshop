# IDUG EMEA Workshop — Detailed Agenda
## Db2 Serverless with Bob

**Event:** IDUG EMEA Conference  
**Facilitators:** Andrew Hilden — ahilden@ca.ibm.com | Jillian Quiller, Db2 Serverless Product Manager — jmquille@us.ibm.com
**Format:** In-person, facilitated  
**Duration:** 4 hours  
**Date:** September 27, 2026
**Timezone:** Europe/Amsterdam  

---

## Agenda Overview

| Time | Session | Duration | Lab |
|---|---|---|---|
| 09:00 | Introduction & Setup | 20 min | — |
| 09:20 | Core Bob Features | 75 min | Lab 1 (25 min) |
| 10:35 | ☕ Break | 10 min | — |
| 10:45 | Advanced Features & Differentiators | 50 min | Lab 2 (25 min) |
| 11:35 | Db2 Serverless Use Case Labs | 75 min | Lab 3 (60 min) |
| 12:50 | Wrap-up & Next Steps | 10 min | — |
| **13:00** | **End** | | |

---

## Session Details

### 09:00 — Introduction & Setup _(20 minutes)_

**Facilitators:** Andrew Hilden & Jillian Quiller

**Topics:**
- Welcome and introductions
- Workshop objectives and agenda walkthrough
- What is Bob? — AI coding assistant overview
- Bob and databases: where the value is for DBAs
- Environment setup verification
  - Bob running (standalone desktop app — https://bob.ibm.com/download)
  - Db2 Serverless endpoint URL distributed (IBMid used for access — no separate API key)
- Opening Q&A

**Deliverables:**
- ✅ All attendees have Bob running and authenticated with IBMid
- ✅ Db2 Serverless endpoint URL distributed and connectivity verified

---

### 09:20 — Core Bob Features _(75 minutes, includes Lab 1)_

**Topics:**
- Bob modes: Ask, Plan, Agent — and when to use each
- Reading and navigating a codebase with Bob
- Writing and editing files with `apply_diff` (surgical vs. full rewrite)
- Executing commands through Bob (`execute_command`) — no terminal switching
- Bob Findings — automated security and quality analysis
- Literate coding — asking Bob to explain unfamiliar code
- Auto-approval for trusted read operations
- Prompting best practices for database developers

**🔬 Lab 1: Core Bob Operations — Db2 Serverless Context**  
⏱️ 25 minutes | Beginner | [`labs/lab1-basic-operations/instructions.md`](../labs/lab1-basic-operations/instructions.md)

Key objectives:
- Navigate and read a Db2-connected Python project
- Update Db2 Serverless connection config using `apply_diff`
- Execute a SQL query through Bob's terminal integration
- Use Bob Findings to identify a SQL injection risk
- Practice Ask, Plan, Agent mode switching

**Deliverables:**
- ✅ Comfortable with Bob modes and core tools in VS Code
- ✅ Completed Lab 1 exercises

---

### 10:35 — ☕ Break _(10 minutes)_

---

### 10:45 — Advanced Bob Features & Differentiators _(50 minutes, includes Lab 2)_

**Topics:**
- Agentic workflows — Bob executes multi-step tasks autonomously
- Sub-tasks — delegate large pieces of work to focused child tasks
- Sub-agents — parallel workers for simultaneous research
- Mode switching mid-conversation (Ask → Plan → Agent)
- Pre-built Workflows: code review, PR creation, documentation generation
- MCP server integration — extending Bob with custom tools via VS Code
- Bob Marketplace — discover and install modes, skills, MCP servers
- Db2 Serverless MCP server — available now

**🔬 Lab 2: Advanced Workflows — Building a Db2-Connected App**  
⏱️ 25 minutes | Intermediate | [`labs/lab2-advanced-workflows/instructions.md`](../labs/lab2-advanced-workflows/instructions.md)

Key objectives:
- Scaffold a full inventory management application with one agentic prompt
- Use a sub-task to build a reporting module cleanly
- Practice mode switching mid-implementation
- Run a pre-built code review workflow

**Deliverables:**
- ✅ Understanding of Bob's agentic and extensibility differentiators
- ✅ Completed Lab 2 exercises

---

### 11:35 — Db2 Serverless Use Case Labs _(75 minutes, includes Lab 3)_

**Topics covered across the three use case paths:**
- Use Case 1: REST API app using Db2 Serverless RunSQL endpoint
- Use Case 2: Native Java app using the Db2 JCC JDBC driver
- Use Case 3: Full database workflow — schema creation, branching, evolution (MCP/REST)

> Attendees choose their path. Most will complete Use Cases 1 and 2 in sequence.
> Use Case 3 is a facilitator-led walkthrough if the MCP/REST spec is not yet finalized.

**🔬 Lab 3: Db2 Serverless Use Case Labs**  
⏱️ 60 minutes | Advanced | [`labs/lab3-client-specific/instructions.md`](../labs/lab3-client-specific/instructions.md)

**Use Case 1 — REST API App with Db2 Serverless RunSQL** _(~25 min)_
- Build a Python expense tracker using the Db2 Serverless REST RunSQL endpoint
- Bob scaffolds the full app, creates the schema, and runs security analysis
- No JDBC driver needed — just HTTP + API key

**Use Case 2 — Native Java App with Db2 JCC Driver** _(~25 min)_
- Build a Java product catalog app using `db2jcc4.jar`
- Bob generates JDBC boilerplate: SSL config, PreparedStatements, try-with-resources
- Maven project scaffolded in VS Code from a single prompt

**Use Case 3 — Db2 Serverless Database Workflow** _(~25 min or demo)_
- Provision a Db2 Serverless instance, create a schema, branch for safe evolution
- Db2 Serverless MCP server is available — hands-on workflow
- ⚠️ REST API RunSQL spec not yet finalized — Use Case 1 is reserved for a future workshop

**Deliverables:**
- ✅ Working application code for at least one Db2 Serverless scenario
- ✅ Understanding of how Bob accelerates Db2 application development

---

### 12:50 — Wrap-up & Next Steps _(10 minutes)_

**Topics:**
- Key takeaways from the workshop
- Resource links and where to get Bob
- How to install the Db2 Serverless MCP server (when available)
- Open Q&A and discussion

**Deliverables:**
- ✅ Action plan for using Db2 Serverless more effectively with Bob
- ✅ Resource links distributed

---

## Lab Reference

| Lab | File | Duration | Difficulty |
|---|---|---|---|
| Lab 1: Core Bob Operations | [`labs/lab1-basic-operations/instructions.md`](../labs/lab1-basic-operations/instructions.md) | 25 min | Beginner |
| Lab 2: Advanced Workflows | [`labs/lab2-advanced-workflows/instructions.md`](../labs/lab2-advanced-workflows/instructions.md) | 25 min | Intermediate |
| Lab 3: Db2 Serverless Use Cases | [`labs/lab3-client-specific/instructions.md`](../labs/lab3-client-specific/instructions.md) | 60 min | Advanced |

---

## Facilitator Notes

- **Audience:** Experienced Db2 DBAs and database engineers. Strong SQL and schema knowledge, less application development experience. Keep app scaffolding explanations concise — focus on the value Bob and Db2 Serverless delivers, not the code mechanics.
- **Key differentiator to emphasize:** Bob and Db2 Serverless bridge deep DB expertise and application development. DBAs bring the prompts, Db2 Serverless provides the database; Bob generates the boilerplate. Working applications in minutes, not hours.
- **Lab 3 Use Case 3:** If the Db2 Serverless MCP/REST spec is not yet available, run Use Case 3 as a conceptual walkthrough to show the *vision* rather than hands-on steps.
- **Setup tip:** Pre-provision Db2 Serverless instances for attendees if possible — reduces setup friction during the Introduction segment.

---

## Contact

**Andrew Hilden**
IBM Canada
ahilden@ca.ibm.com

**Jillian Quiller, Db2 Serverless Product Manager**
IBM US
jmquille@us.ibm.com
