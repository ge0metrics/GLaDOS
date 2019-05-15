# GLaDOS
* A non-lethal computer pest
* `Aperture Antivirus.pyw` is a small Python program that imports GLaDOS and periodically calls on her 'tasks'
* Upon instantiation, GLaDOS (`/modules/GLaDOS.py`) will monitor the USB ports and keys pressed in order to deliver appropriate voice lines at the execution of certain tasks. She will yell at you when you plug in a USB storage device, and express relief when you remove it. She will also make various comments depending on what you type.
* Use the system tray icon to kill GLaDOS

# **NEITHER GLaDOS OR APERTURE ANTIVIRUS WILL HARM/FIX YOUR PC!**
* This is just for fun! GLaDOS' keylogging is not stored or sent anywhere, and is erased every hundred logged keys of finding nothing interesting to respond to. Likewise, GLaDOS does not really delete files, even if she says she did and she cannot mess with any of your USB storage devices beyond acknowledging that they exist. 

# Dependencies
- `pip install pypiwin32`
- `pip install playsound`
- `pip instal pyttsx3`
- https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook **note**: it is easier to install pyHook from here BUT GLaDOS will crash silently if you enter a window with some non-ascii character in the title. this is a bug with this version of pyHook. a better version with this bug fixed can be found here: https://github.com/Answeror/pyhook_py3k and installed using the following instructions: https://stackoverflow.com/questions/36109533/install-pyhook-3-5. you may also need to follow these instructions for installing swig: https://stackoverflow.com/questions/44504899/installing-pocketsphinx-python-module-command-swig-exe-failed

# Credits
* All sounds from here: https://theportalwiki.com/wiki/GLaDOS_voice_lines
