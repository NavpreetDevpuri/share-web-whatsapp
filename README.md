# share-web-whatsapp (SWW)

Python script to share web WhatsApp's session files so another person can open web WhatsApp using shared session files without scanning QR code.

# How to use

1. Install selenium by `pip install selenium` OR `pip install -r requirements.txt`.
2. Setup python selenium chromedriver, I suggest google it according to your OS.
3. Run Python scripts as explains follow.

# To generate session file

1. Run `session_generator.py` with/without a argument for session file name for example `python session_generator.py "Name of session file"` and if you run it without session file name argument then it will name files with increasing numerically.
2. Scan QR code and wait for window to close.
3. Share generated session file.

# To open web whatsapp from generated session file

1. Run `session_opener.py` with/without a argument for session file name for example `python session_generator.py "Name of session file"` and if you run it without session file name argument then it will try default file "00"
2. It will open web whatsapp session.
