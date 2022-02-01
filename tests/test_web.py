import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

url="https://www.mozilla.org"
title="Internet for people"

@pytest.fixture
def webFix():
    driver=webdriver.Firefox(executable_path=r'C:\geckodriver-v0.30.0-win64\geckodriver.exe')
    driver.get(url)
    try:
        element=wait(driver,10).until(EC.title_contains(title))
    except Exception as ex:
        print(ex)
    yield driver

    driver.quit()

def test_web_link(webFix):
    title=webFix.title
    assert 'Internet para la ' in title
    webFix.find_element_by_link_text("Legal").click()
    
def test_web_links(webFix):
    links=webFix.find_elements_by_tag_name("a")
    for i in links:
        href=i.get_attribute("href")
        assert 'cnbc.com' in href or 'bbc.com' in href or 'mozilla' in href




#def test_add():
 #   assert 2+3==5
