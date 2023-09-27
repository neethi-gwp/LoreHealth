import os
import platform
import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def before_scenario(context, scenario):
    chromedriver_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), ".." , "core/resources"))
    os_name = platform.system()
    machine = platform.machine()
    chromedriver_path = ""

    if "Darwin" in os_name:
        if 'arm64' in machine:
            chromedriver_path = chromedriver_dir + "/mac_chromedriver"
        else:
            chromedriver_path = chromedriver_dir + "/mac_intel_chromedriver"
    elif "Linux" in os_name:
        chromedriver_path = chromedriver_dir + "/linux_chromedriver"
    elif "Windows" in os_name:
        chromedriver_path = chromedriver_dir + "/win_chromedriver.exe"

    context.browser = webdriver.Chrome(service=Service(chromedriver_path))
    context.browser.maximize_window()


def after_scenario(context, scenario):
    context.browser.quit()


def before_feature(context, feature):
    if 'StoreEpochTime' in feature.tags:
        context.epoch_time = str(int(time.time()))