# Installing Bob

Bob is a standalone desktop application. Setup takes about 5 minutes.

**Download page:** https://bob.ibm.com/download

---

## Step 1: Download the Installer

Choose the correct installer for your operating system.

### macOS

First, determine your Mac's chip type:
1. Click the **Apple logo** (top-left) → **About This Mac**
2. Check the **Chip** field:
   - **Apple M1, M2, M3, etc.** → download the **mac-ARM** installer
   - **Intel** → download the **mac-intel** installer

**Using `.pkg` (recommended):**
1. Download the `.pkg` file from https://bob.ibm.com/download
2. Open the downloaded `.pkg` file
3. Follow the steps in the installation wizard

**Using `.dmg`:**
1. Download the `.dmg` file from https://bob.ibm.com/download
2. Open the downloaded `.dmg` file
3. Drag the Bob application to your **Applications** folder

---

### Windows

1. Download the `.exe` installer from https://bob.ibm.com/download
2. Run the downloaded `.exe` installer
3. Follow the installation wizard prompts
4. Accept the default installation directory (recommended)
5. Click **Finish** to complete the installation

---

### Linux

**Debian / Ubuntu:**
1. Download the `.deb` file from https://bob.ibm.com/download
2. Install it:
   ```bash
   sudo apt install ./IBM-Bob-linux-amd64-<version>.deb
   ```

**Red Hat / Fedora:**
1. Download the `.rpm` file from https://bob.ibm.com/download
2. Install it:
   ```bash
   sudo dnf install ./IBM-Bob-linux-x64-<version>.rpm
   ```

---

## Step 2: Install the IBM Data Server Client 12.1.5

> ⚠️ **Required for this lab.** The sample application connects to Db2 Serverless using the IBM Data Server Client 12.1.5. You must install it before running the sample app.

**Download from Fix Central:**
[IBM Data Server Client Packages v12.1.5](https://www-945.ibm.com/support/fixcentral/swg/selectFixes?parent=ibm~Information%2BManagement&product=ibm/Information+Management/IBM+Data+Server+Client+Packages&release=12.1&platform=All&function=fixId&fixids=*FP000*&includeSupersedes=0&source=fc)

### macOS / Linux

1. Download the v12.1.5 package for your platform from the Fix Central link above
2. Extract the archive and run the installer:
   ```bash
   ./db2_install
   ```
3. Select **CLIENT** as the install type and accept the licence
4. After installation, source the DB2 profile to make the libraries available:
   ```bash
   source ~/sqllib/db2profile
   ```
   Add this line to your shell profile (`.zshrc`, `.bashrc`, etc.) so it persists across sessions

### Windows

1. Download the v12.1.5 Windows package from the Fix Central link above
2. Run the installer and select **IBM Data Server Client** as the installation type
3. Follow the wizard to completion
4. Open a **new** Command Prompt or PowerShell window after installation so the updated `PATH` takes effect

---

## Step 3: Create an IBMid (if you don't have one)

An IBMid is required to use both Bob and the Db2 Serverless workshop environment. Andrew or Jillian will grant access to your IBMid — they cannot create one for you.

**Sign up at:** https://login.ibm.com

1. Go to https://login.ibm.com
2. Click **Create an IBMid**
3. Enter your email address and follow the registration steps
4. Verify your email when prompted
5. Once registration is complete, **send your IBMid email address to Andrew** (ahilden@ca.ibm.com) **or Jillian** (jmquille@us.ibm.com) so they can grant you access to the workshop environment

> ⚠️ **Do this before the workshop.** Access provisioning may take a little time — don't leave it until the day.


> 💡 **Already have an IBMid?** Just send your IBMid email address to Andrew (ahilden@ca.ibm.com) or Jillian (jmquille@us.ibm.com) so they can grant you workshop access.


---

## Step 4: Sign In to Bob with Your IBMid

1. Open Bob from your Applications menu or desktop shortcut
2. Sign in with your IBMid when prompted
3. Follow the authentication flow in your browser
4. Return to Bob after completing authentication

> 💡 **Network / firewall issues?** See the [Bob firewall configuration guide](https://ibm.biz/bob-doc) if outbound traffic is blocked in your environment.

---

## Step 5: Get Your Db2 Serverless API Key

The Db2 Serverless MCP server gives Bob direct access to your Db2 Serverless environment — provisioning projects, creating branches, running SQL, and retrieving connection information, all from the Bob chat panel.

Before configuring the MCP server in Bob, you need to generate a personal API key from the Db2 Serverless portal.

### Generate an API key

1. Go to **https://beta.db2.ibm.com** and sign in with your IBMid
   - If you don't have an IBMid, see **Step 3** above to create one first
2. In the left navigation menu, click **Home**
3. Select **API Keys**
4. Click the **Create API Key** button
5. Enter a **name** (e.g. `idug-emea-workshop`), a **description**, and an **expiry date**
6. Click **Create** and then **copy the resulting API key** — you will not be able to see it again

> ⚠️ **Save your API key now.** Once you close the dialog it cannot be retrieved. Paste it into a text file temporarily if needed.

---

## Step 6: Configure the Db2 Serverless MCP Server

### Configure the MCP server

1. Open Bob
2. Click the **Settings** icon in the Bob panel
3. Select the **MCP** tab
4. Click **Edit Global MCP** — this opens `~/.bob/mcp.json`
5. Add the following, replacing `YOUR_API_KEY_HERE` with the key you copied in Step 5:

```json
{
  "mcpServers": {
    "db2-serverless": {
      "type": "streamable-http",
      "url": "https://beta-mcp.db2.ibm.com/mcp",
      "headers": {
        "X-API-Key": "YOUR_API_KEY_HERE"
      },
      "disabled": false,
      "alwaysAllow": []
    }
  }
}
```

6. Save the file
7. Go to **Settings → MCP** and confirm **db2-serverless** shows as connected with no errors

> 💡 The `alwaysAllow` list can be used to pre-approve specific tools so Bob uses them without prompting during the labs. Leave it empty for now — Bob will ask for confirmation the first time each tool is called.

---

## Step 7: Verify Bob and the MCP Server are Working

Open a folder in Bob and try these two checks (File -> Open Folder (or New Folder)):

> 💡 Bob will open the folder in Restricted Mode.  Click on `Manage` in the top message at the top of the window and click "In a Trusted Folder"


**Check 1 — Bob basics:**
```
List all files in the current directory.
```

**Check 2 — MCP server:**

```
Use the db2-serverless MCP server to list my available Db2 Serverless projects.
```

If both respond correctly, you are ready for the workshop.

---

## Quick Reference — Bob Interface

| Feature | How to Access |
|---|---|
| **Mode selector** (Ask / Plan / Agent) | Bottom-left of the Bob chat panel |
| **New conversation** | `+` icon in the Bob panel header |
| **MCP Servers** | Bob menu → MCP Servers |
| **Marketplace** | Bob menu → Marketplace |
| **Settings** | Bob menu → Settings |
| **Check for updates** | IBM Bob menu → Check for Updates... |

---

## Troubleshooting

### macOS — security warning on first open
Go to **System Settings → Privacy & Security** → scroll down → click **Open Anyway** next to the Bob entry.

### Windows — SmartScreen warning
Click **More info** → **Run anyway**.

### Wrong version installed (slow performance)
Download the correct version for your hardware (Intel vs ARM on macOS) from https://bob.ibm.com/download, uninstall the current version, and reinstall.

### Authentication not completing
- Make sure your browser is not blocking popups from Bob
- Try signing out and back in: Bob menu → account icon → Sign Out → Sign In again

### Bob opens but shows no response
- Check your internet connection
- Verify you are fully authenticated (look for your account name in Bob settings)

---

