import sys
import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import subprocess

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
chrome_options.binary_location = "/usr/bin/google-chrome"
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=chrome_options)

driver.get("https://ttp.cbp.dhs.gov/schedulerui/schedule-interview/location?lang=en&vo=true&service=UP")
time.sleep(2)

SFO = 'US34'
BOS = 'US190'
#ANC = 'US10' # anchorage usually has free slots, so this is a test that the script still works.
center_id_prefix = "centerDetails"

def check_loc(loc):
    res = None
    while True:
        try:
            driver.find_element(by=By.ID, value=center_id_prefix + loc).click()
            time.sleep(1)
            res = driver.find_element(by=By.CLASS_NAME, value="nextAppointment").text
            break
        except Exception as e:
            print(f"page load error, retry: {e}")
            time.sleep(1)
            continue

    if 'No appointments available for this location' == res:
        return None
    elif res.startswith('Next Available Appointment'):
        return res
    else:
        raise Exception("Unexpected formatting")

print('checking SFO')
sfo = check_loc(SFO)
print(sfo)
print('checking BOS')
bos = check_loc(BOS)
print(bos)

if sfo != None or bos != None:
    print("sending email")
    subprocess.run(f'echo "sfo: {sfo} bos: {bos}" | mutt -s "TTP Appointment" -- {sys.argv[1]}', shell=True)

driver.quit()
