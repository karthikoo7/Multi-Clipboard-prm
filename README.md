# Multi-Clipboard-prm
You want to be able to run this program with a command line argument that is a short key phrase—for instance, agree or busy. The message associated with that key phrase will be copied to the clipboard so that the user can paste it into an email. This way, the user can have long, detailed messages without having to retype them.
* to check on pycharm, run the code and edit configuration in the drop down menu beside the green play button and pass the parameter in the script parameter field that you want is sys.srgv[1]
Install pyperclip:
PyCharm > Preferences > Python Interpreter > click + > search for pyperclip > Install.
Or open Terminal and run:
pip install pyperclip

Open Command Prompt and test your script manually first:
python "C:\Path\To\mclip.py" agree
If this works and copies text to clipboard, you're ready to make a .bat file.

📄 2. Create a Batch File (e.g., mclip.bat)
Open Notepad.

Paste this code:
@echo off
python "C:\Path\To\Your\mclip.py" %1
Replace C:\Path\To\Your\mclip.py with the full path to your script.

Save the file as:
mclip.bat
but with Save as type: All Files, so it’s not mclip.bat.txt.

You can place this batch file:

In the same folder as your script (for testing),
Or, ideally, somewhere like C:\Scripts\ for system-wide access.

Win + r and then browse and run the batch file with the argument; agree/busy/upsell
Example: C:\Users\HP\Desktop\mclip.bat upsell (in win+r)
and the text is now in your clipboard just paste wherever you want.
