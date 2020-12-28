# share-web-whatsapp (SWW)

Python scripts to share web WhatsApp's session file. So another person can open web WhatsApp using a shared session file
without scanning QR code.

# How to use

Watch this [Video](https://www.youtube.com/watch?v=YGE97m6bUNo), It's in Hindi with English subtitles.

1. Install selenium by `pip install selenium` OR `pip install -r requirements.txt`.
2. Setup python selenium chrome driver, I suggest google it according to your OS.
3. Run Python scripts as follows.

# To generate a session file

1. Run `session_generator.py` and it will save "session_file.wa" file.
2. Scan QR code and wait for the window to close.
3. Share the generated session file.

# To open web WhatsApp from generated session file

1. Run `session_opener.py` and it will open "session_file.wa" file.
2. It will open a Web WhatsApp session after a refresh.
