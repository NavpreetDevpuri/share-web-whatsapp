from selenium import webdriver
from time import sleep
import sys
from os import path, listdir

sessionName = "00"

if len(sys.argv) == 2:
    sessionName = sys.argv[1]

driver = webdriver.Chrome("./chromedriver")

driver.get("https://web.whatsapp.com/")

sleep(1)

print("Injecting session...")

session = None

with open(path.join("sessions", sessionName), "r") as sessionFile:
    session = eval(sessionFile.read())

driver.execute_script(
    """
var keys = Object.keys(arguments[0]);
var values = Object.values(arguments[0]);
for(i=0;i<keys.length;++i) window.localStorage.setItem(keys[i], values[i]);
""",
    session,
)

driver.refresh()
input("Enter any key to exit.")
driver.close()
