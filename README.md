# Setup Instructions

This fetch & update script runs 24/7 by a bot. You just need to download `components_to_clipboard.py` and follow the steps below.

## Setting Up `components_to_clipboard.py` as `cwkv` Alias on Windows

### 1. Move or Locate the Script
Place `components_to_clipboard.py` in a folder where you want to keep your scripts.

### 2. Add the Directory to System PATH

#### 2.1 Open System Properties
Press `Win + R`, type `sysdm.cpl`, and hit Enter.

![System Properties](https://github.com/user-attachments/assets/d4d568c3-f0d1-45e2-ab66-10ae403f0ead)

#### 2.2 Navigate to the Advanced tab and click **Environment Variables**

![Environment Variables](https://github.com/user-attachments/assets/77913ff1-a156-4c2f-a3e6-422353f8b4e1)

#### 2.3 Edit the Path Variable
Under **System variables**, find and select **Path**, then click **Edit**.

![Path Variable](https://github.com/user-attachments/assets/0d196c25-1893-4278-afa7-cb95258b9c1d)

#### 2.4 Add Your Script's Folder Path
Click **New** and add the full path to your folder (e.g., `C:\Users\YourUsername\Scripts\`).

![Add Path](https://github.com/user-attachments/assets/b9cae7af-411b-44ca-b27c-18fc8d999932)

#### 2.5 Save Changes
Click **OK** to save and exit.

---

### 3. Create a Batch File (Alias `cwkv`)

#### 3.1 Create a New Batch File
Open a text editor and paste the following:

```batch
@echo off
python "<PATH_TO_SCRIPT>" %*
```

#### 3.2 Save the File
Save the file as `cwkv.bat` in the same folder as your script.

![Save Batch File](https://github.com/user-attachments/assets/8c91058c-0ae4-428c-b8cb-f8b039cb3cdb)

#### 3.3 Test the Command
Open a new command prompt and type:

```sh
cwkv
```

![Command Prompt Test](https://github.com/user-attachments/assets/d1cdddbc-46e6-4e74-afa3-312e1fffd9d0)

✅ If the script runs, the setup is complete!
