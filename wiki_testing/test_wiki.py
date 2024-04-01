from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def test_wiki_python():
    print("testing wikipedia results to see if BDFL is mentionedin python results") #Benevolent dictator for life
    browser = webdriver.Chrome() # can be called browser or driver
    browser.get("http://www.wikipedia.org")
    query = "Python (programming language)"
    search_input = browser.find_element(By.ID, "searchInput")
    search_input.clear()
    search_input.send_keys(query)
    search_input.send_keys(Keys.RETURN)
    assert "Guido" in browser.page_source #Guido van rossum - founder of python (BDFL)

    time.sleep(20)
    browser.close()

def test_wiki_CPP():
    print("testing wikipedia results to see if Bjarne is mentioned in C++ results") 
    browser = webdriver.Chrome() # can be called browser or driver
    browser.get("http://www.wikipedia.org")
    query = "C++"
    search_input = browser.find_element(By.ID, "searchInput")
    search_input.clear()
    search_input.send_keys(query)
    search_input.send_keys(Keys.RETURN)
    assert "Bjarne Stroustrup" in browser.page_source #G

    time.sleep(3)
    browser.close()


if __name__ == "__main__":
    test_wiki_python()
    test_wiki_CPP()
    print("done.")
