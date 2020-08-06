# share-web-whatsapp
Python script to share web WhatsApp's session files so another person can open web WhatsApp using shared session files without scanning QR code.

# How to use 
1. Install selenium by `pip install selenium`.
2. Setup python selenium chromedriver, I suggest google it according to your OS.
3. Run Python scripts as explains follow.

# To generate session file 
1. Run `session_generator.py` with/without a argument for session file name for example `python session_generator.py "Name of session file"` and if you run it without session file name argument then it will name files with increasing numerically.
3. Scan QR code and wait for windows to close.
2. Share generated file.

# To open web whatsapp from generated
