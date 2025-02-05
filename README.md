<h1>🔍 Web Application Library Version Checker</h1>

<h2>📌 Overview</h2>

<p>This project includes a bot that automatically checks for new versions of web application libraries every 12 hours. Additionally, it provides a JavaScript snippet that can be pasted into the browser console to detect and display the currently used versions of specified components alongside their latest available versions.</p>

<p>A Python script is also included, which retrieves the JavaScript snippet (script.txt) from this repository and copies it to the clipboard, allowing to easily paste it into their browser console.</p>

<h2>🚀 Features</h2>

<ul>
  <li><b>Automated Version Checking:</b> The bot runs every 12 hours to detect new library versions.</li>
  <li><b>JavaScript Snippet:</b> Extracts the current versions of specified web application components and displays them in a structured table.</li>
  <li><b>Clipboard Helper:</b> A Python script fetches the latest JavaScript snippet and copies it to the clipboard for quick usage.</li>
  <li><b>Simple Setup:</b> Easily integrate the Python script into your system for convenient access.</li>
</ul>

<h2>🛠️ Installation & Setup</h2>

<h3>1️⃣ Download & Place the Script</h3>

<p>Download <code>components_to_clipboard.py</code> and place it in a preferred folder where you keep scripts.</p>

<h3>2️⃣ Add Script Folder to System PATH (Windows)</h3>

<p>To run the script from anywhere, add its directory to the system PATH.</p>

<h4>🔹 Open System Properties</h4>
<ul>
  <li>Press <kbd>Win</kbd> + <kbd>R</kbd>, type <code>sysdm.cpl</code>, and press <kbd>Enter</kbd>.</li>
</ul>

<h4>🔹 Navigate to Environment Variables</h4>
<ul>
  <li>Click the <b>Advanced</b> tab.</li>
  <li>Select <b>Environment Variables</b>.</li>
  <li>Under <b>System variables</b>, find and edit the <b>Path</b> variable.</li>
  <li>Click <b>New</b> and add the full path to the folder containing the script (e.g., <code>C:\Users\admin\scripts\</code>).</li>
  <li>Click <b>OK</b> to save.</li>
</ul>

<h3>3️⃣ Create a Batch Alias (Optional for Windows Users)</h3>

<p>For easier execution, create a batch file alias.</p>

<h4>✍️ Create a New Batch File</h4>

<p>1.Open a text editor and paste the following:</p>

<pre>@echo off
python "C:\Users\admin\scripts\components_to_clipboard.py" %*</pre>

<h2>4️⃣ Run the Script</h2>
<p>To fetch and copy the latest JavaScript snippet to the clipboard, simply run:</p>
<pre>cwkv</pre>
<p>If everything is set up correctly, you can now paste the snippet into your browser console.</p>

<h2>✅ You're all set! 🎉</h2>

<h3>🖥️ Usage</h3>
<ul>
    <li>Run the script (<code>cwkv</code> or <code>python components_to_clipboard.py</code>).</li>
    <li>Paste the copied JavaScript snippet into the browser console.</li>
    <li>View a table displaying the detected component versions alongside the latest available versions.</li>
</ul>

<h3>🤝 Contributing</h3>
<p>Feel free to open issues or suggest more libraries to be checked to improve this tool!</p>

<h3>📜 License</h3>
<p>This project is licensed under the MIT License.</p>

<h2>🚀 Happy Vulnerable Versions Checking!</h2>
