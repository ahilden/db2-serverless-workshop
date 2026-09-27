# Bob Quick Reference Guide

A quick reference for common Bob operations and best practices.

## 🔧 Core Tools

### File Operations

#### read_file
Read one or more files, optionally with line ranges.

```text
"Read src/app.py"
```

**Multiple files with line ranges:**
```text
"Read src/app.py and src/utils.py lines 1-50 and 100-150"
```

**When to use:**
- Understanding code structure
- Before making changes
- Reviewing multiple related files
- Analyzing specific sections

---

#### list_files
List files and directories.

```text
"List all files in src/ recursively"
```

**When to use:**
- Exploring project structure
- Finding files
- Understanding organization

---

#### grep
Fast content search using regex patterns.

```text
"Search for TODO and FIXME comments in all Python files under src/"
```

**When to use:**
- Finding specific code patterns
- Locating function calls
- Discovering TODOs
- Finding all usages across the project

> **Note:** In older documentation you may see `search_files` — `grep` is the current equivalent.

---

#### glob
Fast file pattern matching (find files by name).

```text
"Find all TypeScript files under src/"
```

**When to use:**
- Find all files matching a name pattern
- Locate test files, config files, etc.

---

### Code Analysis

#### GetSymbolsOverview
Get a high-level overview of symbols (classes, functions, etc.) in a file.

```text
"Give me an overview of the symbols in src/services/payment.py"
```

**When to use:**
- Understanding a file's structure quickly
- Finding which class or function to read next

> **Note:** Replaces the older `list_code_definition_names` tool.

---

### Code Editing

#### apply_diff
Make precise changes to files (PREFERRED for edits).

```text
"In src/utils.py starting at line 10, replace the old_function() body so it returns 'new' and add a docstring"
```

**When to use:**
- Targeted code changes
- Refactoring
- Bug fixes
- Most editing scenarios

---

#### write_file
Write complete file content (creates or overwrites).

```text
"Create a new file config.json with these contents: ..."
```

**When to use:**
- Creating new files from scratch
- Complete rewrites of small files

---

### Command Execution

#### execute_command
Run CLI commands.

```text
"Run npm test"
```

**When to use:**
- Running tests
- Building projects
- Installing dependencies
- Git operations

---

### Task Management

#### update_todo_list
Track multi-step tasks.

```text
"Update the todo list: mark 'Add email validation' as complete and 'Write tests' as in progress"
```

**Todo status format:**
```markdown
[x] Completed task
[-] In progress task
[ ] Pending task
```

**When to use:**
- Complex multi-step tasks
- Tracking progress
- Planning work

---

### Agentic Capabilities (Bob v2)

#### start_subtask
Spawn an isolated child task with its own context, instructions, and todo list.

```text
"Start a sub-task to implement the authentication module and report back with a summary."
```

**When to use:**
- Delegating a large, self-contained piece of work
- Keeping the main conversation clean during multi-phase work
- Running a child task in a different mode (e.g., IBM i Developer)

**Example flow:**
```text
Sub-task: "Set up JWT authentication"
→ Child task handles full implementation
→ Returns summary to parent when complete
→ Parent continues with next phase
```

---

#### spawn_subagent
Launch an independent parallel worker for focused side tasks.

```text
"Spawn a sub-agent to explore the src/services directory and report back what services exist."
```

**When to use:**
- Research or exploration that shouldn't bloat the main context
- Running multiple investigations simultaneously (parallel execution)
- Short, self-contained tasks where only the result is needed

**Parallel example:**
```text
Sub-agent 1: Explore the database schema
Sub-agent 2: Check the API documentation
Main agent:  Continues planning while both sub-agents work
```

---

#### switch_mode
Switch Bob to a different mode mid-conversation to access specialized capabilities.

```text
"Switch to Plan mode so we can design the architecture before coding."
```

**Available modes:**
| Mode | Best For |
|------|----------|
| Agent | Implementation, refactoring, agentic tasks |
| Ask | Questions, explanations, analysis (read-only) |
| Plan | Architecture, task breakdown, strategy |
| IBM i Developer | RPG, CL, Db2 for i development |
| IBM i Database | Db2 for i SQL analysis |
| Z Code | COBOL, PL/I, JCL development |
| Custom | Your organization's specialized workflows |

---

#### start_workflow
Start a pre-defined curated workflow for a common task.

```text
"Start the Create Pull Request workflow."
```

**Available workflows:**
- **Create Pull Request** — Generate PR description from git diff
- **Code Review** — Open review panel for branch comparison
- **Business Rules Extraction** — Extract rules from IBM i source code
- **Generate Documentation** — Full-program docs for COBOL/PL/I/HLASM
- **Refactor COBOL or PL/I** — Extract services from legacy programs

---

### Bob Marketplace

Discover, install, and manage community-created assets (modes, skills, rules, MCP servers).

**Search for assets:**
```text
"Search the Bob Marketplace for a skill that helps with Terraform."
```

**Install an asset:**
```text
"Install the 'iac-review' skill from the marketplace."
```

**List installed assets:**
```text
"Show me what's installed in my workspace."
```

**Check for updates:**
```text
"Are there any updates available for my installed marketplace assets?"
```

---

## 💡 Best Practices

### Prompting Tips

**Be Specific:**
```text
❌ "Fix the bug"
✅ "Fix the null pointer exception in getUserData() on line 45 of src/user.py"
```

**Provide Context:**
```text
❌ "Add a function"
✅ "Add a validateEmail() function to src/utils.py that checks email format using regex"
```

**Break Down Complex Tasks:**
```text
❌ "Refactor the entire application"
✅ "Refactor the user authentication module: 1) Extract validation logic, 2) Add error handling, 3) Update tests"
```

**Use Examples:**
```text
❌ "Make it better"
✅ "Refactor this function to use list comprehension like we do in other utility functions"
```

---

### Workflow Patterns

#### Pattern 1: Read → Understand → Modify
```text
1. Read the file(s)
2. Ask Bob to explain if needed
3. Make targeted changes
4. Verify with tests
```

#### Pattern 2: Search → Read → Update All
```text
1. Search for all usages
2. Read affected files
3. Update all occurrences
4. Run tests
```

#### Pattern 3: Plan → Execute → Verify
```text
1. Create todo list
2. Execute step by step
3. Test after each step
4. Update todo list
```

---

### Tool Selection Guide

| Task | Recommended Tool | Alternative |
|------|-----------------|-------------|
| View file content | `read_file` | - |
| Find files | `glob` | `list_files` |
| Search code | `grep` | `read_file` + manual search |
| Understand file structure | `GetSymbolsOverview` | `read_file` |
| Edit existing code | `apply_diff` | `search_and_replace` |
| Create new file | `write_file` | - |
| Add new lines | `insert_content` | `apply_diff` |
| Run tests | `execute_command` | - |
| Track progress | `update_todo_list` | Manual notes |
| Delegate large sub-work | `start_subtask` | - |
| Parallel exploration | `spawn_subagent` | - |
| Change AI mode | `switch_mode` | - |
| Run standard workflow | `start_workflow` | - |

---

## 🎯 Common Scenarios

### Scenario: Rename a Function

```text
Step 1: Find all usages
"Search for all files that use the function getUserData"

Step 2: Read affected files
"Read these files: [list from search results]"

Step 3: Update all occurrences
"Rename getUserData to fetchUserProfile in all these files"

Step 4: Verify
"Run the test suite to verify everything works"
```

---

### Scenario: Add a New Feature

```text
Step 1: Plan
"Create a todo list for adding email validation to the User model"

Step 2: Understand existing code
"Read src/models/user.py and show me the current validation logic"

Step 3: Implement
"Add email validation following the existing pattern"

Step 4: Test
"Create tests for email validation in tests/test_user.py"

Step 5: Document
"Update the User model docstring to document email validation"
```

---

### Scenario: Debug an Issue

```text
Step 1: Reproduce
"Run the failing test: pytest tests/test_checkout.py::test_payment"

Step 2: Analyze
"Read the test file and the checkout module to understand the flow"

Step 3: Locate issue
"Search for error handling in the payment processing code"

Step 4: Fix
"Update the payment timeout handling in src/payment.py"

Step 5: Verify
"Run all payment-related tests to ensure the fix works"
```

---

### Scenario: Refactor Code

```text
Step 1: Analyze
"Read src/services/report_generator.py and identify areas for improvement"

Step 2: Plan
"Create a refactoring plan focusing on readability and maintainability"

Step 3: Refactor incrementally
"Extract the data processing logic into separate functions"

Step 4: Test continuously
"Run tests after each refactoring step"

Step 5: Document
"Add docstrings to the new functions"
```

---

## ⚡ Quick Commands

### File Operations
```text
"Read src/app.py"
"List all Python files in src/"
"Search for TODO comments in the codebase"
```

### Code Changes
```text
"Change the timeout value to 30 in config.py"
"Add a helper function to format dates in utils.py"
"Refactor the calculate_total function to be more readable"
```

### Testing
```text
"Run the test suite"
"Run tests for the user module"
"Run tests with coverage report"
```

### Analysis
```text
"Explain how the authentication flow works"
"Find all places where getUserData is called"
"Review this code for potential issues"
```

---

## 🚫 Common Mistakes

### Mistake 1: Not Reading Before Editing
```text
❌ "Update the config file"
✅ "Read config.json, then update the timeout value to 30"
```

### Mistake 2: Vague Requests
```text
❌ "Fix the code"
✅ "Fix the IndexError on line 42 of src/parser.py by adding bounds checking"
```

### Mistake 3: Too Many Changes at Once
```text
❌ "Refactor everything and add new features"
✅ "First refactor the user module, then we'll add the new features"
```

### Mistake 4: Not Verifying Changes
```text
❌ Make changes and move on
✅ "Make the changes, then run tests to verify"
```

### Mistake 5: Insufficient Context
```text
❌ "Add validation"
✅ "Add email validation to the User model following the same pattern as password validation"
```

---

## 📚 Advanced Tips

### Tip 1: Batch Related Changes
Instead of multiple requests, combine related changes:
```text
"In src/user.py:
1. Add email field to User class
2. Add email validation method
3. Update __init__ to accept email
4. Update __str__ to include email"
```

### Tip 2: Use Line Ranges for Large Files
```text
"Read src/app.py lines 1-50 for initialization and lines 200-250 for the main logic"
```

### Tip 3: Leverage Bob's Understanding
```text
"Review the authentication flow and suggest improvements for security"
```

### Tip 4: Ask for Explanations
```text
"Explain why this function might be causing performance issues"
```

### Tip 5: Get Multiple Options
```text
"Show me three different ways to implement this feature, with pros and cons"
```

---

## 🎓 Learning Resources

### Practice Exercises
1. Read and understand a new codebase
2. Refactor a complex function
3. Add a new feature with tests
4. Debug a failing test
5. Optimize slow code

### Next Steps
- Try Bob with your own code
- Experiment with different prompting styles
- Share learnings with your team
- Build your own workflow patterns

---

## 📞 Getting Help

### When Stuck
1. Ask Bob to explain the issue
2. Break the problem into smaller steps
3. Search for similar patterns in the codebase
4. Consult the facilitator or support channel

### Resources
- Full documentation: [Link]
- Support channel: [Link]
- Community forum: [Link]
- Video tutorials: [Link]

---

**Remember:** The more context you provide, the better Bob can help you!
