# share-web-whatsapp (SWW)

Python script to share web WhatsApp's session files so another person can open web WhatsApp using shared session files without scanning QR code.

# How to use

1. Install selenium by pip install selenium OR pip install -r requirements.txt.
2. Setup python selenium chrome driver, I suggest google it according to your OS.
3. Run Python scripts as explains follow.

# To generate a session file

1. Run session_generator.py with/without an argument for a session file name for example python session_generator.py "Name of session file" and if you run it without session file name argument then it will name files with increasing numerically.
2. Scan QR code and wait for the window to close.
3. Share the generated session file.

# To open web WhatsApp from generated session file

1. If you want to give the only file name as an argument then put it to the same directory as python script or put that session file to folder sessions or provide a direct link to that file while running script.
2. Run session_opener.py with/without an argument for the session file name, for example, python session_generator.py "Name of session file" and if you run it without session file name argument then it will try default file "00"
3. It will open a web WhatsApp session.
