from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os
import sys
import subprocess



opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--window-size=500,500");
opt.add_argument("--allow-insecure-localhost");

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.notifications": 1
  })



driver = webdriver.Chrome(executable_path="/home/endavouros/Sankara/WW/app/./chromedriver", chrome_options=opt)

driver.get("http://127.0.0.1:8080/")
c=int(float(87))

time.sleep(5)

while(1):

    value = driver.find_element_by_xpath("/html/body/section[1]/div[2]/div[2]/span[2]");
    time.sleep(0.5)
    absValue=value.text
    real = absValue.replace("%", "")
    realreal = int(float(real))
    print("real is : " +real)


    if realreal >= c:

        print("You called me")
        os.system("python vad.py")




