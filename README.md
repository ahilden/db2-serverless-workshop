# Db2 Serverless with Bob — IDUG EMEA Workshop

Welcome to the **Db2 Serverless with Bob** hands-on workshop at IDUG EMEA.

This workshop shows Db2 professionals how Db2 Serverless and Bob — IBM's AI coding assistant for VS Code —
can dramatically accelerate Db2 application development and usage: from scaffolding Python and Java JDBC
applications, to driving database workflows directly from your IDE.

---

## Your Facilitators

**Andrew Hilden, Chief Architect Db2 SaaS**
IBM Canada
📧 ahilden@ca.ibm.com

**Jillian Quiller, Db2 Serverless Product Manager**
IBM US
📧 jmquille@us.ibm.com

Questions before, during, or after the workshop? Reach out directly to either of them!

---

> ## ⚠️ Pre-GA Experience — Please Read
>
> **Db2 Serverless is a pre-GA (pre-General Availability) product.** What you are using today is an early access environment, not a production-hardened service. You may encounter rough edges, missing features, or unexpected behaviour.
>
> **Why are you here?** A primary goal of this workshop is to gather early user experience feedback from Db2 professionals like you. Your observations — what works well, what is confusing, what is missing — will directly shape the product before it reaches general availability. Please share feedback freely with Andrew and Jillian during and after the exercises.
>
> **Known limitations in this environment:**
> - Some management and monitoring features are not yet available
> - The Db2 Serverless REST API RunSQL endpoint specification is not yet finalized (Use Case 1 in Lab 3 is a preview for a future workshop)
> - Performance and availability SLAs do not apply to this environment
>
> If you hit a problem, ask Andrew (ahilden@ca.ibm.com) or Jillian (jmquille@us.ibm.com)
>
> **📤 Session export:** At the end of each lab you'll be asked to export your Bob chat history as HTML and email it to the facilitators. Bob generates the export for you — it takes about 2 minutes and is the most valuable feedback you can give.

---

## What You'll Build

In 4 hours you will:

1. **Lab 1** — Navigate a Db2-connected codebase, edit configuration, execute SQL, and spot security issues using Bob Findings — all inside VS Code
2. **Lab 2** — Scaffold a complete Db2 inventory application using a single agentic prompt, delegate work via sub-tasks, and run a pre-built code review workflow
3. **Lab 3** — Choose your path:
   - Build a **Java app** using the **Db2 JCC JDBC driver**
   - Drive a complete **database management workflow** — branching, users, scaling, and autoscaling — via the Db2 Serverless MCP server
   - _(Use Case 1: Python REST API app — coming in a future workshop once the RunSQL spec is finalized)_

---

## Getting Started

### 1. Create an IBMid (if you don't have one)

Both Bob and the Db2 Serverless workshop environment require an **IBMid**.

1. Go to **https://login.ibm.com** → click **Create an IBMid**
2. Register with your email address and verify it
3. **Email your IBMid address to Andrew or Jillian** — ahilden@ca.ibm.com or jmquille@us.ibm.com — and they will grant you access to the workshop environment


### 2. Install Bob

Bob is a **standalone desktop application** — download it at **https://bob.ibm.com/download**

See [`resources/installation.md`](resources/installation.md) for step-by-step instructions for macOS (Intel and ARM), Windows, and Linux.

### 3. Db2 Serverless Access

Db2 Serverless is available at **https://beta.db2.ibm.com**. These labs focus on using Bob with Db2 Serverless through the **Db2 Serverless MCP server** — you will interact with your database entirely through Bob rather than the web console.

No IBM Cloud account needed. Once the facilitators have your IBMid they will provide your access. You will also need to generate a personal API key from https://beta.db2.ibm.com — see [`resources/installation.md`](resources/installation.md) Step 5 for instructions.

> ⚠️ **Note:** Db2 Serverless is currently pre-release. You will be using a beta environment rather than the production service. Andrew and Jillian will assist with any environment issues during the session.

### 4. Java Setup (optional — for Use Case 2)

If you plan to work through the JCC JDBC lab:
- Java 11+ installed
- Maven installed
- `db2jcc4.jar` downloaded from IBM (or provided on the day)

---

## Workshop Agenda

| Time | Session | Lab |
|---|---|---|
| 09:00 | Introduction & Setup | — |
| 09:20 | Core Bob Features | Lab 1 (25 min) |
| 10:35 | ☕ Break | — |
| 10:45 | Advanced Features & Differentiators | Lab 2 (25 min) |
| 11:35 | Db2 Serverless Use Case Labs | Lab 3 (60 min) |
| 12:50 | Wrap-up & Next Steps | — |
| 13:00 | End | |

📋 Full agenda with session details: [`schedule/detailed-agenda.md`](schedule/detailed-agenda.md)

---

## Lab Materials

| Lab | Instructions | Duration | Difficulty |
|---|---|---|---|
| Lab 1: Core Bob Operations | [`labs/lab1-basic-operations/instructions.md`](labs/lab1-basic-operations/instructions.md) | 25 min | Beginner |
| Lab 2: Advanced Workflows | [`labs/lab2-advanced-workflows/instructions.md`](labs/lab2-advanced-workflows/instructions.md) | 25 min | Intermediate |
| Lab 3: Db2 Serverless Use Cases | [`labs/lab3-client-specific/instructions.md`](labs/lab3-client-specific/instructions.md) | 60 min | Advanced |

---

## Resources

| Resource | Link |
|---|---|
| Bob Installation (VS Code) | [`resources/installation.md`](resources/installation.md) |
| Bob Cheat Sheet | [`resources/cheat-sheet.md`](resources/cheat-sheet.md) |
| Troubleshooting | [`resources/troubleshooting.md`](resources/troubleshooting.md) |
| Bob Documentation | https://ibm.biz/bob-doc |
| Db2 Serverless Docs | https://cloud.ibm.com/docs/Db2onCloud |

---

## A Note on Lab 3 Use Case 1

The **Db2 Serverless MCP server** (Use Case 3) is available now — branch, users, disk, and autoscaling management all work directly from Bob. Use Case 3 is fully hands-on.

**Use Case 1** (Python REST API app using the RunSQL endpoint) is reserved for a future workshop — the REST API RunSQL specification is not yet finalized. It is labelled as a future use case in the lab instructions.

Contact Andrew (ahilden@ca.ibm.com) or Jillian (jmquille@us.ibm.com) with any questions.

---

## Get Bob

See [`resources/installation.md`](resources/installation.md) to get started.

---

*Db2 Serverless with Bob · IDUG EMEA*
