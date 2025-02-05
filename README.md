# Instructions

This fetch & update script runs 24/7 by a bot. You, as a user, just need to download the components_to_clipboard.py to your local machine and....


Setting Up components_to_clipboard.py as cwkv alias command on Windows - 

Steps to Set Up

1. Move or Locate the Script

Place components_to_clipboard.py in a folder where you want to keep your scripts. For example:

{Full_Path_to_File}\components_to_clipboard.py

2. Add the Directory to the System PATH

You need to add the folder containing the script to your system's PATH.

  2.1 Press Win + R, type sysdm.cpl, and hit Enter.
  <img width="286" alt="image" src="https://github.com/user-attachments/assets/d4d568c3-f0d1-45e2-ab66-10ae403f0ead" />

  2.2 Navigate to the Advanced tab and click Environment Variables.
  <img width="308" alt="image" src="https://github.com/user-attachments/assets/77913ff1-a156-4c2f-a3e6-422353f8b4e1" />

  2.3 Under System variables, find and select the Path variable, then click Edit.
  <img width="423" alt="image" src="https://github.com/user-attachments/assets/0d196c25-1893-4278-afa7-cb95258b9c1d" />

  2.4 Click New and add the full path to the folder (e.g., C:\Users\YourUsername\Scripts\).
  <img width="377" alt="image" src="https://github.com/user-attachments/assets/b9cae7af-411b-44ca-b27c-18fc8d999932" />

  2.5 Click OK to save and exit.

3. Create a Batch File (Alias cwkv)

To allow running the script by typing cwkv, create a batch file:

  3.1 Open any text editor and paste the following:

      @echo off
      python "<PATH_TO_SCRIPT>" %*

  3.2 Save the file as cwkv.bat in the same folder as your script.
  <img width="144" alt="image" src="https://github.com/user-attachments/assets/8c91058c-0ae4-428c-b8cb-f8b039cb3cdb" />

  3.3 Test it by opening a new command prompt and typing:
    cwkv
<img width="256" alt="image" src="https://github.com/user-attachments/assets/d1cdddbc-46e6-4e74-afa3-312e1fffd9d0" />

  If the script runs, the setup is complete. :)
