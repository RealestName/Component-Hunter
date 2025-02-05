<h1 align="center">🛠️ Setup Instructions</h1>

<p align="center">This fetch & update script runs 24/7 by a bot. You just need to download <code>components_to_clipboard.py</code> and follow the steps below.</p>

---

## 🚀 Setting Up <code>components_to_clipboard.py</code> as <code>cwkv</code> Alias on Windows

### 1️⃣ Move or Locate the Script
Place <code>components_to_clipboard.py</code> in a folder where you want to keep your scripts.

### 2️⃣ Add the Directory to System PATH

#### 🔹 Open System Properties
Press <kbd>Win</kbd> + <kbd>R</kbd>, type <code>sysdm.cpl</code>, and hit <kbd>Enter</kbd>.

<img src="https://github.com/user-attachments/assets/d4d568c3-f0d1-45e2-ab66-10ae403f0ead" alt="System Properties" width="500"/>

#### 🔹 Navigate to Advanced tab and Click **Environment Variables**

<img src="https://github.com/user-attachments/assets/77913ff1-a156-4c2f-a3e6-422353f8b4e1" alt="Environment Variables" width="500"/>

#### 🔹 Edit the Path Variable
Under **System variables**, find and select **Path**, then click **Edit**.

<img src="https://github.com/user-attachments/assets/0d196c25-1893-4278-afa7-cb95258b9c1d" alt="Path Variable" width="500"/>

#### 🔹 Add Your Script's Folder Path
Click **New** and add the full path to your folder (e.g., <code>C:\Users\YourUsername\Scripts\</code>).

<img src="https://github.com/user-attachments/assets/b9cae7af-411b-44ca-b27c-18fc8d999932" alt="Add Path" width="500"/>

#### 🔹 Save Changes
Click **OK** to save and exit.

---

### 3️⃣ Create a Batch File (Alias <code>cwkv</code>)

#### ✍️ Create a New Batch File
Open a text editor and paste the following:

```batch
@echo off
python "<PATH_TO_SCRIPT>" %*
```

#### 💾 Save the File
Save the file as <code>cwkv.bat</code> in the same folder as your script.

<img src="https://github.com/user-attachments/assets/8c91058c-0ae4-428c-b8cb-f8b039cb3cdb" alt="Save Batch File" width="500"/>

#### 🖥️ Test the Command
Open a new command prompt and type:

```sh
cwkv
```

<img src="https://github.com/user-attachments/assets/d1cdddbc-46e6-4e74-afa3-312e1fffd9d0" alt="Command Prompt Test" width="500"/>

✅ **If the script runs, the setup is complete!** 🎉
