import time
import ast
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def reset_button():
    driver.find_element(By.XPATH, "//*[text()='Reset']").click()

def get_equation(n):
    eq = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//ol//li[{n}]"))
    )
    return eq.text
def add_element(id, key):
    driver.find_element(By.ID, id).send_keys(key)

def result(ans):
    div_coins = driver.find_element(By.CLASS_NAME, "coins")
    button = div_coins.find_element(
                    By.XPATH, f".//button[text()='{ans}']")
    button.click()



try:
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    driver.get("http://sdetchallenge.fetch.com/")  
    add_element("left_0", 0)
    add_element("left_1", 1)
    add_element("left_2", 2)
    add_element("right_0", 3)
    add_element("right_1", 4)
    add_element("right_2", 5)
    weigh = driver.find_element(By.ID, "weigh")
    weigh.click()
    tt = get_equation(1)
    print(tt)
    if "=" in tt:
        reset_button()
        add_element("left_0", 6)
        add_element("right_0", 7)
        weigh.click()
        ntt = get_equation(2)   
        if "=" in ntt:
            result(8)
        if "<" in ntt:
            result(6)
        if ">" in ntt:
            result(7)

    if "<" in tt:
        expressions = tt.split("<")
        lhs = expressions[0].strip()
        lhs = ast.literal_eval(lhs)
        reset_button()
        add_element("left_0", lhs[0])
        add_element("right_0", lhs[1])
        weigh.click()
        ntt =get_equation(2)
        if "=" in ntt:
            result(lhs[2])
        if "<" in ntt:
            result(lhs[0])
        if ">" in ntt:
           result(lhs[1])
    if ">" in tt:
        expressions = tt.split(">")
        rhs = expressions[1].strip()
        print(rhs)
        rhs = ast.literal_eval(rhs)
        reset_button()
        add_element("left_0", rhs[0])
        add_element("right_0", rhs[1])
        weigh.click()
        ntt = get_equation(2)
        if "=" in ntt:
            result(rhs[2])    
        if "<" in ntt:
            result(rhs[0])
        if ">" in ntt:
            result(rhs[1])
            


except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

finally:
    time.sleep(5)
    driver.quit()