<h1>🔍 Web Application Library Version Checker</h1>

📌 Overview

This project includes a bot that automatically checks for new versions of web application libraries every 12 hours. Additionally, it provides a JavaScript snippet that can be pasted into the browser console to detect and display the currently used versions of specified components alongside their latest available versions.

A Python script is also included, which retrieves the JavaScript snippet from a GitHub-hosted file and copies it to the clipboard, allowing users to easily paste it into their browser console.

🚀 Features

Automated Version Checking: The bot runs every 12 hours to detect new library versions.

JavaScript Snippet: Extracts the current versions of specified web application components and displays them in a structured table.

Clipboard Helper: A Python script fetches the latest JavaScript snippet and copies it to the clipboard for quick usage.

Simple Setup: Easily integrate the Python script into your system for convenient access.

🛠️ Installation & Setup

1️⃣ Download & Place the Script

Download components_to_clipboard.py and place it in a preferred folder where you keep scripts.

2️⃣ Add Script Folder to System PATH (Windows)

To run the script from anywhere, add its directory to the system PATH.

🔹 Open System Properties

Press Win + R, type sysdm.cpl, and press Enter.

🔹 Navigate to Environment Variables

Click the Advanced tab.

Select Environment Variables.

Under System variables, find and edit the Path variable.

Click New and add the full path to the folder containing the script (e.g., C:\Users\admin\scripts\).

Click OK to save.

3️⃣ Create a Batch Alias (Optional for Windows Users)

For easier execution, create a batch file alias.

✍️ Create a New Batch File

Open a text editor and paste the following:

@echo off
python "C:\Users\admin\scripts\components_to_clipboard.py" %*

Save the file as cwkv.bat in the same folder as your script.

4️⃣ Run the Script

To fetch and copy the latest JavaScript snippet to the clipboard, simply run:

cwkv

If everything is set up correctly, you can now paste the snippet into your browser console.

✅ You're all set! 🎉

🖥️ Usage

Run the script (cwkv or python components_to_clipboard.py).

Paste the copied JavaScript snippet into the browser console.

View a table displaying the detected component versions alongside the latest available versions.

🤝 Contributing

Feel free to open issues or suggest more libraries to be checked to improve this tool!



📜 License

This project is licensed under the MIT License.

🚀 Happy version checking!
