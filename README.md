<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Setup Instructions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin: auto;
        }
        h1, h2 {
            color: #333;
        }
        code {
            background: #eee;
            padding: 3px 6px;
            border-radius: 4px;
        }
        .steps {
            padding-left: 20px;
        }
        .steps img {
            display: block;
            max-width: 100%;
            height: auto;
            margin-top: 10px;
            border-radius: 5px;
        }
        .code-block {
            background: #333;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .code-block pre {
            margin: 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Setup Instructions</h1>
        <p>This fetch & update script runs 24/7 by a bot. You just need to download <code>components_to_clipboard.py</code> and follow the steps below.</p>
        
        <h2>Setting Up <code>components_to_clipboard.py</code> as <code>cwkv</code> Alias on Windows</h2>
        
        <h3>1. Move or Locate the Script</h3>
        <p>Place <code>components_to_clipboard.py</code> in a folder where you want to keep your scripts.</p>
        
        <h3>2. Add the Directory to System PATH</h3>
        <div class="steps">
            <p><strong>2.1</strong> Press <code>Win + R</code>, type <code>sysdm.cpl</code>, and hit Enter.</p>
            <img src="https://github.com/user-attachments/assets/d4d568c3-f0d1-45e2-ab66-10ae403f0ead" alt="System Properties">
            
            <p><strong>2.2</strong> Navigate to the <strong>Advanced</strong> tab and click <strong>Environment Variables</strong>.</p>
            <img src="https://github.com/user-attachments/assets/77913ff1-a156-4c2f-a3e6-422353f8b4e1" alt="Environment Variables">
            
            <p><strong>2.3</strong> Under System variables, find and select <strong>Path</strong>, then click <strong>Edit</strong>.</p>
            <img src="https://github.com/user-attachments/assets/0d196c25-1893-4278-afa7-cb95258b9c1d" alt="Path Variable">
            
            <p><strong>2.4</strong> Click <strong>New</strong> and add the full path to your folder (e.g., <code>C:\Users\YourUsername\Scripts\</code>).</p>
            <img src="https://github.com/user-attachments/assets/b9cae7af-411b-44ca-b27c-18fc8d999932" alt="Add Path">
            
            <p><strong>2.5</strong> Click <strong>OK</strong> to save and exit.</p>
        </div>
        
        <h3>3. Create a Batch File (Alias <code>cwkv</code>)</h3>
        <div class="steps">
            <p><strong>3.1</strong> Open a text editor and paste the following:</p>
            <div class="code-block">
                <pre>@echo off
python "<PATH_TO_SCRIPT>" %*</pre>
            </div>
            
            <p><strong>3.2</strong> Save the file as <code>cwkv.bat</code> in the same folder as your script.</p>
            <img src="https://github.com/user-attachments/assets/8c91058c-0ae4-428c-b8cb-f8b039cb3cdb" alt="Save Batch File">
            
            <p><strong>3.3</strong> Open a new command prompt and type:</p>
            <div class="code-block">
                <pre>cwkv</pre>
            </div>
            <img src="https://github.com/user-attachments/assets/d1cdddbc-46e6-4e74-afa3-312e1fffd9d0" alt="Command Prompt Test">
        </div>
        
        <p>If the script runs, the setup is complete! ✅</p>
    </div>
</body>
</html>
