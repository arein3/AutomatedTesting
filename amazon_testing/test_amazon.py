from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def test_blender_brand():
    print("testing blender brand presence")
    browser = webdriver.Chrome() # can be called browser or driver
    browser.get("http://www.amazon.com")
    time.sleep(10)
    browser.close()


if __name__ == "__main__":
    test_blender_brand()
    print("done.")
