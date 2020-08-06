from selenium import webdriver
from time import sleep
import sys
from os import listdir, path, makedirs

makedirs("sessions", exist_ok=True)

sessionFileName = "%02d" % (len(listdir("sessions")))

if len(sys.argv) == 2:
    sessionFileName = sys.argv[1]

driver = webdriver.Chrome("./chromedriver")

driver.get("https://web.whatsapp.com/")

print("Waiting for QR code scan...")

while "WAToken1" not in driver.execute_script("return window.localStorage;"):
    continue

sleep(5)

session = driver.execute_script("return window.localStorage;")

with open(path.join("sessions", sessionFileName), "w", encoding="utf-8") as sessionFile:
    sessionFile.write(str(session))

print("Your session file is saved to: " + path.join("sessions", sessionFileName))

driver.close()
