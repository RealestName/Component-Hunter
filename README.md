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

  2.2 Navigate to the Advanced tab and click Environment Variables.

  2.3 Under System variables, find and select the Path variable, then click Edit.

  2.4 Click New and add the full path to the folder (e.g., C:\Users\YourUsername\Scripts\).

  2.5 Click OK to save and exit.

3. Create a Batch File (Alias cwkv)

To allow running the script by typing cwkv, create a batch file:

  3.1 Open any text editor and paste the following:

      @echo off
      python "C:\Users\YourUsername\Scripts\components_to_clipboard.py" %*

  3.2 Save the file as cwkv.bat in the same folder as your script.

  3.3 Test it by opening a new command prompt and typing:

    cwkv

  If the script runs, the setup is complete. :)
